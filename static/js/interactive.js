let currentWord = null;
let currentContext = null;
let sortedWords = [];

function supportsNativeSmoothScroll() {
    return 'scrollBehavior' in document.documentElement.style;
}

function smoothScroll(target) {
    const targetElement = document.querySelector(target);
    if (targetElement) {
        window.scrollTo({
            top: targetElement.offsetTop,
            behavior: 'smooth'
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

function highlightWords(word) {
    const elements = document.querySelectorAll(`[data-word="${word}"]`);
    elements.forEach(el => el.classList.add('highlight'));
}

function unhighlightWords(word) {
    const elements = document.querySelectorAll(`[data-word="${word}"]`);
    elements.forEach(el => el.classList.remove('highlight'));
}

function hideWord(word) {
    const elements = document.querySelectorAll(`[data-word="${word}"]`);
    elements.forEach(el => {
        el.classList.add('hidden');
        hideCounter(el.parentNode);
    });
}

function showWord(word) {
    const elements = document.querySelectorAll(`[data-word="${word}"]`);
    elements.forEach(el => {
        el.classList.remove('hidden');
    });
}

function strikeoutWord(word) {
    const elements = document.querySelectorAll(`[data-word="${word}"]`);
    elements.forEach(el => {
        el.classList.add('strikeout');
    });
}

function showNextEntry(element, word) {
    const positions = wordPositions[word];
    const currentTextIndex = parseInt(element.id.split('-')[2]);
    const currentPosition = parseInt(element.id.split('-')[3]);
    
    let nextEntry = positions.find(pos => 
        pos[0] > currentTextIndex || (pos[0] === currentTextIndex && pos[1] > currentPosition)
    );
    if (!nextEntry) {
        nextEntry = positions[0];
    }

    let nextEntryHtml = `<div class="next-entry">Next: Text ${nextEntry[0] + 1}</div>`;
    element.parentNode.insertAdjacentHTML('beforeend', nextEntryHtml);
}

function hideNextEntry(element) {
    const nextEntry = element.parentNode.querySelector('.next-entry');
    if (nextEntry) {
        nextEntry.remove();
    }
}

function showWordActions(word, context, x, y) {
    const wordActions = document.getElementById('word-actions');
    wordActions.style.display = 'block';
    wordActions.style.left = `${x}px`;
    wordActions.style.top = `${y + 20}px`;  // 20px below the word
    currentWord = word;
    currentContext = context;
}

async function getContinuation(word, context) {
    const response = await fetch('/get_continuation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ word, context }),
    });
    const data = await response.json();
    return data.continuation;
}

function showContinuationResult(continuation) {
    const resultDiv = document.getElementById('continuation-result');
    resultDiv.textContent = continuation;
    resultDiv.style.display = 'block';
}

function updateWordVisibility(threshold) {
    const sortedWords = Object.entries(wordCounts).sort((a, b) => a[1] - b[1]);
    const totalWords = sortedWords.length;
    const visibleCount = Math.floor(totalWords * (1 - threshold));
    
    sortedWords.forEach((entry, index) => {
        const [word, count] = entry;
        const elements = document.querySelectorAll(`[data-word="${word}"]`);
        if (index < visibleCount) {
            elements.forEach(el => el.classList.remove('hidden'));
        } else {
            elements.forEach(el => el.classList.add('hidden'));
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const wordActions = document.createElement('div');
    wordActions.id = 'word-actions';
    const hideButton = document.createElement('button');
    hideButton.id = 'hide-button';
    hideButton.textContent = 'Hide';
    const strikeoutButton = document.createElement('button');
    strikeoutButton.id = 'strikeout-button';
    strikeoutButton.textContent = 'Strike-out';
    const continueButton = document.createElement('button');
    continueButton.id = 'continue-button';
    continueButton.textContent = 'Continue';
    wordActions.appendChild(hideButton);
    wordActions.appendChild(strikeoutButton);
    wordActions.appendChild(continueButton);
    document.body.appendChild(wordActions);

    const continuationResult = document.createElement('div');
    continuationResult.id = 'continuation-result';
    document.body.appendChild(continuationResult);

    const sliderContainer = document.createElement('div');
    sliderContainer.id = 'frequency-slider-container';
    const slider = document.createElement('input');
    slider.type = 'range';
    slider.id = 'frequency-slider';
    slider.min = '0';
    slider.max = '100';
    slider.value = '0';
    sliderContainer.appendChild(slider);
    document.body.appendChild(sliderContainer);

    sortedWords = Object.keys(wordCounts).sort((a, b) => wordCounts[b] - wordCounts[a]);

    slider.addEventListener('input', function() {
        const threshold = this.value / 100;
        updateWordVisibility(threshold);
    });

    const commonWords = document.querySelectorAll('.common-word');
    commonWords.forEach(word => {
        word.addEventListener('mouseover', function(e) {
            showCounter(this.parentNode);
            highlightWords(this.dataset.word);
            showNextEntry(this, this.dataset.word);
            const context = this.closest('p').textContent;
            showWordActions(this.dataset.word, context, e.pageX, e.pageY);
        });
        word.addEventListener('mouseout', function() {
            hideCounter(this.parentNode);
            unhighlightWords(this.dataset.word);
            hideNextEntry(this);
        });
        word.addEventListener('click', function(e) {
            if (!supportsNativeSmoothScroll()) {
                e.preventDefault();
                smoothScroll(this.getAttribute('href'));
            }
        });
    });

    hideButton.addEventListener('click', function() {
        if (currentWord) {
            hideWord(currentWord);
            wordActions.style.display = 'none';
        }
    });

    strikeoutButton.addEventListener('click', function() {
        if (currentWord) {
            strikeoutWord(currentWord);
            wordActions.style.display = 'none';
        }
    });

    continueButton.addEventListener('click', async function() {
        if (currentWord && currentContext) {
            const continuation = await getContinuation(currentWord, currentContext);
            showContinuationResult(continuation);
            wordActions.style.display = 'none';
        }
    });

    document.addEventListener('click', function(e) {
        if (!e.target.closest('.common-word') && !e.target.closest('#word-actions')) {
            wordActions.style.display = 'none';
        }
    });
});
