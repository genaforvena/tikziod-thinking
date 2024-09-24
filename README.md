# Interactive HTML Intersecting Texts Visualizer

This script generates an interactive HTML visualization of intersecting texts, featuring word counters, hover effects, and dynamic highlighting. It now supports multiple file formats and URL-based input.

### Example output

https://genaforvena.github.io/tikziod-thinking/


* [Scum Manifesto](https://genaforvena.github.io/tikziod-thinking/scum_manifesto.html) - The only thing worth reading. The rest are paste.
* [Scum Manifesto - degendered](https://genaforvena.github.io/tikziod-thinking/scum_manifesto.html?state=eyJzbGlkZXIiOiIwIiwiaGlnaGxpZ2h0ZWQiOlsiY29tcGxldGUiLCJkdWN0aW9uIiwicmVwcm8iLCJlbW90aW9uYWxseSIsInBoeXNpY2FsIiwic2Vuc2F0aW9ucyIsIm9ic2Vzc2VkIiwic2NyZXdpbmciLCJjb25zdGFudGx5Iiwic2Vla2luZyIsImRlc2lyZSIsImFnYWluc3QiLCJmZWVsIiwiY29tcGFzc2lvbiIsImRydWdzIiwiYWJzb3JiZWQiLCJ0aGVpciIsInByb2plY3RzIiwiaGFwcGluZXNzIiwib3V0c2lkZSIsInlvdXJzZWxmIiwiZnVja2luZyIsInVwIl0sImN1cnNvcnMiOnsiY29tcGxldGUiOjAsImR1Y3Rpb24iOjAsInJlcHJvIjowLCJlbW90aW9uYWxseSI6MCwicGh5c2ljYWwiOjAsInNlbnNhdGlvbnMiOjAsIm9ic2Vzc2VkIjowLCJzY3Jld2luZyI6MCwiY29uc3RhbnRseSI6MCwic2Vla2luZyI6MCwiZGVzaXJlIjowLCJhZ2FpbnN0IjowLCJmZWVsIjowLCJjb21wYXNzaW9uIjowLCJkcnVncyI6MCwiYWJzb3JiZWQiOjAsInRoZWlyIjowLCJwcm9qZWN0cyI6MCwiaGFwcGluZXNzIjowLCJvdXRzaWRlIjowLCJ5b3Vyc2VsZiI6MCwiZnVja2luZyI6MCwidXAiOjB9LCJyZW1vdmVkIjpbIndvbWVuIiwiZmVtYWxlcyIsIm1vbmV5IiwibWFsZSIsInNleCIsImF1dG9tYXRpb24iLCJzb2NpZXR5Iiwic3lzdGVtIiwibWFsZXMiLCJyZXByb2R1Y2UiLCJvZiIsInByb2R1Y2UiLCJmZW1hbGUiLCJnZW5lIiwiaW5jb21wbGV0ZSIsIm1hbGVuZXNzIiwiaGltc2VsZiIsImhlIiwiaGlzIiwibWVuIiwibWFuIiwiaGltIiwicHVzc3kiLCJ3b21hbiIsIm1vdGhlcmhvb2QiLCJlbnZ5IiwiZHJhZyIsInF1ZWVuIiwiY29jayIsIm1hbmhvb2QiLCJzaGUiLCJtb3RoZXIiLCJmYXRoZXJob29kIiwiaGVyIiwia2lkcyIsImRhZGR5IiwiZmF0aGVyIiwibWFycmlhZ2UiLCJkYWQiLCJkeSIsImJveSIsImdpcmwiLCJtYW1hIiwiYm9vYmllcyJdLCJzdHJ1Y2tPdXQiOltdfQ==) - Removing all gender related words from Scum Manifesto make it even more true.
* [Tolstoy's Gospel](https://genaforvena.github.io/tikziod-thinking/gospel.html#word-son-36-11?state=eyJzbGlkZXIiOiIwIiwiaGlnaGxpZ2h0ZWQiOlsibGV0IiwiYXMiLCJvdXIiXSwiY3Vyc29ycyI6eyJsZXQiOjAsImFzIjowLCJvdXIiOjF9LCJyZW1vdmVkIjpbInNvbiIsImdvZCIsIm1hbiIsIm1lbiIsImZhdGhlciIsImhpcyIsImhpbXNlbGYiLCJldmlsIiwiZm9yZ2l2ZSIsImRlYnRzIiwiZXJyb3JzIiwibWlzdGFrZXMiLCJub3QiLCJubyIsImRlYnRvcnMiXSwic3RydWNrT3V0IjpbXX0=) - A visualization of the Gospel by Tolstoy in correct form .
* [Minima Moralia](https://genaforvena.github.io/tikziod-thinking/minima.html) - A visualization of the book "Minima Moralia" by Theodor W. Adorno.
* [LP Tractatus](https://genaforvena.github.io/tikziod-thinking/logico.html) - Young Wittgenstein's Tractatus Logico-Philosophicus.
* [Worstward Hoe by Beckett](https://genaforvena.github.io/tikziod-thinking/worstward_hoe.html) - A visualization of the book "Worstward Hoe" by Samuel Beckett.
* [Илья Масодов - Мрак твоих глаз](https://genaforvena.github.io/tikziod-thinking/mrak_rus.html) - Илья Масодов "Мрак твоих глаз" (a masterpiece in russian, yet to be translated into English).
* [Ilya Masodov - The darkness of your eyes](https://genaforvena.github.io/tikziod-thinking/mrak_eng_machine.html) - The masterpiece from above in English, roughly translated with small llms (low quality, yet to be edited).
* [Anti-Oedipus](https://genaforvena.github.io/tikziod-thinking/anti-oedipus.html) to check the visualization of the book "Anti-Oedipus" by Deleuze and Guattari. It is large and may take a while to load.

## Supported File Formats

The tool supports the following file formats:
- Plain text (.txt)
- PDF (.pdf)
- Microsoft Word (.docx)
- Markdown (.md)
- HTML (.html, .htm)

## Basic Usage

The script supports three input methods:

### Local File Input

1. Prepare your input file in any of the supported formats.

2. Run the script with the file input option:

   ```
   python main.py -f input.txt
   ```

   Replace `input.txt` with your file name and appropriate extension.

### Direct Text Input

You can provide texts directly as command-line arguments:

```
python main.py -t "First text here" "Second text here" "Third text here"
```

### Remote File Download

You can now provide a URL to download and process a file:

```
python main.py -u https://example.com/path/to/document.pdf
```

The script will download the file, detect its format, and process it accordingly.

## Viewing and Interacting with the Visualization

After running the script:

1. An interactive HTML file named `index.html` will be generated in the `docs` folder.

2. Open this file in any modern web browser to view the visualization.

3. The visualization offers a rich set of interactive features:

   - **Word Selection**: Click on any word to highlight all its occurrences across the text(s).
   - **Word Controls**: For each selected word, a control panel appears with options to remove, strike out, or navigate between occurrences.
   - **Frequency Slider**: Use the slider to hide less frequent words, dynamically updating the visualization.
   - **Hidden Words Popup**: View a list of words hidden by the frequency slider.
   - **Search Functionality**: Use the search bar to find specific words or phrases in the text.
   - **Shareable State**: Generate a shareable link that captures the current state of your visualization.

4. Additional Interactive Elements:
   - Hover over words to see their frequency across all texts.
   - The font size of words reflects their frequency or importance in the text.

## Advanced Features

- **Multi-format Support**: The tool can process various text formats, automatically detecting and handling the file type.
- **Remote File Processing**: Ability to download and process files from URLs, expanding the range of accessible texts.
- **Natural Language Processing**: Utilizes NLTK for advanced text tokenization and analysis.
- **LaTeX Integration**: Uses Jinja2 for potential LaTeX template rendering, useful for academic or scientific texts.

## Customization

You can customize the visualization by modifying the `interactive.js` file:

- Adjust the color scheme for highlighted words
- Modify the behavior of word selection and navigation
- Add new interactive features or buttons
- Customize the styling of various elements (words, control panels, popups)

## Dependencies

To run this script with all features, you need to have the following Python libraries installed:

- numpy (1.21.0): For numerical computations
- matplotlib (3.4.2): For data visualization
- nltk (3.6.2): For natural language processing
- PyPDF2 (3.0.1): For PDF file support
- python-docx (0.8.11): For DOCX file support
- markdown (3.3.4): For Markdown file support
- beautifulsoup4 (4.9.3): For HTML parsing
- requests (2.25.1): For downloading files from URLs
- jinja2 (3.0.1): For template rendering

Development dependencies:
- pylint (2.8.3): For code linting
- black (21.6b0): For code formatting

You can install the required dependencies using the provided `requirements.txt` file:

```
pip install -r requirements.txt
```

## Troubleshooting

- If you encounter issues with PDF processing, ensure you have the correct version of PyPDF2 installed.
- For NLTK-related functions, you may need to download additional NLTK data. Refer to the NLTK documentation for details.
- When processing files from URLs, ensure you have a stable internet connection and the URL is accessible.
- If a specific file format fails to process, check that you have the necessary dependencies installed and the file is not corrupted.

For any further questions or issues, please refer to the script comments or reach out to the project maintainers.
