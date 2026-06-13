document.getElementById("contactForm")
.addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = {
    name: e.target.name.value,
    email: e.target.email.value,
    message: e.target.message.value
  };

  const res = await fetch("https://my-portfolio-1-arom.onrender.com/contact", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(formData)
  });

  if (res.ok) {
    alert("Message sent successfully!");
  } else {
    alert("Error sending message");
  }
});