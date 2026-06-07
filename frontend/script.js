document.getElementById("contactForm")
.addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = {
    name: e.target.name.value,
    email: e.target.email.value,
    message: e.target.message.value
  };

  const res = await fetch("http://127.0.0.1:8000/contact", {
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