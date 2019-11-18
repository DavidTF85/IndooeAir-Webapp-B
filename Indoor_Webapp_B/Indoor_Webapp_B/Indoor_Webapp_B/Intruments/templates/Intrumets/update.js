function generateViewFromObject(dataObj) {
    if (dataObj.was_found === false) {
        alert("Sorry we could not find that instrument!");
        onBackClick();
    } else {
        var idInputElement = document.getElementById("id");
        var nameInputElement = document.getElementById("name");
        idInputElement.value = dataObj.id;
        nameInputElement.value = dataObj.name;
    }
}

function onPageLoadRunGetInstrumentDetailsFromAPI(instrument_id) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const dataString = this.responseText;
            const dataObj = JSON.parse(dataString);
            generateViewFromObject(dataObj);
        }
    }
    const detailURL = "/api/instrument/"+instrument_id.toString();
    console.log(detailURL);
    xhttp.open("GET", detailURL, true);
    xhttp.send();
}

const instrument_id = {{ instrument_id }};
onPageLoadRunGetInstrumentDetailsFromAPI(instrument_id);


function onBackClick() {
    window.location.href = "{% url 'i_retrieve_page' instrument_id %}"
}

function onSubmitClick() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) { // Thisis the callback function
            // Get the string data that the server sent us.
            const resultString = this.responseText;

            // Create an object which converts the string to an object using JSON parsing.
            var resultObject = JSON.parse(resultString);

            // Please note, "was_logged_in" is a key set by the server.
            if (resultObject.was_logged_in === false) {
                alert(resultObject.reason);
            } else {
                window.location.href = "{% url 'i_list_page' %}";
            }
        }
    }

    const instrumentId = {{ instrument_id }};
    xhttp.open("POST", "/api/instrument/"+instrumentId+"/update", true);
    xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
    const name = document.getElementById("name").value;
    xhttp.send("name="+name);
}
