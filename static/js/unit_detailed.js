document.addEventListener("DOMContentLoaded", function() {
    // On initial load, display the first section
    const sections = document.querySelectorAll('.section');

    if (sections.length > 0) {
        sections[0].style.display = 'block';
    }

    function showDiv() {
        for (let i = 0; i < sections.length; i++) {
            if (sections[i].style.display === "none") {
                sections[i].style.display = "block";
                if (i === sections.length - 1) {
                    showButton.style.display = "none";
                }
                sections[i].scrollIntoView({ behavior: "smooth" });
                return;
            }
        }
    }

    // Add an event listener for the button
    const showButton = document.getElementById('show-div');
    if (showButton) {
        showButton.addEventListener('click', showDiv);
    }
});
