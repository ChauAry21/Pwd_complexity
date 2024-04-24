function checkPasswordComplexity() {
    var password = document.getElementById("passwordInput").value;
    console.log("Password:", password); // Log the password before sending the request

    fetch('http://localhost:5000/checkPasswordComplexity', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({password: password})
    })
    .then(response => response.json())
    .then(data => {
        console.log("Response:", data); // Log the response received from the backend
        var resultText = data.complexity ? "Strong" : "Weak"; // Determine the result text based on the response
        document.getElementById("result").innerText = "Password complexity: " + resultText; // Update the HTML content with the result
        if (data.is_weak) {
            document.getElementById("alternativePassword").innerText = "Alternative Strong Password: " + data.alternative_password;
        }
    })
    .catch(error => console.error('Error:', error));
}
