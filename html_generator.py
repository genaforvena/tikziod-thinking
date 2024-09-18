import re
import random
import math
import html
import json
from utils import CustomEncoder

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
    word_counts_json = json.dumps(word_counts)
    
    with open('templates/visualization.html', 'r') as template_file:
        template = template_file.read()
    
    text_html = ""
    for i, text in enumerate(texts):
        text_html += f'<div class="text"><p>'
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
                text_html += f'<span class="word-container">'
                text_html += f'<span class="counter"><span class="current">{current_index}</span>/<span class="total">{count}</span></span>'
                if count > 1:
                    next_positions = [pos for pos in positions if pos > (i, current_position)]
                    if next_positions:
                        next_text_index, next_position = next_positions[0]
                    else:
                        next_text_index, next_position = positions[0]
                    text_html += f'<a href="#word-{html.escape(word)}-{next_text_index}-{next_position}" id="word-{html.escape(word)}-{i}-{current_position}" data-word="{html.escape(word)}" class="word common-word" style="font-family: \'{font}\', sans-serif; font-size: {font_size}%;">{html.escape(token)}</a>'
                else:
                    text_html += f'<span class="word" style="font-size: {font_size}%;">{html.escape(token)}</span>'
                text_html += '</span> '
            else:
                text_html += f'<span class="punctuation">{html.escape(token)}</span>'
            current_position += len(token) + 1
        text_html += '</p></div>'
    return template.format(word_positions_json=word_positions_json, word_counts_json=word_counts_json, text_content=text_html)
