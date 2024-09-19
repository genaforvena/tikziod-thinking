## Interactive HTML Intersecting Texts Visualizer with Word Counters and Hover Effects

This script generates an interactive HTML visualization of intersecting texts, featuring word counters, hover effects, and dynamic highlighting.

### Basic Usage

The script supports two methods of input: file input and direct text input via command line.

### Example output

https://genaforvena.github.io/tikziod-thinking/

https://genaforvena.github.io/tikziod-thinking/anti-oediupus.html to check the visualization of the book "Anti-Oedipus" by Deleuze and Guattari. It is large and may take a while to load.

#### File Input

1. Create a text file with your input texts, one per line. For example, `input.txt`:

   ```
   The quick brown fox jumps over the lazy dog
   A quick brown dog jumps over the lazy cat
   The lazy fox and the quick cat are friends
   ```

2. Run the script with the file input option:

   ```
   python main.py -f input.txt
   ```

#### Direct Text Input

You can provide texts directly as command-line arguments. Make sure to enclose each text in quotes:

```
python main.py -t "First text here" "Second text here" "Third text here"
```

### Viewing the Visualization

After running the script:

1. An interactive HTML file named `intersecting_texts.html` will be generated in the same directory.

2. Open this file in any modern web browser to view the visualization.

3. Ensure you have an internet connection when viewing the HTML file, as it uses Google Fonts.

### Understanding the Output

- Each input text is displayed as a separate paragraph, prefixed with "Text 1:", "Text 2:", etc.
- Words that appear in more than one text are highlighted in bold and assigned a unique typeface.
- The font size of each word is proportional to its frequency across all texts.
- Common words (those appearing in multiple texts) are clickable and have hover effects.

### Interactive Features

- When you hover over a common word:
  - A counter appears above the word, showing its current occurrence and total occurrences.
  - All instances of that word across all texts are highlighted.
- Common words are clickable. When you click on a common word, the page will smoothly scroll to the next occurrence of that word in another text.
- The target word is briefly highlighted when scrolled to, making it easy to locate.
- You can continue clicking to cycle through all occurrences of the word across different texts.

### Tips for Optimal Results

1. **Input Text Length**: The visualization works best with texts that are neither too short nor too long. Aim for sentences or short paragraphs.

2. **Number of Texts**: The script can handle multiple texts, but for clarity, it's best to use 2-5 texts at a time.

3. **Word Frequency**: The visualization is most effective when there's a good mix of common and unique words. This creates an interesting visual hierarchy while maintaining readability.

### Customization

- If you want to use different fonts, you can modify the `fonts` list in the script. Make sure to also update the Google Fonts link in the HTML template if you add new fonts.
- You can adjust the `calculate_font_size` function in the script to change how word frequency affects font size.
- The appearance of the counters and highlighting can be modified by adjusting the CSS in the HTML template.

### Troubleshooting

If you encounter any issues:

1. Ensure you're using the latest version of the script.
2. Check that you have a modern web browser to view the HTML file.
3. Make sure you have an active internet connection to load the Google Fonts.
4. If the interactive features are not working, check your browser's JavaScript settings.

Note: If you need to convert the HTML to PDF, the interactive features and custom fonts may not be preserved in the PDF version.

### Recent Updates

- Added hover effects to show word counters only when hovering over words.
- Implemented dynamic highlighting of all instances of a word when hovering.
- Fixed JSON serialization issues for improved compatibility with various input texts.
- Improved smooth scrolling behavior with fallback for older browsers.

For any further questions or issues, please refer to the script comments or reach out to the project maintainers.
