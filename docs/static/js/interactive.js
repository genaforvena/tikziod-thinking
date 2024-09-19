let selectedWords = new Map();
let colorIndex = 0;
const colors = ['highlight-0', 'highlight-1', 'highlight-2', 'highlight-3', 'highlight-4'];
let wordElements = new Map();

function toggleWordSelection(word, element) {
    if (selectedWords.has(word)) {
        unhighlightWord(word);
        selectedWords.delete(word);
        removeWordActions(word);
    } else {
        highlightWord(word);
        selectedWords.set(word, {
            color: colors[colorIndex],
            elements: wordElements.get(word) || [],
            currentIndex: 0
        });
        colorIndex = (colorIndex + 1) % colors.length;
        showWordActions(word, element);
    }
    updateCounters();
}

function highlightWord(word) {
    const elements = wordElements.get(word) || [];
    const color = colors[colorIndex];
    elements.forEach(el => el.classList.add(color));
}

function unhighlightWord(word) {
    const info = selectedWords.get(word);
    if (info) {
        info.elements.forEach(el => {
            el.classList.remove(info.color);
            hideCounter(el.parentNode);
        });
    }
}

function showCounter(element) {
    const counter = element.querySelector('.counter');
    if (counter) counter.style.display = 'block';
}

function hideCounter(element) {
    const counter = element.querySelector('.counter');
    if (counter) counter.style.display = 'none';
}

function updateWordVisibility(threshold) {
    const sortedWords = Object.entries(wordCounts).sort((a, b) => a[1] - b[1]);
    const totalWords = sortedWords.length;
    const visibleCount = Math.floor(totalWords * (1 - threshold));
    
    // Use requestAnimationFrame for smoother updates
    requestAnimationFrame(() => {
        sortedWords.forEach((entry, index) => {
            const [word, count] = entry;
            const elements = wordElements.get(word) || [];
            const shouldHide = index >= visibleCount;
            elements.forEach(el => el.classList.toggle('hidden', shouldHide));
        });
    });
}

document.addEventListener('DOMContentLoaded', function() {
    // Cache all word elements
    document.querySelectorAll('.common-word').forEach(word => {
        const wordText = word.dataset.word;
        if (!wordElements.has(wordText)) {
            wordElements.set(wordText, []);
        }
        wordElements.get(wordText).push(word);
        
        word.addEventListener('click', function(e) {
            e.preventDefault();
            toggleWordSelection(this.dataset.word, this);
        });
    });

    const slider = document.getElementById('frequency-slider');
    let debounceTimer;
    slider.addEventListener('input', function() {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
            const threshold = this.value / 100;
            updateWordVisibility(threshold);
        }, 50); // Debounce for 50ms
    });

    document.addEventListener('click', function(e) {
        if (!e.target.closest('.common-word') && !e.target.closest('.word-actions')) {
            selectedWords.forEach((info, word) => {
                removeWordActions(word);
            });
        }
    });
});

