document.addEventListener("DOMContentLoaded", () => {
    
    document.querySelector("button").addEventListener("click", () => {
        
        const request = new XMLHttpRequest();
        request.onload = function(){
            const data = JSON.parse(this.responseText);
            keys = Object.keys(data.rates)
            keys.forEach(key => {
                console.log(`${key} -s ${data.rates[key]}`);
                const tr = document.createElement("tr");
                const currency = document.createElement("td");
                const rates = document.createElement("td");
                currency.innerHTML = key;
                rates.innerHTML = data.rates[key];
                tr.append(currency);
                tr.append(rates);
                document.querySelector(".result").append(tr);


            })
        }
        request.open("GET", "http://127.0.0.1:5000/api/currency/latest");
        request.send();




    })

})