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

function showWordActions(word, element) {
    const wordActions = document.createElement('div');
    wordActions.className = 'word-actions';
    wordActions.id = `actions-${word}`;
    const removeButton = createButton('Remove', 'remove-button', () => removeWord(word));
    const strikeoutButton = createButton('Strikeout', 'strikeout-button', () => strikeoutWord(word));
    const nextButton = createButton('Next', 'next-button', () => goToNextOccurrence(word));
    wordActions.appendChild(removeButton);
    wordActions.appendChild(strikeoutButton);
    wordActions.appendChild(nextButton);
    document.body.appendChild(wordActions);
    const rect = element.getBoundingClientRect();
    wordActions.style.left = `${rect.left}px`;
    wordActions.style.top = `${rect.bottom + window.scrollY + 5}px`;
    wordActions.style.display = 'block';
}
function createButton(text, className, onClick) {
    const button = document.createElement('button');
    button.textContent = text;
    button.className = className;
    button.addEventListener('click', onClick);
    return button;
}
function removeWordActions(word) {
    const actions = document.getElementById(`actions-${word}`);
    if (actions) actions.remove();
}
function removeWord(word) {
    const elements = document.querySelectorAll(`[data-word="${word}"]`);
    elements.forEach(el => el.classList.add('hidden'));
    unhighlightWord(word);
    selectedWords.delete(word);
    removeWordActions(word);
}
function strikeoutWord(word) {
    const elements = document.querySelectorAll(`[data-word="${word}"]`);
    elements.forEach(el => el.classList.add('strikeout'));
}
function goToNextOccurrence(word) {
    const info = selectedWords.get(word);
    if (info) {
        info.currentIndex = (info.currentIndex + 1) % info.elements.length;
        const nextElement = info.elements[info.currentIndex];
        nextElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

function updateCounters() {
    selectedWords.forEach((info, word) => {
        info.elements.forEach((el, index) => {
            const counter = el.parentNode.querySelector('.counter');
            if (counter) {
                counter.innerHTML = `<span class="current">${index + 1}</span>/<span class="total">${info.elements.length}</span>`;
                showCounter(el.parentNode);
            }
        });
    });
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

