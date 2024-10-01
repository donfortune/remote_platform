// Example job search filter functionality
document.querySelector('.search-btn').addEventListener('click', function() {
    const searchInput = document.querySelector('.search-bar input').value;
    
    // Log search query (you can later replace this with your Django template rendering logic)
    console.log("Searching for: " + searchInput);
    
    // Future implementation: Fetch jobs based on input using Django's backend or API
    // You can use fetch or AJAX calls here to get the search results
});
