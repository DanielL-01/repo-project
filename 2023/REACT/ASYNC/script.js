
// const request = new XMLHttpRequest();
// request.onload = function(){
//     const response = JSON.parse(this.responseText);
//     console.log(response)
// }

// request.open("get", "https://www.omdbapi.com/?apikey=ec53110b&s=harry%20potter")
// request.send();

// fetch("https://www.omdbapi.com/?apikey=ec53110b&s=harry%20potter")
//     .then(response => response.json())
//     .then(response => console.log(response));

// $.ajax({
//     url : "https://www.omdbapi.com/?apikey=ec53110b&s=harry%20potter",
//     success : response => console.log(response)
// })

const fulfilled = false;
// const promise = new Promise((resolve, reject)=>{
//     if (fulfilled)
//         resolve("Done"); // return fulfilled
//     else 
//         reject("undone"); // return not fulfilled
// });

// promise
//     .then(response => console.log("Okay ..."+response))
//     .catch(response=>console.log("Not okay ..."+response))

fetch("https://www.omdbapi.com/?apikey=ec53110b&s=harry%20potter")
    .then(response => response.json())
    .then(response => console.log(response))
    .catch(error => console.log("Sorry, Failed Fetching"+error))