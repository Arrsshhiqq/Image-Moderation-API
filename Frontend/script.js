let token = '';

function setToken() {
    token = document.getElementById('token').value;
    alert('Token set!');
}

async function uploadImage() {
    const fileInput = document.getElementById('image');
    const resultDiv = document.getElementById('result');
    const file = fileInput.files[0];
    if (!file || !token) {
        resultDiv.textContent = 'Please set a token and select an image.';
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('http://localhost:7000/moderate/', {
            method: 'POST',
            headers: { 'Authorization': `Bearer ${token}` },
            body: formData
        });
        const result = await response.json();
        resultDiv.textContent = JSON.stringify(result, null, 2);
    } catch (error) {
        resultDiv.textContent = `Error: ${error.message}`;
    }
}