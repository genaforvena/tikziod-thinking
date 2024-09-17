import re
from collections import defaultdict
import argparse
import random
import math

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def process_texts(texts):
    word_sets = [set(re.findall(r'\b\w+\b', text.lower())) for text in texts]
    all_words = set.union(*word_sets)
    word_counts = defaultdict(int)
    word_positions = defaultdict(list)
    for word in all_words:
        word_counts[word] = sum(text.lower().count(word) for text in texts)
        for i, text in enumerate(texts):
            for match in re.finditer(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE):
                word_positions[word].append((i, match.start()))
    return word_sets, word_counts, word_positions

def calculate_font_size(count, min_count, max_count):
    if min_count == max_count:
        return 100
    if max_count - min_count <= 10:
        # Linear scaling for small ranges
        return 80 + (count - min_count) * 4
    else:
        # Logarithmic scaling for larger ranges
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
    
    html_output = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Interactive Intersecting Texts Visualization</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto&family=Open+Sans&family=Lato&family=Montserrat&family=Raleway&family=Oswald&family=Merriweather&family=Playfair+Display&family=Nunito&family=Quicksand&family=Poppins&family=Archivo&family=Fira+Sans&family=Josefin+Sans&family=Comfortaa&family=Caveat&family=Pacifico&display=swap" rel="stylesheet">
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }
            h1 { color: #333; }
            .text { margin-bottom: 20px; }
            .word { display: inline-block; vertical-align: middle; }
            .common-word { font-weight: bold; cursor: pointer; }
            .common-word:hover { text-decoration: underline; }
        </style>
        <script>
            function jumpToWord(word, textIndex, position) {
                const targetElement = document.getElementById(`word-${word}-${textIndex}-${position}`);
                if (targetElement) {
                    targetElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    targetElement.style.backgroundColor = 'yellow';
                    setTimeout(() => { targetElement.style.backgroundColor = ''; }, 2000);
                }
            }
        </script>
    </head>
    <body>
        <h1>Interactive Intersecting Texts Visualization</h1>
    """
    
    for i, text in enumerate(texts):
        html_output += f'<div class="text"><h2>Text {i+1}:</h2><p>'
        words = re.finditer(r'\b\w+\b', text)
        for match in words:
            word = match.group().lower()
            count = word_counts[word]
            font_size = calculate_font_size(count, min_count, max_count)
            font = word_fonts[word]
            if count > 1:
                positions = word_positions[word]
                current_index = positions.index((i, match.start()))
                next_index = (current_index + 1) % len(positions)
                next_text_index, next_position = positions[next_index]
                html_output += f'<span id="word-{word}-{i}-{match.start()}" class="word common-word" style="font-family: \'{font}\', sans-serif; font-size: {font_size}%;" onclick="jumpToWord(\'{word}\', {next_text_index}, {next_position})">{match.group()}</span> '
            else:
                html_output += f'<span class="word" style="font-size: {font_size}%;">{match.group()}</span> '
        html_output += '</p></div>'
    
    html_output += """
    </body>
    </html>
    """
    return html_output

def main():
    parser = argparse.ArgumentParser(description="Generate interactive intersecting texts visualization with HTML output, unique fonts, clickable links, and variable word sizes.")
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
