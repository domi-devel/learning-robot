function submitBtn(button) {
    var currentLocation = window.location.origin;
    var xhttp = new XMLHttpRequest();
    // xhttp.onreadystatechange = function() {
    //   if (this.readyState == 4 && this.status == 200) {
    //     document.getElementById("demo").innerHTML =
    //     this.responseText;
    //   }
    // };
    xhttp.open("POST", currentLocation + "/post", true);
    xhttp.send(button);
  }