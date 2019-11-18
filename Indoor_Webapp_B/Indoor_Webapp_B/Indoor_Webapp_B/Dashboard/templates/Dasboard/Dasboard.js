function onDashboardClick() {
  const temp = document.getElementById("Temperature").value;
  console.log(temp);
  const co2 = document.getElementById("CO2").value;
  console.log(co2);
  const tvoc = document.getElementById("TVCO").value;
  console.log(tvoc);
  const humid = document.getElementById("Humidity").value;
  console.log(humid);
  const press = document.getElementById("Pressure").value;
  console.log(press);

  var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) { // This is the callback function
         // Get the string data that the server sent us.
         if (this.readyState == 4 && this.status == 200) {
           data = JSON.parse(this.responseText);
           document.getElementById('Average_Temperature').innerHTML =data.temp_avg;
           document.getElementById('Average_Pressure').innerHTML = data.press_avg;
           document.getElementById('Average_CO2').innerHTML = data.co2_avg;
           document.getElementById('Average_TVCO').innerHTML = data.tvoc_avg;
           document.getElementById('Average_Humidity').innerHTML = data.humid_avg;
         }
       }
     }
        xhttp.open('POST', "{% url 'Dashboard_API_View' %}", true);
        xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
        xhttp.send("&Average_Temperature="+temp+"&Average_Pressure="+press+"&Average_CO2="+co2+"&Average_TVCO="+tvoc+"&Average_Humidity="+humid);

}

        xhttp.open('POST', "{% url 'Instruments_List_API_View' %}", true);
        xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
        xhttp.send(Instruments_List_API_View);

}
        xhttp.open('POST', "{% url ' Instruments_statisticsList_API_View' %}", true);
        xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
        xhttp.send( Instruments_statisticsList_API_View);

}
