import re
from collections import defaultdict
import random
import argparse

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

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

def main():
    parser = argparse.ArgumentParser(description="Generate intersecting texts visualization.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', type=str, help="Path to file containing texts (one per line)")
    group.add_argument('-t', '--texts', nargs='+', help="List of texts to visualize")
    args = parser.parse_args()

    if args.file:
        texts = read_file(args.file)
    else:
        texts = args.texts

    word_sets, word_counts, positions = process_texts(texts)
    latex_code = generate_latex(texts, word_sets, word_counts, positions)

    with open('intersecting_texts.tex', 'w') as f:
        f.write(latex_code)
    
    print("LaTeX file 'intersecting_texts.tex' has been generated.")
    print("Compile it using 'pdflatex intersecting_texts.tex' to create the PDF visualization.")

if __name__ == "__main__":
    main()
