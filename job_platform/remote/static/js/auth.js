document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        form.addEventListener("submit", function (event) {
            const inputs = form.querySelectorAll("input");
            let valid = true;

            inputs.forEach(input => {
                if (!input.value.trim()) {
                    input.style.border = "1px solid red";
                    valid = false;
                } else {
                    input.style.border = "1px solid #ddd";
                }
            });

            if (!valid) {
                event.preventDefault(); // Prevent form submission if not valid
            }
        });
    });
});
