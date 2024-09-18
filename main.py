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
    args = parser.parse_args()

    if args.file:
        texts = read_file(args.file)
    else:
        texts = args.texts

    word_sets, word_counts, word_positions = process_texts(texts)
    html_code = generate_html(texts, word_counts, word_positions)

    with open('intersecting_texts.html', 'w') as f:
        f.write(html_code)
    
    print("Interactive HTML file 'intersecting_texts.html' has been generated.")
    print("Starting web server...")

    await start_server()

if __name__ == "__main__":
    asyncio.run(main())
