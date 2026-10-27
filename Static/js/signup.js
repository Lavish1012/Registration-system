document.addEventListener('DOMContentLoaded', () => {
    // Handle all .toggle-password icons
    const toggles = document.querySelectorAll('.toggle-password');

    toggles.forEach(toggle => {
        const selector = toggle.getAttribute('toggle');
        const input = document.querySelector(selector);

        if (!input) return;

        toggle.addEventListener('click', () => {
            const isPasswordVisible = input.type === 'text';
            input.type = isPasswordVisible ? 'password' : 'text';

            // Toggle FontAwesome icon classes
            toggle.classList.toggle('fa-eye');
            toggle.classList.toggle('fa-eye-slash');
        });
    });

    // Password validation on form submit
    const form = document.getElementById('signupForm');
    form.addEventListener('submit', (e) => {
        const password1 = document.getElementById('password1').value;
        const password2 = document.getElementById('password2').value;

        if (password1 !== password2) {
            e.preventDefault();
            alert('Passwords do not match!');
        } else if (password1.length < 6) {
            e.preventDefault();
            alert('Password must be at least 6 characters!');
        }
    });
});
