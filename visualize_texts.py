import re
from collections import defaultdict
import argparse
import random

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def process_texts(texts):
    # Normalize and tokenize texts
    word_sets = [set(re.findall(r'\b\w+\b', text.lower())) for text in texts]
    
    # Find common words
    all_words = set.union(*word_sets)
    word_counts = defaultdict(int)
    for word in all_words:
        word_counts[word] = sum(word in s for s in word_sets)
    
    return word_sets, word_counts

def generate_latex(texts, word_counts):
    latex_output = r"""
\documentclass{article}
\usepackage[margin=1cm]{geometry}
\usepackage{xcolor}
\usepackage[normalem]{ulem}
\usepackage{soul}

\begin{document}

\section*{Intersecting Texts Visualization}

"""
    
    # Define colors for highlighting
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'brown', 'pink']
    word_colors = {}
    
    # Assign colors to common words
    for word, count in word_counts.items():
        if count > 1:
            word_colors[word] = random.choice(colors)
    
    # Add texts with highlighted common words
    for i, text in enumerate(texts):
        latex_output += f"\\textbf{{Text {i+1}:}} "
        words = re.findall(r'\b\w+\b', text)
        for word in words:
            if word.lower() in word_colors:
                color = word_colors[word.lower()]
                latex_output += f"\\textcolor{{{color}}}{{\\uline{{{word}}}}} "
            else:
                latex_output += f"{word} "
        latex_output += "\n\n"
    
    latex_output += r"\end{document}"
    return latex_output

def main():
    parser = argparse.ArgumentParser(description="Generate intersecting texts visualization with highlighted connections.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', type=str, help="Path to file containing texts (one per line)")
    group.add_argument('-t', '--texts', nargs='+', help="List of texts to visualize")
    args = parser.parse_args()

    if args.file:
        texts = read_file(args.file)
    else:
        texts = args.texts

    word_sets, word_counts = process_texts(texts)
    latex_code = generate_latex(texts, word_counts)

    with open('intersecting_texts.tex', 'w') as f:
        f.write(latex_code)
    
    print("LaTeX file 'intersecting_texts.tex' has been generated.")
    print("Compile it using 'pdflatex intersecting_texts.tex' to create the PDF visualization.")

if __name__ == "__main__":
    main()
