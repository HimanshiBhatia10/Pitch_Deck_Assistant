let summaries = [];
let currentIndex = 0;

function handleFileChange() {
    const fileInfo = document.getElementById('file-info');
    const files = this.files;
    if (files.length > 0) {
        fileInfo.textContent = `${files.length} file(s) selected`;
    } else {
        fileInfo.textContent = 'No files selected';
    }
}

function handleFormSubmit(event) {
    event.preventDefault();

    const formData = new FormData(document.getElementById('upload-form'));
    fetch('/upload', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        summaries = data;
        currentIndex = 0;
        displaySummary();
        document.getElementById('prev').disabled = summaries.length <= 1;
        document.getElementById('next').disabled = summaries.length <= 1;
    })
    .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('pdfFile').addEventListener('change', handleFileChange);
    document.getElementById('upload-btn').addEventListener('click', handleFormSubmit);
});


document.getElementById('prev').addEventListener('click', function() {
    if (currentIndex > 0) {
        currentIndex--;
        displaySummary();
    }
});

document.getElementById('next').addEventListener('click', function() {
    if (currentIndex < summaries.length - 1) {
        currentIndex++;
        displaySummary();
    }
});

function displaySummary() {
    if (summaries.length > 0) {
        document.getElementById('Pitch_deck_name').textContent = summaries[currentIndex].filename;
        document.getElementById('summary').textContent = summaries[currentIndex].summary;
    }
}