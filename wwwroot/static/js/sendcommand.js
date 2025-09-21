document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.card-body button').forEach(button => {
        button.addEventListener('click', async () => {
        if (button.classList.contains('accordion-button')) return;

        const type = button.getAttribute('data-type');
        const key = button.getAttribute('data-cmd-key');
        const value = button.getAttribute('data-cmd-value');
        
        const url = `${type}/${key}/${value}`;

        
        try {
            const response = await fetch(url, { method: 'GET' });
            const text = await response.text();

            //alert 
            const alertDiv = document.createElement('div');
            alertDiv.role = 'alert';

            if (!response.ok) {
                alertDiv.className = 'alert alert-danger mt-2';
            } else {
                alertDiv.className = 'alert alert-success mt-2';
            }
            alertDiv.textContent = text;
            button.parentElement.appendChild(alertDiv);

            setTimeout(() => {
                alertDiv.remove();
            }, 5000);

        } catch (err) {
            console.error(err.message);
        }
        });
    });

    document.querySelectorAll('.card-body').forEach(card => {
        const input = card.querySelector('.cmd-input');
        const button = card.querySelector('.cmd-button');

        if (input && button) {
            button.setAttribute('data-cmd-value', input.value); //default set

            input.addEventListener('input', () => {
                button.setAttribute('data-cmd-value', input.value);
            });
        }
    });
});