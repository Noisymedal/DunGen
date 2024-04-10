document.getElementById('generate-button').addEventListener('click', function(event) {
    event.preventDefault();

    const size = document.getElementById('size').value;
    const difficulty = document.getElementById('difficulty').value;
    const theme = document.getElementById('theme').value;

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ size, difficulty, theme }),
    })
    .then(response => response.json())
    .then(data => {
        // Update the image
        const dungeonImage = document.getElementById('dungeon-image');
        dungeonImage.src = "/dungeon.png?" + new Date().getTime();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});