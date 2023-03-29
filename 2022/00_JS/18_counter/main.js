let counter = 0; 
let count = () =>  {
	counter++;
	//document.querySelector("#counter").innerHTML = counter;
	$("#counter").text(counter);
	if (counter % 10 == 0) {
		//alert("Counternya sudah "+counter);
		alert(`COunter nya sudah ${counter}`);
	} 
}