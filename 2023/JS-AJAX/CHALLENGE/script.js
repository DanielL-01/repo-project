document.addEventListener("DOMContentLoaded", ()=>{
    const key = "a3a97565924344d3aec160224231602";

    document.getElementById("submit-btn").onclick = function(){
        let location = document.getElementById("city-name").value
        const request = new XMLHttpRequest();
        //console.log(location)
        request.onload = function(){
            const data = JSON.parse(this.responseText);
            document.getElementById("city").innerHTML = `${data.location.name}` 
            //console.log(`${data.location.name}`)
            document.getElementById("temperature").innerHTML = `${data.current.temp_c} C`
            document.getElementById("weather").innerHTML = `${data.current.condition.text}`
            document.getElementById("weather_icon").src = `${data.current.condition.icon}`

            let cloud_scale = `${data.current.cloud}`
            if (cloud_scale => 90){
                document.getElementById("cloud").innerHTML = "Cloudy"
            }

            else if (cloud_scale => 70){
                document.getElementById("cloud").innerHTML = "Mostly cloudy"
            }

            else if (cloud_scale => 30){
                document.getElementById("cloud").innerHTML = "Partly cloudy"
            }

            else if (cloud_scale => 10){
                document.getElementById("cloud").innerHTML = "Mostly clear"
            }

            else {
                document.getElementById("cloud").innerHTML = "Clear"
            }

            let day_scale = `${data.current.is_day}`
            if (day_scale == 0){
                document.getElementById("day").innerHTML = "Night"
            }

            else {
                document.getElementById("day").innerHTML = "Day"
            }


        }
        request.open("GET",`http://api.weatherapi.com/v1/current.json?key=${key}&q=${location}`);
        request.send()
        return false;
    }
})