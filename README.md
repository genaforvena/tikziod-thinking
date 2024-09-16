# README.md

# Intersecting Texts Visualizer

This project creates a unique visualization of multiple texts, representing them as intersecting lines with words positioned at their intersection points. It uses Python for text processing and LaTeX with TikZ for rendering the final visualization.

## Features

- Process multiple input texts to find common words
- Generate a visual representation where texts are shown as intersecting lines
- Words are positioned at intersection points, with size indicating frequency across texts
- Outputs a LaTeX file that can be compiled into a PDF

## Requirements

- Python 3.6+
- LaTeX distribution (e.g., TeX Live, MiKTeX) with TikZ package

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/intersecting-texts-visualizer.git
   cd intersecting-texts-visualizer
   ```

2. Install Python dependencies (if any):
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have a LaTeX distribution installed with the TikZ package.

## Usage

1. Edit the `texts` list in the `visualize_texts.py` script with your desired input texts.

2. Run the Python script:
   ```
   python visualize_texts.py
   ```

3. Compile the generated LaTeX file:
   ```
   pdflatex intersecting_texts.tex
   ```

4. Open the resulting `intersecting_texts.pdf` to view your visualization.

## Customization

- Modify the `process_texts` function to change word positioning logic.
- Adjust the LaTeX template in `generate_latex` for different visual styles.
- Experiment with color schemes, font sizes, and line styles in the TikZ code.
