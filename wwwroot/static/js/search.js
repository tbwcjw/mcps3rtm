const searchInputs = document.querySelectorAll('.search');

function handleSearch(searchInput) {
    const query = searchInput.value.toLowerCase().replace(/\s+/g, '');

        const elements = document.querySelectorAll('[id^="macro_"], [id^="command_"]');

        let closestMatch = null;
        let closestIndex = Infinity;

        elements.forEach((el, index) => {
            const idText = el.id.toLowerCase(); //#command_* or #macro_*
            if (idText.includes(query)) { //#x_* has query
                el.style.opacity = '1'; 
                el.style.pointerEvents = 'auto';
                if (closestMatch === null) { //set closest match
                    closestMatch = el;
                    closestIndex = index;
                }
            } else {
                el.style.opacity = '0.5';
                el.style.pointerEvents = 'none';
            }
        });

        if (closestMatch) { //scroll to closest
            closestMatch.scrollIntoView({ behavior: 'smooth', block: 'center' });

            const resetOpacity = () => { //click away to reset all opacities
                elements.forEach(el => el.style.opacity = '1');
                elements.forEach(el => el.style.pointerEvents = 'auto');
                window.removeEventListener('click', resetOpacity); 
            };
            window.addEventListener('click', resetOpacity);
        }
}

searchInputs.forEach(searchInput => {
    searchInput.addEventListener('input', () => {
        handleSearch(searchInput);
    });
    searchInput.addEventListener('keydown', (event) => {
        if(event.key === "Enter") handleSearch(searchInput);
    });
});
