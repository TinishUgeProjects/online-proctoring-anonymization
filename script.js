document.addEventListener('DOMContentLoaded', function() {
    const loginLink = document.querySelector('nav ul li:nth-child(1) a');
    const registerLink = document.querySelector('nav ul li:nth-child(2) a');
    const loginForm = document.getElementById('login');
    const registerForm = document.getElementById('register');
    const candidateLoginButton = document.querySelector('#login .card button:nth-of-type(2)'); // Select the second button in the login section
    const candidateLoginForm = document.getElementById('candidate-login-form');

    loginLink.addEventListener('click', function(event) {
        event.preventDefault();
        loginForm.classList.remove('hidden');
        registerForm.classList.add('hidden');
        candidateLoginForm.classList.add('hidden'); // Hide candidate login form when login link is clicked
    });

    registerLink.addEventListener('click', function(event) {
        event.preventDefault();
        registerForm.classList.remove('hidden');
        loginForm.classList.add('hidden');
        candidateLoginForm.classList.add('hidden'); // Hide candidate login form when register link is clicked
    });

    candidateLoginButton.addEventListener('click', function(event) {
        event.preventDefault();
        candidateLoginForm.classList.toggle('hidden'); // Toggle visibility of candidate login form
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const registerButton = document.querySelector('#registerForm button[type="submit"]');

    registerButton.addEventListener('click', function(event) {
        event.preventDefault();

        const form = document.getElementById('registerForm');
        const formData = new FormData(form);

        fetch('/sign_up', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (response.ok) {
                console.log('Registration successful');
                window.location.href = '/dashboard.html'; // Redirect to dashboard.html on successful registration
            } else {
                console.error('Registration failed');
                // Add any additional error handling
            }
        })
        .catch(error => {
            console.error('Error registering:', error);
            // Add any additional error handling
        });
    });
});
