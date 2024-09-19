let selectedWords = new Map();
let colorIndex = 0;
const colors = ['highlight-0', 'highlight-1', 'highlight-2', 'highlight-3', 'highlight-4'];
let sortedWords = [];
let wordElements = new Map();

function toggleWordSelection(word, element) {
    if (selectedWords.has(word)) {
        unhighlightWord(word);
        selectedWords.delete(word);
        removeWordControls(word);
    } else {
        highlightWord(word);
        selectedWords.set(word, {
            color: colors[colorIndex],
            elements: wordElements.get(word) || [],
            currentIndex: 0
        });
        colorIndex = (colorIndex + 1) % colors.length;
        showWordControls(word);
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

function showWordControls(word) {
    const controlsContainer = document.getElementById('word-controls');
    const wordControls = document.createElement('div');
    wordControls.id = `controls-${word}`;
    wordControls.innerHTML = `
        <span>${word}: </span>
        <button class="remove-button">Remove</button>
        <button class="strikeout-button">Strikeout</button>
        <button class="prev-button">Previous</button>
        <button class="next-button">Next</button>
    `;
    controlsContainer.appendChild(wordControls);

    wordControls.querySelector('.remove-button').addEventListener('click', () => removeWord(word));
    wordControls.querySelector('.strikeout-button').addEventListener('click', () => strikeoutWord(word));
    wordControls.querySelector('.prev-button').addEventListener('click', () => goToPreviousOccurrence(word));
    wordControls.querySelector('.next-button').addEventListener('click', () => goToNextOccurrence(word));
}

function removeWordControls(word) {
    const controls = document.getElementById(`controls-${word}`);
    if (controls) controls.remove();
}

function removeWord(word) {
    const elements = wordElements.get(word) || [];
    elements.forEach(el => el.classList.add('hidden'));
    unhighlightWord(word);
    selectedWords.delete(word);
    removeWordControls(word);
}

function strikeoutWord(word) {
    const elements = wordElements.get(word) || [];
    elements.forEach(el => el.classList.add('strikeout'));
}

function goToNextOccurrence(word) {
    const info = selectedWords.get(word);
    if (info) {
        info.currentIndex = (info.currentIndex + 1) % info.elements.length;
        scrollToCurrentOccurrence(word);
    }
}

function goToPreviousOccurrence(word) {
    const info = selectedWords.get(word);
    if (info) {
        info.currentIndex = (info.currentIndex - 1 + info.elements.length) % info.elements.length;
        scrollToCurrentOccurrence(word);
    }
}

function scrollToCurrentOccurrence(word) {
    const info = selectedWords.get(word);
    if (info) {
        const currentElement = info.elements[info.currentIndex];
        currentElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

function updateWordVisibility(threshold) {
    const hiddenWords = [];
    let totalHidden = 0;

    sortedWords.forEach((entry, index) => {
        const [word, count] = entry;
        const elements = wordElements.get(word) || [];
        if (index < threshold) {
            elements.forEach(el => {
                el.classList.add('hidden');
            });
            hiddenWords.push(`${word} (${count})`);
            totalHidden += count;
        } else if (elements[0] && elements[0].classList.contains('hidden')) {
            elements.forEach(el => {
                el.classList.remove('hidden');
            });
        }
    });

    updateHiddenWordsPopup(hiddenWords);
    updateSliderValue(totalHidden);
}

function updateHiddenWordsPopup(hiddenWords) {
    const popup = document.getElementById('hidden-words-popup');
    if (hiddenWords.length > 0) {
        popup.innerHTML = `<h3>Hidden Words:</h3><p>${hiddenWords.join(', ')}</p>`;
        popup.style.display = 'block';
    } else {
        popup.style.display = 'none';
    }
}

function updateSliderValue(totalHidden) {
    const sliderValue = document.getElementById('slider-value');
    sliderValue.textContent = `Hidden: ${totalHidden}`;
}

function updateHiddenWordsPopup(hiddenWords) {
    const popup = document.getElementById('hidden-words-popup');
    const content = document.getElementById('hidden-words-content');
    if (hiddenWords.length > 0) {
        content.innerHTML = `<h3>Hidden Words:</h3><p>${hiddenWords.join(', ')}</p>`;
        popup.style.display = 'block';
    } else {
        popup.style.display = 'none';
    }
}

function closeHiddenWordsPopup() {
    const popup = document.getElementById('hidden-words-popup');
    popup.style.display = 'none';
}

let searchHighlight = null;

function addSearchBar() {
    const searchContainer = document.createElement('div');
    searchContainer.id = 'search-container';
    searchContainer.innerHTML = `
        <input type="text" id="search-input" placeholder="Search for words...">
        <span id="search-count"></span>
    `;
    document.body.insertBefore(searchContainer, document.body.firstChild);

    const searchInput = document.getElementById('search-input');
    searchInput.addEventListener('input', handleSearch);
}

function handleSearch() {
    const searchTerm = this.value.toLowerCase();
    const searchCount = document.getElementById('search-count');
    
    if (searchTerm.length === 0) {
        if (searchHighlight) {
            searchHighlight.classList.remove('search-highlight');
            searchHighlight = null;
        }
        searchCount.textContent = '';
        return;
    }

    const matches = [];
    wordElements.forEach((elements, word) => {
        if (word.toLowerCase().includes(searchTerm)) {
            matches.push(...elements);
        }
    });

    if (matches.length > 0) {
        searchCount.textContent = `${matches.length} match${matches.length > 1 ? 'es' : ''}`;
        highlightNextMatch(matches);
    } else {
        searchCount.textContent = 'No matches';
        if (searchHighlight) {
            searchHighlight.classList.remove('search-highlight');
            searchHighlight = null;
        }
    }
}

function highlightNextMatch(matches) {
    if (searchHighlight) {
        searchHighlight.classList.remove('search-highlight');
    }

    let nextMatch;
    if (!searchHighlight) {
        nextMatch = matches[0];
    } else {
        const currentIndex = matches.indexOf(searchHighlight);
        nextMatch = matches[(currentIndex + 1) % matches.length];
    }

    searchHighlight = nextMatch;
    searchHighlight.classList.add('search-highlight');
    searchHighlight.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

document.addEventListener('DOMContentLoaded', function() {
    const commonWords = document.querySelectorAll('.common-word');
    commonWords.forEach(word => {
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

    document.addEventListener('click', function(e) {
        if (!e.target.closest('.common-word') && !e.target.closest('#word-controls')) {
            selectedWords.forEach((info, word) => {
                removeWordControls(word);
            });
        }
    });
    
    const closePopupButton = document.getElementById('close-popup');
    closePopupButton.addEventListener('click', closeHiddenWordsPopup);

    const slider = document.getElementById('frequency-slider');
    sortedWords = Object.entries(wordCounts).sort((a, b) => b[1] - a[1]);
    slider.max = sortedWords.length;

    slider.addEventListener('input', function() {
        const threshold = parseInt(this.value);
        updateWordVisibility(threshold);
    });

    document.addEventListener('click', function(e) {
        if (!e.target.closest('.common-word') && !e.target.closest('#word-controls')) {
            selectedWords.forEach((info, word) => {
                removeWordControls(word);
            });
        }
    });

    addSearchBar();

    // Add this new CSS for search highlight
    const style = document.createElement('style');
    style.textContent = `
        .search-highlight {
            background-color: yellow;
            font-weight: bold;
        }
        #search-container {
            position: fixed;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1000;
            background-color: white;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
        #search-input {
            padding: 5px;
            width: 200px;
        }
        #search-count {
            margin-left: 10px;
            font-size: 0.9em;
            color: #666;
        }
    `;
    document.head.appendChild(style);
});
