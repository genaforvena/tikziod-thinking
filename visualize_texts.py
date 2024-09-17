import re
from aiohttp import web
from collections import defaultdict
import argparse
import random
import math
import html
import json
import asyncio
from ollama import AsyncClient

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def process_texts(texts):
    word_sets = [set(re.findall(r'\b\w+\b', text.lower())) for text in texts]
    all_words = set.union(*word_sets)
    word_counts = defaultdict(int)
    word_positions = defaultdict(list)
    for i, text in enumerate(texts):
        for match in re.finditer(r'\b\w+\b', text, re.IGNORECASE):
            word = match.group().lower()
            word_counts[word] += 1
            word_positions[word].append((i, match.start()))
    return word_sets, word_counts, word_positions

def calculate_font_size(count, min_count, max_count):
    if min_count == max_count:
        return 100
    if max_count - min_count <= 10:
        return 80 + (count - min_count) * 4
    else:
        log_min = math.log(min_count)
        log_max = math.log(max_count)
        log_count = math.log(count)
        return 80 + (log_count - log_min) / (log_max - log_min) * 60


async def get_ollama_continuation(word, context):
    client = AsyncClient()
    prompt = f"Continue the following sentence that contains the word '{word}': {context}"
    response = await client.chat(model='llama2', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']


def generate_html(texts, word_counts, word_positions):
    fonts = [
        'Roboto', 'Open Sans', 'Lato', 'Montserrat', 'Raleway', 'Oswald', 
        'Merriweather', 'Playfair Display', 'Nunito', 'Quicksand', 'Poppins', 
        'Archivo', 'Fira Sans', 'Josefin Sans', 'Comfortaa', 'Caveat', 'Pacifico'
    ]
    word_fonts = {word: random.choice(fonts) for word in word_counts.keys()}
    
    min_count = min(word_counts.values())
    max_count = max(word_counts.values())
    
    word_positions_json = json.dumps(word_positions, cls=CustomEncoder)
    word_counts_json = json.dumps(word_counts)
    
    html_output = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Interactive Intersecting Texts Visualization</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto&family=Open+Sans&family=Lato&family=Montserrat&family=Raleway&family=Oswald&family=Merriweather&family=Playfair+Display&family=Nunito&family=Quicksand&family=Poppins&family=Archivo&family=Fira+Sans&family=Josefin+Sans&family=Comfortaa&family=Caveat&family=Pacifico&display=swap" rel="stylesheet">
        <style>
            html {{
                scroll-behavior: smooth;
            }}
            body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }}
            h1 {{ color: #333; }}
            .text {{ margin-bottom: 20px; }}
            .word-container {{ 
                display: inline-block; 
                vertical-align: bottom; 
                margin-right: 5px; 
                text-align: center; 
                position: relative;
            }}
            .word {{ display: inline-block; }}
            .common-word {{ font-weight: bold; text-decoration: none; color: inherit; }}
            .common-word:hover {{ text-decoration: underline; }}
            .counter {{ 
                display: none; 
                font-size: 10px; 
                color: #666; 
                position: absolute; 
                top: -15px; 
                left: 50%; 
                transform: translateX(-50%); 
                white-space: nowrap;
                background-color: white;
                padding: 2px;
                border: 1px solid #ddd;
                border-radius: 3px;
            }}
            #word-actions {{ 
                display: none; 
                position: fixed;
                z-index: 1000;
            }}
            #word-actions button {{ 
                font-size: 12px; 
                color: white; 
                border: none; 
                cursor: pointer; 
                padding: 5px 10px; 
                margin-right: 5px;
            }}
            #hide-button {{ background-color: #f44336; }}
            #strikeout-button {{ background-color: #4CAF50; }}
            #continue-button {{ background-color: #2196F3; }}
            .punctuation {{ display: inline-block; vertical-align: bottom; margin-right: 5px; }}
            .highlight {{ 
                background-color: #FFFF00; 
                box-shadow: 0 0 5px #FFFF00;
            }}
            .hidden {{ display: none !important; }}
            .strikeout {{ text-decoration: line-through; }}
            .next-entry {{ 
                display: none; 
                position: absolute; 
                bottom: -30px; 
                left: 50%; 
                transform: translateX(-50%); 
                background-color: white; 
                border: 1px solid #ddd; 
                padding: 5px; 
                z-index: 1000;
                white-space: nowrap;
            }}
            #continuation-result {{
                display: none;
                position: fixed;
                bottom: 20px;
                left: 20px;
                right: 20px;
                background-color: white;
                border: 1px solid #ddd;
                padding: 10px;
                z-index: 1001;
                max-height: 200px;
                overflow-y: auto;
            }}
            #frequency-slider-container {{
                position: fixed;
                bottom: 20px;
                left: 20px;
                right: 20px;
                background-color: white;
                padding: 10px;
                border: 1px solid #ddd;
                z-index: 1000;
            }}
            #frequency-slider {{
                width: 100%;
           }}
        </style>
        <script>
        const wordPositions = {word_positions_json};
        const wordCounts = {word_counts_json};
        let currentWord = null;
        let currentContext = null;
        let sortedWords = [];

        function supportsNativeSmoothScroll() {{
            return 'scrollBehavior' in document.documentElement.style;
        }}

        function smoothScroll(target) {{
            const targetElement = document.querySelector(target);
            if (targetElement) {{
                window.scrollTo({{
                    top: targetElement.offsetTop,
                    behavior: 'smooth'
                }});
            }}
        }}

        function showCounter(element) {{
            const counter = element.querySelector('.counter');
            if (counter) counter.style.display = 'block';
        }}

        function hideCounter(element) {{
            const counter = element.querySelector('.counter');
            if (counter) counter.style.display = 'none';
        }}

        function highlightWords(word) {{
            const elements = document.querySelectorAll(`[data-word="${{word}}"]`);
            elements.forEach(el => el.classList.add('highlight'));
        }}

        function unhighlightWords(word) {{
            const elements = document.querySelectorAll(`[data-word="${{word}}"]`);
            elements.forEach(el => el.classList.remove('highlight'));
        }}

        function hideWord(word) {{
            const elements = document.querySelectorAll(`[data-word="${{word}}"]`);
            elements.forEach(el => {{
                el.classList.add('hidden');
                hideCounter(el.parentNode);
            }});
        }}

        function showWord(word) {{
            const elements = document.querySelectorAll(`[data-word="${{word}}"]`);
            elements.forEach(el => {{
                el.classList.remove('hidden');
            }});
        }}

        function strikeoutWord(word) {{
            const elements = document.querySelectorAll(`[data-word="${{word}}"]`);
            elements.forEach(el => {{
                el.classList.add('strikeout');
            }});
        }}

        function showNextEntry(element, word) {{
            const positions = wordPositions[word];
            const currentTextIndex = parseInt(element.id.split('-')[2]);
            const currentPosition = parseInt(element.id.split('-')[3]);
            
            let nextEntry = positions.find(pos => 
                pos[0] > currentTextIndex || (pos[0] === currentTextIndex && pos[1] > currentPosition)
            );
            if (!nextEntry) {{
                nextEntry = positions[0];
            }}

            let nextEntryHtml = `<div class="next-entry">Next: Text ${{nextEntry[0] + 1}}</div>`;
            element.parentNode.insertAdjacentHTML('beforeend', nextEntryHtml);
        }}

        function hideNextEntry(element) {{
            const nextEntry = element.parentNode.querySelector('.next-entry');
            if (nextEntry) {{
                nextEntry.remove();
            }}
        }}

        function showWordActions(word, context, x, y) {{
            const wordActions = document.getElementById('word-actions');
            wordActions.style.display = 'block';
            wordActions.style.left = `${{x}}px`;
            wordActions.style.top = `${{y + 20}}px`;  // 20px below the word
            currentWord = word;
            currentContext = context;
        }}

        async function getContinuation(word, context) {{
            const response = await fetch('/get_continuation', {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                }},
                body: JSON.stringify({{ word, context }}),
            }});
            const data = await response.json();
            return data.continuation;
        }}

        function showContinuationResult(continuation) {{
            const resultDiv = document.getElementById('continuation-result');
            resultDiv.textContent = continuation;
            resultDiv.style.display = 'block';
        }}

        function updateWordVisibility(threshold) {{
            const sortedWords = Object.entries(wordCounts).sort((a, b) => a[1] - b[1]);
            const totalWords = sortedWords.length;
            const visibleCount = Math.floor(totalWords * (1 - threshold));
            
            sortedWords.forEach((entry, index) => {{
                const [word, count] = entry;
                const elements = document.querySelectorAll(`[data-word="${{word}}"]`);
                if (index < visibleCount) {{
                    elements.forEach(el => el.classList.remove('hidden'));
                }} else {{
                    elements.forEach(el => el.classList.add('hidden'));
                }}
            }});
        }}

        document.addEventListener('DOMContentLoaded', function() {{
            const wordActions = document.createElement('div');
            wordActions.id = 'word-actions';
            const hideButton = document.createElement('button');
            hideButton.id = 'hide-button';
            hideButton.textContent = 'Hide';
            const strikeoutButton = document.createElement('button');
            strikeoutButton.id = 'strikeout-button';
            strikeoutButton.textContent = 'Strike-out';
            const continueButton = document.createElement('button');
            continueButton.id = 'continue-button';
            continueButton.textContent = 'Continue';
            wordActions.appendChild(hideButton);
            wordActions.appendChild(strikeoutButton);
            wordActions.appendChild(continueButton);
            document.body.appendChild(wordActions);

            const continuationResult = document.createElement('div');
            continuationResult.id = 'continuation-result';
            document.body.appendChild(continuationResult);

            const sliderContainer = document.createElement('div');
            sliderContainer.id = 'frequency-slider-container';
            const slider = document.createElement('input');
            slider.type = 'range';
            slider.id = 'frequency-slider';
            slider.min = '0';
            slider.max = Object.keys(wordCounts);
            slider.value = 0;
            sliderContainer.appendChild(slider);
            document.body.appendChild(sliderContainer);

            sortedWords = Object.keys(wordCounts).sort((a, b) => wordCounts[b] - wordCounts[a]);

            slider.addEventListener('input', function() {{
                const threshold = this.value / 100;
                updateWordVisibility(threshold);
            }});
            const commonWords = document.querySelectorAll('.common-word');
            commonWords.forEach(word => {{
                word.addEventListener('mouseover', function(e) {{
                    showCounter(this.parentNode);
                    highlightWords(this.dataset.word);
                    showNextEntry(this, this.dataset.word);
                    const context = this.closest('p').textContent;
                    showWordActions(this.dataset.word, context, e.pageX, e.pageY);
                }});
                word.addEventListener('mouseout', function() {{
                    hideCounter(this.parentNode);
                    unhighlightWords(this.dataset.word);
                    hideNextEntry(this);
                }});
                word.addEventListener('click', function(e) {{
                    if (!supportsNativeSmoothScroll()) {{
                        e.preventDefault();
                        smoothScroll(this.getAttribute('href'));
                    }}
                }});
            }});

            hideButton.addEventListener('click', function() {{
                if (currentWord) {{
                    hideWord(currentWord);
                    wordActions.style.display = 'none';
                }}
            }});

            strikeoutButton.addEventListener('click', function() {{
                if (currentWord) {{
                    strikeoutWord(currentWord);
                    wordActions.style.display = 'none';
                }}
            }});

            continueButton.addEventListener('click', async function() {{
                if (currentWord && currentContext) {{
                    const continuation = await getContinuation(currentWord, currentContext);
                    showContinuationResult(continuation);
                    wordActions.style.display = 'none';
                }}
            }});

            document.addEventListener('click', function(e) {{
                if (!e.target.closest('.common-word') && !e.target.closest('#word-actions')) {{
                    wordActions.style.display = 'none';
                }}
            }});
        }});
        </script>
    </head>
    <body>
        <h1>Interactive Intersecting Texts Visualization</h1>
    """

    for i, text in enumerate(texts):
        html_output += f'<div class="text"><h2>Text {i+1}:</h2><p>'
        tokens = re.findall(r'\b\w+\b|[^\w\s]', text)
        current_position = 0
        for token in tokens:
            if re.match(r'\w+', token):
                word = token.lower()
                count = word_counts[word]
                font_size = calculate_font_size(count, min_count, max_count)
                font = word_fonts[word]
                positions = word_positions[word]
                current_index = sum(1 for pos in positions if pos <= (i, current_position)) + 1
                html_output += f'<span class="word-container">'
                html_output += f'<span class="counter"><span class="current">{current_index}</span>/<span class="total">{count}</span></span>'
                if count > 1:
                    next_positions = [pos for pos in positions if pos > (i, current_position)]
                    if next_positions:
                        next_text_index, next_position = next_positions[0]
                    else:
                        next_text_index, next_position = positions[0]
                    html_output += f'<a href="#word-{html.escape(word)}-{next_text_index}-{next_position}" id="word-{html.escape(word)}-{i}-{current_position}" data-word="{html.escape(word)}" class="word common-word" style="font-family: \'{font}\', sans-serif; font-size: {font_size}%;">{html.escape(token)}</a>'
                else:
                    html_output += f'<span class="word" style="font-size: {font_size}%;">{html.escape(token)}</span>'
                html_output += '</span> '
            else:
                html_output += f'<span class="punctuation">{html.escape(token)}</span>'
            current_position += len(token) + 1
        html_output += '</p></div>'
    
    html_output += """
    </body>
    </html>
    """
    return html_output

async def get_continuation(request):
    data = await request.json()
    word = data['word']
    context = data['context']
    continuation = await get_ollama_continuation(word, context)
    return web.json_response({'continuation': continuation})

async def main():
    parser = argparse.ArgumentParser(description="Generate interactive intersecting texts visualization with HTML output, unique fonts, clickable links, variable word sizes, hover effects, and preserved punctuation.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', type=str, help="Path to file containing texts (one per line)")
    group.add_argument('-t', '--texts', nargs='+', help="List of texts to visualize")
    args = parser.parse_args()

    if args.file:
        texts = read_file(args.file)
    else:
        texts = args.texts

    word_sets, word_counts, word_positions = process_texts(texts)
    html_code = generate_html(texts, word_counts, word_positions)

    with open('intersecting_texts.html', 'w') as f:
        f.write(html_code)
    
    print("Interactive HTML file 'intersecting_texts.html' has been generated.")
    print("Starting web server...")

    app = web.Application()
    app.router.add_get('/', lambda request: web.FileResponse('intersecting_texts.html'))
    app.router.add_post('/get_continuation', get_continuation)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    print("Server started at http://localhost:8080")
    print("Press Ctrl+C to stop the server")

    # Keep the server running
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
