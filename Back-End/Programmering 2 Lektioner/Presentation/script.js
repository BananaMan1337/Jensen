var largeImage = document.getElementById('large-image');

var thumbnails = document.getElementsByClassName('thumbnail');
for (var i = 0; i < thumbnails.length; i++) {
    thumbnails[i].onclick = function() {
        largeImage.src = this.src;
        largeImage.alt = this.alt;
    }
}


document.getElementById('book-now').onclick = function() {
    var selectedDate = document.getElementById('booking-date').value;
    if (selectedDate) {
      alert('Du har bokat datumet: ' + selectedDate);
    } else {
      alert('Vänligen välj ett datum för bokning.');
    }
  };


  function validateForm() {

    var name = document.getElementById("name");
    var email = document.getElementById("email");
    var message = document.getElementById("message");

    var errorMessage = "";

    if (name.value === "") {
    errorMessage += "Vänligen fyll i ditt namn.\n";
    }

    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.value)) {
    
    errorMessage += "Vänligen ange en giltig e-ßpostadress.\n";
    
    }

    if (message.value === "") {
    errorMessage += "Vänligen ange ett meddelande.";
    }

    if (errorMessage !== "") {
    alert(errorMessage);
    return false; 
    }

    return true;
    }