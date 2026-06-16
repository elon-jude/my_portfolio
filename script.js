document
.getElementById("contactForm")
.addEventListener("submit", async function(e) {

    e.preventDefault();

    const formData = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value
    };

    try {
        const response = await fetch(
            "https://my-portfolio-1-arom.onrender.com/contact",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            }
        );

        const result = await response.json();

        alert("Message sent successfully!");
        document.getElementById("contactForm").reset();
    } catch(error) {
        console.error(error);
        alert("Failed to send message.");
    }
});
