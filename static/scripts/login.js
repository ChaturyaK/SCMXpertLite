function Signin() {
  // Retrieve email and password values from the input fields
  var email = document.getElementById("Email").value;
  var password = document.getElementById("Password").value;

  // You can perform client-side validation here if needed
  if (email.trim() === "" || password.trim() === "") 
  {
    alert("Email and password are required");
    return;
  }

  // Make an Axios request to your backend for authentication
  axios.post("/login", {
      email: email,
      password: password
  })
  .then(function (response) {
      // Handle the response from the server
      if (response.data.success) {
          // If authentication is successful, you might want to redirect the user or perform other actions
          alert("Login successful!");
          window.location.href = "/dashboard";
      } else {
          // If authentication fails, you can display an error message
          alert("Login failed. Please check your credentials.");
      }
  })
  .catch(function (error) {
      // Handle errors, e.g., network issues or server errors
      console.error("Error during login:", error);
      alert("An error occurred during login. Please try again.");
  });
}
  document.querySelector(".clear-button").addEventListener("click", function () {
  document.getElementById("Email").value = "";
  document.getElementById("Password").value = "";
});