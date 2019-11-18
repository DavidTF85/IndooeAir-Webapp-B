function CreateNewInstrumentClick(){

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
        document.getElementById("Create").innerHTML = this.responseText;
       }
     }

  xhttp.open('POST',"{%'/instruments/create/api'%}"", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  const newIntruments = document.getElementById('Intruments_Created').value;
  xhttp.send("create_instrument="+newIntruments);
  }
