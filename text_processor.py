import re
from collections import defaultdict
import PyPDF2
import requests
from nltk.tokenize import word_tokenize
import io
import docx
import markdown
from bs4 import BeautifulSoup

def download_file(url):
    response = requests.get(url)
    response.raise_for_status()
    return io.BytesIO(response.content)

def read_file(file_path):
    if file_path.startswith('http://') or file_path.startswith('https://'):
        file_content = download_file(file_path)
        file_extension = file_path.split('.')[-1].lower()
    else:
        file_content = file_path
        file_extension = file_path.split('.')[-1].lower()

    if file_extension == 'pdf':
        return read_pdf(file_content)
    elif file_extension == 'docx':
        return read_docx(file_content)
    elif file_extension == 'md':
        return read_markdown(file_content)
    elif file_extension == 'html' or file_extension == 'htm':
        return read_html(file_content)
    else:
        with open(file_content, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]

def read_pdf(file_content):
    texts = []
    pdf_reader = PyPDF2.PdfReader(file_content)
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text.strip():
            texts.append(text.strip())
    return texts

def read_docx(file_content):
    doc = docx.Document(file_content)
    return [para.text for para in doc.paragraphs if para.text.strip()]

def read_markdown(file_content):
    with open(file_content, 'r', encoding='utf-8') as file:
        md_content = file.read()
    html_content = markdown.markdown(md_content)
    return [text for text in BeautifulSoup(html_content, 'html.parser').stripped_strings]

def read_html(file_content):
    with open(file_content, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return [text for text in BeautifulSoup(html_content, 'html.parser').stripped_strings]

def process_texts(texts):
    word_sets = [set(word_tokenize(text.lower())) for text in texts]
    all_words = set.union(*word_sets)
    word_counts = defaultdict(int)
    word_positions = defaultdict(list)
    for i, text in enumerate(texts):
        for match in re.finditer(r'\b\w+\b', text, re.IGNORECASE):
            word = match.group().lower()
            word_counts[word] += 1
            word_positions[word].append((i, match.start()))
    return word_sets, word_counts, word_positions