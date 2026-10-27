// Prevent Enter key from submitting the form and move focus to the next input
document.addEventListener("DOMContentLoaded", function () {
    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password");

    usernameInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault(); // Prevent form submission
            passwordInput.focus(); // Move focus to the password input field
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    // Get the password input and toggle image
    const passwordInput = document.getElementById('password');
    const togglePassword = document.getElementById('toggle-password');

    // Read the image URLs from data attributes
    const eyeCloseImage = togglePassword.getAttribute('data-eye-close');
    const eyeOpenImage = togglePassword.getAttribute('data-eye-open');

    // Add the event listener for toggling password visibility
    togglePassword.addEventListener('click', () => {
        const isPasswordVisible = passwordInput.type === 'text';
        passwordInput.type = isPasswordVisible ? 'password' : 'text';

        // Toggle the icon image (eye-open vs. eye-close)
        togglePassword.src = isPasswordVisible ? eyeCloseImage : eyeOpenImage;
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const toggles = document.querySelectorAll('.toggle-password');

    toggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const input = document.querySelector(toggle.getAttribute('toggle'));
            if (input.type === 'password') {
                input.type = 'text';
                toggle.classList.remove('fa-eye');
                toggle.classList.add('fa-eye-slash');
            } else {
                input.type = 'password';
                toggle.classList.remove('fa-eye-slash');
                toggle.classList.add('fa-eye');
            }
        });
    });
});
