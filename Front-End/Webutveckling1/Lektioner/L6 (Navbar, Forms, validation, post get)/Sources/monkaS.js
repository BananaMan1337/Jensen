

function validateForm() {
    var name = document.forms["name"].value;
    var email = document.forms["email"].value;
    var password = document.forms["password"].value;
  
    if (name == "") {
      alert("Name must be filled out");
      return false;
    }
  
    if (email == "") {
      alert("Email must be filled out");
      return false;
    }
  
    if (password == "") {
      alert("Password must be filled out");
      return false;
    }
  
    if (password.length < 8) {
      alert("Password must be at least 8 characters long");
      return false;
    }
  
    return true;
  }


  function validateForm() {
    var name = document.getElementById("name").value.trim();
    var email = document.getElementById("email").value.trim();
    var message = document.getElementById("message").value.trim();

    if (name === "" || email === "" || message === "") {
        document.getElementById("error-message").innerHTML = "Alla fält måste fyllas i.";
        return false;
    }

    if (!validateEmail(email)) {
        document.getElementById("error-message").innerHTML = "E-postadressen är ogiltig.";
        return false;
    }

    return true;
}

function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}
