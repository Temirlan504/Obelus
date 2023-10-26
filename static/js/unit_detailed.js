document.addEventListener("DOMContentLoaded", function() {
    // Adjust image layout based on the width of the image
    function adjustImageLayout(imgElement) {
        const maxWidthInline = 250; // Change this value based on your preference
        if (imgElement.width > maxWidthInline) {
            imgElement.parentElement.classList.add('image-block');
        } else {
            imgElement.parentElement.classList.add('image-inline');
        }
    }

    const sections = document.querySelectorAll('.section');
    const progressBar = document.getElementById('myBar');
    const showButton = document.getElementById('show-div');
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

    function showDiv() {
        if (currentSection < sections.length) {
            sections[currentSection].style.display = "block";
            sections[currentSection].scrollIntoView({ behavior: "smooth" });
            currentSection++;
            updateProgressBar();
        }
    
        if (currentSection === sections.length) {
            showButton.style.display = "none";
        }
    }
    

    // Add an event listener for the button
    if (showButton) {
        showButton.addEventListener('click', showDiv);
    }

    let images = document.querySelectorAll('.section-image');
    images.forEach(img => {
        img.onload = function() {
            adjustImageLayout(img);
        };
    });
});
