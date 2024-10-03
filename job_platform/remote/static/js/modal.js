// modal.js

// Get modal elements
const modal = document.getElementById("job-modal");
const btn = document.getElementById("add-job-btn");
const span = document.getElementsByClassName("close")[0];

// Open the modal when the "Add Job" button is clicked
btn.onclick = function() {
    console.log("Add Job button clicked");
    modal.style.display = "flex"; // Change to 'flex' to maintain centering
}

// Close the modal when the "x" button is clicked
span.onclick = function() {
    modal.style.display = "none";
}

// Close the modal when clicking outside of the modal content
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}

// Close the modal when pressing the "Esc" key
window.addEventListener("keydown", function(event) {
    if (event.key === "Escape") {
        modal.style.display = "none";
    }
});
