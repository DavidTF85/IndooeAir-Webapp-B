function generateViewFromObject(dataObj) {

    if (dataObj.was_found === false) {
        alert("That Instrument Do Not exist please create one");
        onBackClick();
      }

      else {

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
    const detailURL = "/api/instruments/"+instrument_id.toString();
    console.log(detailURL);
    xhttp.open("GET", detailURL, true);
    xhttp.send();
}

const instrument_id = {{ instrument_id }};
onPageLoadRunGetInstrumentDetailsFromAPI(instrument_id);


function onBackClick() {
    window.location.href = "{% url 'Instruments_lists_page' %}";
}

function onUpdateClick() {
    window.location.href = "{% url 'Instruments_update_page' instrument_id %}";
}

function SensorDetailsClick() {
    window.location.href = "{% url 'sensor_retrieve_page' sensor_id %}";
}
