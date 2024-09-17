## How to Use the Intersecting Texts Visualizer

### Basic Usage

The script now supports two methods of input: file input and direct text input via command line.

#### File Input

1. Create a text file with your input texts, one per line. For example, `input.txt`:

   ```
   The quick brown fox jumps over the lazy dog
   A quick brown dog jumps over the lazy cat
   The lazy fox and the quick cat are friends
   ```

2. Run the script with the file input option:

   ```
   python visualize_texts.py -f input.txt
   ```

#### Direct Text Input

You can also provide texts directly as command-line arguments:

```
python visualize_texts.py -t "First text here" "Second text here" "Third text here"
```

### Generating the Visualization

After running the script with either input method:

1. The script will generate a LaTeX file named `intersecting_texts.tex`.

2. Compile the LaTeX file to create a PDF:

   ```
   pdflatex intersecting_texts.tex
   ```

3. Open the resulting `intersecting_texts.pdf` to view your visualization.

### Advanced Usage

#### Changing Word Positioning

You can modify the `positions` dictionary in the `process_texts` function to change how words are positioned. For example, to position words in a circle:

```python
import math

def process_texts(texts):
    # ... (earlier part of the function remains the same)

    # Assign positions in a circle
    num_words = len(all_words)
    for i, word in enumerate(all_words):
        angle = 2 * math.pi * i / num_words
        x = 5 + 4 * math.cos(angle)  # Center at (5,5) with radius 4
        y = 5 + 4 * math.sin(angle)
        positions[word] = (x, y)

    return word_sets, word_counts, positions
```

#### Customizing the Visualization

You can modify the LaTeX code in the `generate_latex` function to change the appearance of the visualization. For instance, to change line thickness and word colors:

```python
def generate_latex(texts, word_sets, word_counts, positions):
    # ... (beginning of the function remains the same)
    
    # Draw thicker lines for each text
    colors = ['red', 'blue', 'green', 'orange', 'purple']
    for i, words in enumerate(word_sets):
        path = []
        for word in words:
            x, y = positions[word]
            path.append(f"({x},{y})")
        
        color = colors[i % len(colors)]
        latex_output += f"\\draw[{color}, opacity=0.5, line width=2pt] {' -- '.join(path)};\n"
    
    # Place words with varying colors
    for word, (x, y) in positions.items():
        size = 'tiny' if word_counts[word] == 1 else 'small' if word_counts[word] == 2 else 'normalsize'
        color = colors[word_counts[word] % len(colors)]
        latex_output += f"\\node[{size}, text={color}] at ({x},{y}) {{{word}}};\n"
    
    # ... (rest of the function remains the same)
```

Remember to experiment and adjust these settings to achieve the desired visual effect for your specific texts!
