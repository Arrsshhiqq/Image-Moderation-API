async function moderate() {
    const token = document.getElementById('token').value;
    const fileInput = document.getElementById('image');
    const errorDiv = document.getElementById('error');
    const resultDiv = document.getElementById('result');

    if (!token || !fileInput.files[0]) {
        errorDiv.textContent = 'Please provide a token and image';
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    try {
        const response = await fetch('http://localhost:7000/moderate/', {
            method: 'POST',
            headers: { 'Authorization': `Bearer ${token}` },
            body: formData
        });
        const data = await response.json();
        if (response.ok) {
            errorDiv.textContent = '';
            resultDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        } else {
            errorDiv.textContent = data.detail || 'Error moderating image';
        }
    } catch (error) {
        errorDiv.textContent = 'Network error: ' + error.message;
    }
}