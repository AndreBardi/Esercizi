document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let isValid = true;
    const inputs = document.querySelectorAll('input, select');
    inputs.forEach(input => {
        if (!input.value) {
            isValid = false;
        }
    });

    if (isValid) {
        showResponsePage();
    } else {
        alert('Per favore, compila tutti i campi.');
    }
});

function showResponsePage() {
    const container = document.querySelector('.container');
    container.innerHTML = `
        <h1>Grazie per la Registrazione!</h1>
        <p><strong>Nome:</strong> ${document.getElementById('nome').value}</p>
        <p><strong>Cognome:</strong> ${document.getElementById('cognome').value}</p>
        <p><strong>Data di Nascita:</strong> ${document.getElementById('dataNascita').value}</p>
        <p><strong>Indirizzo:</strong> ${document.getElementById('indirizzo').value}</p>
        <p><strong>Città:</strong> ${document.getElementById('città').value}</p>
        <p><strong>Codice Fiscale:</strong> ${document.getElementById('codiceFiscale').value}</p>
        <p><strong>Email:</strong> ${document.getElementById('mail').value}</p>
        <button onclick="goToLoginPage()">Torna al Login</button>
    `;
}

function goToLoginPage() {
    window.location.href = 'formRegistrazione.html';
}
