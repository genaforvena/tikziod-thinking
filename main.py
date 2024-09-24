import argparse
import asyncio
from text_processor import read_file, process_texts
from html_generator import generate_html
from web_server import start_server

async def main():
    parser = argparse.ArgumentParser(description="Generate interactive intersecting texts visualization with HTML output.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', type=str, help="Path to file containing texts (one per line)")
    group.add_argument('-t', '--texts', nargs='+', help="List of texts to visualize")
    group.add_argument('-u', '--url', type=str, help="URL of the file to download and process")
    args = parser.parse_args()

    if args.file:
        texts = read_file(args.file)
    elif args.url:
        texts = read_file(args.url)
    else:
        texts = args.texts

    word_sets, word_counts, word_positions = process_texts(texts)
    html_code = generate_html(texts, word_counts, word_positions)

    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_code)
    
    print("Interactive HTML file 'index.html' has been generated in the 'docs' folder.")
    print("Starting web server...")

    await start_server()

if __name__ == "__main__":
    asyncio.run(main())