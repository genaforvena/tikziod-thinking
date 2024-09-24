import re
from collections import defaultdict
import PyPDF2

def read_file(file_path):
    if file_path.lower().endswith('.pdf'):
        return read_pdf(file_path)
    else:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]

def read_pdf(file_path):
    texts = []
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text.strip():
                texts.append(text.strip())
    return texts

def process_texts(texts):
    word_sets = [set(re.findall(r'\b\w+\b', text.lower())) for text in texts]
    all_words = set.union(*word_sets)
    word_counts = defaultdict(int)
    word_positions = defaultdict(list)
    for i, text in enumerate(texts):
        for match in re.finditer(r'\b\w+\b', text, re.IGNORECASE):
            word = match.group().lower()
            word_counts[word] += 1
            word_positions[word].append((i, match.start()))
    return word_sets, word_counts, word_positions