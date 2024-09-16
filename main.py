import re
from collections import defaultdict
import random

def process_texts(texts):
    # Normalize and tokenize texts
    word_sets = [set(re.findall(r'\w+', text.lower())) for text in texts]
    
    # Find common words
    all_words = set.union(*word_sets)
    word_counts = defaultdict(int)
    for word in all_words:
        word_counts[word] = sum(word in s for s in word_sets)
    
    # Assign positions (simplified for demonstration)
    positions = {}
    for word in all_words:
        positions[word] = (random.uniform(0, 10), random.uniform(0, 10))
    
    return word_sets, word_counts, positions

def generate_latex(texts, word_sets, word_counts, positions):
    latex_output = r"""
\documentclass{article}
\usepackage{tikz}
\usepackage[margin=1cm]{geometry}
\begin{document}
\begin{tikzpicture}[remember picture, overlay]
"""
    
    # Draw lines for each text
    colors = ['red', 'blue', 'green', 'orange', 'purple']
    for i, words in enumerate(word_sets):
        path = []
        for word in words:
            x, y = positions[word]
            path.append(f"({x},{y})")
        
        color = colors[i % len(colors)]
        latex_output += f"\\draw[{color}, opacity=0.5] {' -- '.join(path)};\n"
    
    # Place words
    for word, (x, y) in positions.items():
        size = 'tiny' if word_counts[word] == 1 else 'small' if word_counts[word] == 2 else 'normalsize'
        latex_output += f"\\node[{size}] at ({x},{y}) {{{word}}};\n"
    
    latex_output += r"""
\end{tikzpicture}
\end{document}
"""
    return latex_output

# Example usage
texts = [
    "The quick brown fox jumps over the lazy dog",
    "A quick brown dog jumps over the lazy cat",
    "The lazy fox and the quick cat are friends"
]

word_sets, word_counts, positions = process_texts(texts)
latex_code = generate_latex(texts, word_sets, word_counts, positions)

print(latex_code)

# Save to file
with open('intersecting_texts.tex', 'w') as f:
    f.write(latex_code)
