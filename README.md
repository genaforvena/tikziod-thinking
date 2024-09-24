# Interactive HTML Intersecting Texts Visualizer with Word Counters and Hover Effects

This script generates an interactive HTML visualization of intersecting texts, featuring word counters, hover effects, and dynamic highlighting. It supports both text and PDF files as input.

## Basic Usage

The script supports three methods of input: text file input, PDF file input, and direct text input via command line.

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

### File Input (Text or PDF)

1. Prepare your input file. This can be either:
   - A text file with your input texts, one per line.
   - A PDF file containing the text you want to visualize.

2. Run the script with the file input option:

   ```
   python main.py -f input.txt
   ```

   or for a PDF file:

   ```
   python main.py -f document.pdf
   ```

#### Direct Text Input

You can provide texts directly as command-line arguments. Make sure to enclose each text in quotes:

```
python main.py -t "First text here" "Second text here" "Third text here"
```

## Viewing and Interacting with the Visualization

After running the script:

1. An interactive HTML file named `index.html` will be generated in the `docs` folder.

2. Open this file in any modern web browser to view the visualization.

3. The visualization offers a rich set of interactive features:

   - **Word Selection**: Click on any word to highlight all its occurrences across the text(s). Each selected word gets a unique color.
   
   - **Word Controls**: For each selected word, a control panel appears with options to:
     - Remove the word (replacing it with underscores)
     - Strike out the word
     - Navigate between occurrences ("Go to", "Previous", "Next")
     - View the current occurrence number out of total occurrences
   
   - **Frequency Slider**: Use the slider to hide less frequent words, dynamically updating the visualization.
   
   - **Hidden Words Popup**: View a list of words hidden by the frequency slider.
   
   - **Search Functionality**: Use the search bar to find specific words or phrases in the text.
   
   - **Shareable State**: Generate a shareable link that captures the current state of your visualization, including highlighted, removed, and struck-out words.

4. Additional Interactive Elements:
   - Hover over words to see their frequency across all texts.
   - The font size of words reflects their frequency or importance in the text.
   - Some words may be pre-highlighted or styled differently based on their significance in the text.

5. This visualization technique allows you to engage with the text in new ways, emphasizing certain words or themes and providing a unique perspective on the content.

6. Ensure you have an internet connection when viewing the HTML file, as it uses external resources like Google Fonts.

## Advanced Features

- **State Preservation**: The tool can encode the current state of the visualization (highlighted words, removed words, slider position, etc.) into a URL parameter. This allows you to share or bookmark specific views of the text.

- **Responsive Design**: The interface includes fixed position elements like the search bar and word controls panel for easy access while scrolling through long texts.

- **Performance Optimization**: The tool is designed to handle large texts efficiently, with features like dynamic word hiding to manage visual complexity.

## Customization

You can customize the visualization by modifying the `interactive.js` file:

- Adjust the color scheme for highlighted words
- Modify the behavior of word selection and navigation
- Add new interactive features or buttons
- Customize the styling of various elements (words, control panels, popups)

### Tips for Optimal Results

1. **Input Text Length**: The visualization works best with texts that are neither too short nor too long. Aim for sentences or short paragraphs.

2. **Number of Texts**: The script can handle multiple texts, but for clarity, it's best to use 2-5 texts at a time.

3. **Word Frequency**: The visualization is most effective when there's a good mix of common and unique words. This creates an interesting visual hierarchy while maintaining readability.

### Troubleshooting

If you encounter any issues:

1. Ensure you're using the latest version of the script.
2. Check that you have a modern web browser to view the HTML file.
3. Make sure you have an active internet connection to load the Google Fonts.
4. If the interactive features are not working, check your browser's JavaScript settings.

Note: If you need to convert the HTML to PDF, the interactive features and custom fonts may not be preserved in the PDF version.