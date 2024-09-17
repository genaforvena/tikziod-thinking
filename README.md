## How to Use the HTML Intersecting Texts Visualizer with Unique Fonts

### Basic Usage

The script supports two methods of input: file input and direct text input via command line.

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

You can provide texts directly as command-line arguments. Make sure to enclose each text in quotes:

```
python visualize_texts.py -t "First text here" "Second text here" "Third text here"
```

### Viewing the Visualization

After running the script:

1. An HTML file named `intersecting_texts.html` will be generated in the same directory.

2. Open this file in any modern web browser to view the visualization.

3. Ensure you have an internet connection when viewing the HTML file, as it uses Google Fonts.

### Understanding the Output

- Each input text is displayed as a separate paragraph, prefixed with "Text 1:", "Text 2:", etc.
- Words that appear in more than one text are highlighted in bold and assigned a unique typeface.
- The varying typefaces make it easy to spot the same word across different texts.

### Tips for Optimal Results

1. **Input Text Length**: The visualization works best with texts that are neither too short nor too long. Aim for sentences or short paragraphs.

2. **Number of Texts**: The script can handle multiple texts, but for clarity, it's best to use 2-5 texts at a time.

3. **Common Words**: The visualization is most effective when there are some common words between the texts, but not too many. This creates interesting connections without overwhelming the reader with too many font changes.

### Customization

- If you want to use different fonts, you can modify the `fonts` list in the script. Make sure to also update the Google Fonts link in the HTML template if you add new fonts.

### Troubleshooting

If you encounter any issues:

1. Ensure you're using the latest version of the script.
2. Check that you have a modern web browser to view the HTML file.
3. Make sure you have an active internet connection to load the Google Fonts.
4. If some fonts are not displaying correctly, try clearing your browser cache or using a different browser.

If you need to convert the HTML to PDF, you can use various online tools or browser extensions that allow you to save web pages as PDFs. Note that some fonts might not render correctly in PDFs, depending on the conversion method used.
