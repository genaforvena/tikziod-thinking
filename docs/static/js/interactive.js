let selectedWords = new Map();
let colorIndex = 0;
const colors = ['highlight-0', 'highlight-1', 'highlight-2', 'highlight-3', 'highlight-4'];
let sortedWords = [];
let wordElements = new Map();
let removedWords = new Set();
let struckOutWords = new Set();

function initializeWordInteractions() {
    const allWords = document.querySelectorAll('.word, .common-word');
    allWords.forEach(wordElement => {
        const word = wordElement.textContent.toLowerCase();
        if (!wordElements.has(word)) {
            wordElements.set(word, []);
        }
        wordElements.get(word).push(wordElement);

        wordElement.addEventListener('click', function(e) {
            e.preventDefault();
            const clickedIndex = wordElements.get(word).indexOf(this);
            toggleWordSelection(word, clickedIndex);
        });
    });
}

function toggleWordSelection(word, clickedIndex) {
    if (selectedWords.has(word)) {
        unhighlightWord(word);
        selectedWords.delete(word);
        removeWordControls(word);
    } else {
        highlightWord(word);
        selectedWords.set(word, {
            color: colors[colorIndex],
            elements: wordElements.get(word) || [],
            currentIndex: clickedIndex
        });
        colorIndex = (colorIndex + 1) % colors.length;
        showWordControls(word);
    }
    updateCounters();
    updateControlsPanel();
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

function showWordControls(word) {
    updateControlsPanel();
}

function updateControlsPanel() {
    const controlsContainer = document.getElementById('word-controls');
    controlsContainer.innerHTML = '';
    selectedWords.forEach((info, word) => {
        const wordControl = document.createElement('div');
        wordControl.className = 'word-control';
        wordControl.innerHTML = `
            <span>${word} (${info.elements.length}): </span>
            <button class="remove-button">Remove</button>
            <button class="strikeout-button">Strikeout</button>
            <button class="goto-button">Go to</button>
            ${info.elements.length > 1 ? `
                <button class="prev-button">Previous</button>
                <button class="next-button">Next</button>
            ` : ''}
            <span class="occurrence-counter">${info.currentIndex + 1}/${info.elements.length}</span>
            <button class="close-button">×</button>
        `;
        controlsContainer.appendChild(wordControl);

        wordControl.querySelector('.remove-button').addEventListener('click', () => removeWord(word));
        wordControl.querySelector('.strikeout-button').addEventListener('click', () => strikeoutWord(word));
        wordControl.querySelector('.goto-button').addEventListener('click', () => goToCurrentOccurrence(word));
        if (info.elements.length > 1) {
            wordControl.querySelector('.prev-button').addEventListener('click', () => goToPreviousOccurrence(word));
            wordControl.querySelector('.next-button').addEventListener('click', () => goToNextOccurrence(word));
        }
        wordControl.querySelector('.close-button').addEventListener('click', () => {
            unhighlightWord(word);
            selectedWords.delete(word);
            updateControlsPanel();
        });
    });
}

function removeWord(word) {
    const elements = wordElements.get(word) || [];
    elements.forEach(el => { 
        let textNode = document.createTextNode('_'.repeat(el.textContent.length));
        el.parentNode.insertBefore(textNode, el);
        el.classList.add('removed-word');
        el.dataset.originalText = el.textContent;
        el.textContent = ' '.repeat(el.textContent.length);
    });
    unhighlightWord(word);
    selectedWords.delete(word);
    removedWords.add(word);
    updateControlsPanel();
}

function strikeoutWord(word) {
    const elements = wordElements.get(word) || [];
    struckOutWords.add(word);
    elements.forEach(el => el.classList.add('strikeout'));
}

function goToCurrentOccurrence(word) {
    const info = selectedWords.get(word);
    if (info && info.elements.length > 0) {
        const element = info.elements[info.currentIndex];
        element.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

function goToNextOccurrence(word) {
    const info = selectedWords.get(word);
    if (info && info.elements.length > 1) {
        info.currentIndex = (info.currentIndex + 1) % info.elements.length;
        goToCurrentOccurrence(word);
        updateControlsPanel();
    }
}

function goToPreviousOccurrence(word) {
    const info = selectedWords.get(word);
    if (info && info.elements.length > 1) {
        info.currentIndex = (info.currentIndex - 1 + info.elements.length) % info.elements.length;
        goToCurrentOccurrence(word);
        updateControlsPanel();
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

function showCounter(element) {
    const counter = element.querySelector('.counter');
    if (counter) counter.style.display = 'block';
}

function hideCounter(element) {
    const counter = element.querySelector('.counter');
    if (counter) counter.style.display = 'none';
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
    const content = document.getElementById('hidden-words-content');
    if (hiddenWords.length > 0) {
        content.innerHTML = `<h3>Hidden Words:</h3><p>${hiddenWords.join(', ')}</p>`;
        popup.style.display = 'block';
    } else {
        popup.style.display = 'none';
    }
}

function updateSliderValue(totalHidden) {
    const sliderValue = document.getElementById('slider-value');
    sliderValue.textContent = `Hidden: ${totalHidden}`;
}

function closeHiddenWordsPopup() {
    const popup = document.getElementById('hidden-words-popup');
    popup.style.display = 'none';
}

function encodeState() {
    const state = {
        slider: document.getElementById('frequency-slider').value,
        highlighted: Array.from(selectedWords.keys()),
        cursors: Object.fromEntries(
            Array.from(selectedWords.entries()).map(([word, info]) => [word, info.currentIndex])
        ),
        removed: Array.from(removedWords),
        struckOut: Array.from(struckOutWords),
    };

    return btoa(JSON.stringify(state));
}

function decodeState(encodedState) {
    return JSON.parse(atob(encodedState));
}

function applyState(state) {
    removedWords = new Set(state.removed);
    struckOutWords = new Set(state.struckOut);
    const slider = document.getElementById('frequency-slider');
    slider.value = state.slider;
    updateWordVisibility(state.slider);
   
    state.removed.forEach(word => {
        removeWord(word);
    });

    state.struckOut.forEach(word => {
        strikeoutWord(word);
    });

    state.highlighted.forEach(word => {
        const elements = wordElements.get(word) || [];
        elements.forEach(el => el.classList.add('highlight-0'));
        selectedWords.set(word, {
            color: 'highlight-0',
            elements: elements,
            currentIndex: state.cursors[word] || 0
        });
        scrollToCurrentOccurrence(word);
        showWordControls(word);
    });
}

function generateShareableLink() {
    const baseUrl = window.location.href.split('?')[0];
    const state = encodeState();
    return `${baseUrl}?state=${state}`;
}

function addShareButton() {
    const shareButton = document.createElement('button');
    shareButton.id = 'share-button';
    shareButton.textContent = 'Share Current State';
    shareButton.addEventListener('click', () => {
        const link = generateShareableLink();
        navigator.clipboard.writeText(link).then(() => {
            alert('Shareable link copied to clipboard!');
        });
    });
    document.body.appendChild(shareButton);
}

document.addEventListener('DOMContentLoaded', function() {
    initializeWordInteractions();

    document.addEventListener('click', function(e) {
        if (!e.target.closest('.word, .common-word') && !e.target.closest('#word-controls')) {
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

    addShareButton();

    // Check if there's a state in the URL and apply it
    const urlParams = new URLSearchParams(window.location.search);
    const encodedState = urlParams.get('state');
    if (encodedState) {
        const state = decodeState(encodedState);
        applyState(state);
    }

    const style = document.createElement('style');
    style.textContent += `
        #search-container {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background-color: #f8f9fa;
            padding: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            z-index: 1001;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        #search-input {
            padding: 5px 10px;
            width: 300px;
            border: 1px solid #ced4da;
            border-radius: 4px;
            font-size: 16px;
        }
        #search-count {
            margin-left: 10px;
            font-size: 14px;
            color: #6c757d;
        }
        #share-button {
            position: fixed;
            top: 33vh;
            right: 20px;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            z-index: 1000;
            transform: rotate(-90deg);
            transform-origin: right center;
        }
        #share-button:hover {
            background-color: #0056b3;
        }
        #word-controls {
            position: fixed;
            top: 10px;
            right: 10px;
            background-color: white;
            border: 1px solid #ccc;
            padding: 10px;
            max-height: 80vh;
            overflow-y: auto;
            z-index: 1000;
        }
        .word-control {
            margin-bottom: 10px;
        }
        .close-button {
            cursor: pointer;
            float: right;
            font-weight: bold;
        }
        .word, .common-word {
            cursor: pointer;
        }
        .word:hover, .common-word:hover {
            background-color: #f0f0f0;
        }
        .removed-word {
            text-decoration: underline;
            text-decoration-style: solid;
            text-decoration-color: #007bff;
            text-decoration-thickness: 2px;
        }
    `;
    document.head.appendChild(style);
});