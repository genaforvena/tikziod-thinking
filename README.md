## Interactive HTML Intersecting Texts Visualizer with Word Counters and Hover Effects

This script generates an interactive HTML visualization of intersecting texts, featuring word counters, hover effects, and dynamic highlighting.

### Basic Usage

The script supports two methods of input: file input and direct text input via command line.

### Example output

https://genaforvena.github.io/tikziod-thinking/


* [Scum Manifesto](https://genaforvena.github.io/tikziod-thinking/scum_manifesto.html) - The only thing worth reading. The rest are paste.
* [Scum Manifesto - degendered](https://genaforvena.github.io/tikziod-thinking/scum_manifesto.html?state=eyJzbGlkZXIiOiIwIiwiaGlnaGxpZ2h0ZWQiOlsiY29tcGxldGUiLCJkdWN0aW9uIiwicmVwcm8iLCJlbW90aW9uYWxseSIsInBoeXNpY2FsIiwic2Vuc2F0aW9ucyIsIm9ic2Vzc2VkIiwic2NyZXdpbmciLCJjb25zdGFudGx5Iiwic2Vla2luZyIsImRlc2lyZSIsImFnYWluc3QiLCJmZWVsIiwiY29tcGFzc2lvbiIsImRydWdzIiwiYWJzb3JiZWQiLCJ0aGVpciIsInByb2plY3RzIiwiaGFwcGluZXNzIiwib3V0c2lkZSIsInlvdXJzZWxmIiwiZnVja2luZyIsInVwIl0sImN1cnNvcnMiOnsiY29tcGxldGUiOjAsImR1Y3Rpb24iOjAsInJlcHJvIjowLCJlbW90aW9uYWxseSI6MCwicGh5c2ljYWwiOjAsInNlbnNhdGlvbnMiOjAsIm9ic2Vzc2VkIjowLCJzY3Jld2luZyI6MCwiY29uc3RhbnRseSI6MCwic2Vla2luZyI6MCwiZGVzaXJlIjowLCJhZ2FpbnN0IjowLCJmZWVsIjowLCJjb21wYXNzaW9uIjowLCJkcnVncyI6MCwiYWJzb3JiZWQiOjAsInRoZWlyIjowLCJwcm9qZWN0cyI6MCwiaGFwcGluZXNzIjowLCJvdXRzaWRlIjowLCJ5b3Vyc2VsZiI6MCwiZnVja2luZyI6MCwidXAiOjB9LCJyZW1vdmVkIjpbIndvbWVuIiwiZmVtYWxlcyIsIm1vbmV5IiwibWFsZSIsInNleCIsImF1dG9tYXRpb24iLCJzb2NpZXR5Iiwic3lzdGVtIiwibWFsZXMiLCJyZXByb2R1Y2UiLCJvZiIsInByb2R1Y2UiLCJmZW1hbGUiLCJnZW5lIiwiaW5jb21wbGV0ZSIsIm1hbGVuZXNzIiwiaGltc2VsZiIsImhlIiwiaGlzIiwibWVuIiwibWFuIiwiaGltIiwicHVzc3kiLCJ3b21hbiIsIm1vdGhlcmhvb2QiLCJlbnZ5IiwiZHJhZyIsInF1ZWVuIiwiY29jayIsIm1hbmhvb2QiLCJzaGUiLCJtb3RoZXIiLCJmYXRoZXJob29kIiwiaGVyIiwia2lkcyIsImRhZGR5IiwiZmF0aGVyIiwibWFycmlhZ2UiLCJkYWQiLCJkeSIsImJveSIsImdpcmwiLCJtYW1hIiwiYm9vYmllcyJdLCJzdHJ1Y2tPdXQiOltdfQ==) - Removing all gender related words from Scum Manifesto make it even more true.
* [Tolstoy's Gospel](https://genaforvena.github.io/tikziod-thinking/gospel.html#word-son-36-11?state=eyJzbGlkZXIiOiIwIiwiaGlnaGxpZ2h0ZWQiOlsibGV0IiwiYXMiLCJvdXIiXSwiY3Vyc29ycyI6eyJsZXQiOjAsImFzIjowLCJvdXIiOjF9LCJyZW1vdmVkIjpbInNvbiIsImdvZCIsIm1hbiIsIm1lbiIsImZhdGhlciIsImhpcyIsImhpbXNlbGYiLCJldmlsIiwiZm9yZ2l2ZSIsImRlYnRzIiwiZXJyb3JzIiwibWlzdGFrZXMiLCJub3QiLCJubyIsImRlYnRvcnMiXSwic3RydWNrT3V0IjpbXX0=) - A visualization of the Gospel by Tolstoy in correct form .
* [LP Tractatus](https://genaforvena.github.io/tikziod-thinking/logico.html) - Young Wittgenstein's Tractatus Logico-Philosophicus.
* [Worstward Hoe by Beckett](https://genaforvena.github.io/tikziod-thinking/worstward_hoe.html) - A visualization of the book "Worstward Hoe" by Samuel Beckett.
* [Илья Масодов - Мрак твоих глаз](https://genaforvena.github.io/tikziod-thinking/mrak_rus.html) - Илья Масодов "Мрак твоих глаз" (a masterpiece in russian, yet to be translated into English).
* [Ilya Masodov - The darkness of your eyes](https://genaforvena.github.io/tikziod-thinking/mrak_eng_machine.html) - The masterpiece from above in English, roughly translated with small llms (low quality, yet to be edited).
* [Anti-Oedipus](https://genaforvena.github.io/tikziod-thinking/anti-oedipus.html) to check the visualization of the book "Anti-Oedipus" by Deleuze and Guattari. It is large and may take a while to load.

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
