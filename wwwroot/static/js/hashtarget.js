const elements = document.querySelectorAll('[id^="macro_"], [id^="command_"]');

function handleHashChange() {
    const hash = window.location.hash.toLowerCase().replace('#', ''); 

    elements.forEach(el => {
        const idText = el.id.toLowerCase();
        if (hash && hash !== idText) { //darken non matches
            el.style.opacity = '0.5';
        } else {
            el.style.opacity = '1';
            if (hash === idText) { //scroll to match
                el.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }
    });

    if (hash) { //click away to reset all opacities
        const resetOpacity = () => {
            elements.forEach(el => el.style.opacity = '1');
            window.removeEventListener('click', resetOpacity); 
        };
        window.addEventListener('click', resetOpacity);
    }
}

window.addEventListener("hashchange", handleHashChange);
handleHashChange();
