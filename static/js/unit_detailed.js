document.addEventListener("DOMContentLoaded", function() {
    // Progress bar
    const sections = document.querySelectorAll('.section');
    const progressBar = document.getElementById('myBar');
    let currentSection = 0;

    if (sections.length > 0) {
        sections[0].style.display = 'block';
        currentSection = 1;
        updateProgressBar();
    }

    function updateProgressBar() {
        const progressPercentage = (currentSection / sections.length) * 100;
        progressBar.style.width = progressPercentage + "%";
    }

    // Function to show the next div after "Continue" is clicked
    const continueButton = document.getElementById('show-div');
    function showDiv() {
        if (currentSection < sections.length) {
            sections[currentSection].style.display = "block";
            sections[currentSection].scrollIntoView({ behavior: "smooth" });
            currentSection++;
            updateProgressBar();
        }
    
        if (currentSection === sections.length) {
            continueButton.style.display = "none";
        }
    }

    // Add an event listener for the button "continue"
    if (continueButton) {
        continueButton.addEventListener('click', showDiv);
    }
});
