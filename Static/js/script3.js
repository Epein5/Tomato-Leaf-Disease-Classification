document.getElementById('imageInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const imagePreview = document.getElementById('imagePreview');
            const imageLabel = document.getElementById('imageLabel');
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block';
            imageLabel.style.display = 'none';
        }
        reader.readAsDataURL(file);
    }
});

document.getElementById('uploadForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const imageInput = document.getElementById('imageInput');
    const file = imageInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('image', file);

        const response = await fetch('/classify_image', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const result = await response.json();
            document.getElementById('predictedClass').textContent = result.predicted_class;
            document.getElementById('description').textContent = result.disease_info.Description;
            document.getElementById('preventionMeasures').textContent = result.disease_info.Prevention_measures;
            document.querySelector('.result').style.display = 'block';
        } else {
            alert('Error classifying image');
        }
    }
});

document.getElementById('sendChat').addEventListener('click', async function() {
    const chatInput = document.getElementById('chatInput');
    const message = chatInput.value;

    if (message) {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });

        if (response.ok) {
            const result = await response.json();
            updateChat(message, 'user');
            updateChat(result.reply, 'system');
            chatInput.value = '';
        } else {
            alert('Error sending message');
        }
    }
});

function updateChat(message, sender) {
    const chatMessages = document.getElementById('chatMessages');
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message', sender);
    const bubbleElement = document.createElement('div');
    bubbleElement.classList.add('chat-bubble', sender);
    bubbleElement.innerHTML = message;
    messageElement.appendChild(bubbleElement);
    chatMessages.appendChild(messageElement);
    renderMathInElement(bubbleElement);  // Use KaTeX to render LaTeX
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
