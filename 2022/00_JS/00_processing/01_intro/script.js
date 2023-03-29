function setup(){
	createCanvas(400,400)
	console.log("oke")
	noStroke();
	frameRate(24)
}

function draw() {
	background(121)
	fill(255, 0, 0,160);
	
	ellipse(200, 200, 200, 200)
	fill(0,255,0,160)
	ellipse(100,200,200,200)
	fill(0,0,255,160)
	ellipse(300,200,200,200)

}