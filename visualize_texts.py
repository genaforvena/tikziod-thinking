import re
from collections import defaultdict
import argparse
import random
import math
import html
import json

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
            .word-container {{ display: inline-block; vertical-align: bottom; margin-right: 5px; text-align: center; position: relative; }}
            .word {{ display: inline-block; }}
            .common-word {{ font-weight: bold; text-decoration: none; color: inherit; }}
            .common-word:hover {{ text-decoration: underline; }}
            .counter {{ display: none; font-size: 10px; color: #666; position: absolute; top: -15px; left: 50%; transform: translateX(-50%); white-space: nowrap; }}
            .punctuation {{ display: inline-block; vertical-align: bottom; margin-right: 5px; }}
            .highlight {{ background-color: yellow; }}
        </style>
        <script>
        const wordPositions = {word_positions_json};

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
            if (counter) {{
                counter.style.display = 'block';
            }}
        }}

        function hideCounter(element) {{
            const counter = element.querySelector('.counter');
            if (counter) {{
                counter.style.display = 'none';
            }}
        }}

        function highlightWords(word) {{
            const elements = document.querySelectorAll(`[data-word="${{word}}"]`);
            elements.forEach(el => el.classList.add('highlight'));
        }}

        function unhighlightWords(word) {{
            const elements = document.querySelectorAll(`[data-word="${{word}}"]`);
            elements.forEach(el => el.classList.remove('highlight'));
        }}

        document.addEventListener('DOMContentLoaded', function() {{
            const commonWords = document.querySelectorAll('.common-word');
            commonWords.forEach(word => {{
                word.addEventListener('mouseover', function() {{
                    showCounter(this.parentNode);
                    highlightWords(this.dataset.word);
                }});
                word.addEventListener('mouseout', function() {{
                    hideCounter(this.parentNode);
                    unhighlightWords(this.dataset.word);
                }});
                word.addEventListener('click', function(e) {{
                    if (!supportsNativeSmoothScroll()) {{
                        e.preventDefault();
                        smoothScroll(this.getAttribute('href'));
                    }}
                }});
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

def main():
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
    print("Open this file in a web browser to view the visualization.")

if __name__ == "__main__":
    main()
