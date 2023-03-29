

document.addEventListener("DOMContentLoaded", ()=>{
	let canvas = document.getElementById("canvas");
	let ctx = canvas.getContext("2d");
	let covid_img = document.getElementById("covid")
	let mask_img = document.getElementById("mask")
	let car_img = document.getElementById("car")

	let game = false
	let gameover =false

	let velocity = 0;
	let real_time = 0; 
	let score = 0;
	let player = "";

	if (!sessionStorage.getItem("highscore"))sessionStorage.setItem("highscore", 0)
	let highscore = sessionStorage.getItem("highscore")

	const car_Starting = new Audio("resources/car start.mp3")
	const game_over = new Audio("resources/game over.mp3")
	const beep = new Audio("resources/beep.m4a")
 	
 	const blockSize = 20
 	const column = canvas.width/blockSize;
 	const row = canvas.height/blockSize;

 	class Block{
 		constructor(column, row){
 			this.row = row
 			this.column = column;
 			this.size = blockSize;
 		}
		square(color){
			let x = this.column *this.size;
			let y = this.row * this.size;
			ctx.fillStyle = color;
			ctx.fillRect(x, y, this.size, this.size/2);
		}
 	}
 	let scoreText = {
		font : "20px Sans-Serif",
		color : "white",
		align : 'right',
		baseline : "top",

		draw_score : function (){
			const x = 790;
			const y = 10;
			ctx.font = this.font;
			ctx.fillStyle = this.color;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText(`${score}`, x, y);


		},

		draw_highscore : function(){
			const x = 700
			const y = 10
			ctx.fillStyle = this.color;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText(`Hi : ${sessionStorage.getItem("highscore")}`, x, y)

		}
	}
	let dataText = {
		font : "20px Sans-Serif",
		color : "white",
		align : 'left',
		baseline : "top",

		draw_mask : function (){
			let value;
			const x = 10;
			const y = 10;
			ctx.font = this.font;
			ctx.fillStyle = this.color;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			if (car.life == 0) mask = 0
			else mask = car.life -1
			ctx.fillText(`Mask : ${mask}`, x, y);


		},
		draw_player : function (){
			let value;
			const x = 100;
			const y = 10;
			ctx.font = this.font;
			ctx.fillStyle = this.color;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText(`Player : ${player}`, x, y);


		}
	}

	const gameoverText = {
		font : "60px Arial",
		color : "white",
		align : 'center',
		baseline : "middle",

		draw : function (){
			
			const x = canvas.width / 2;
			const y = 30;
			ctx.font = this.font;
			ctx.fillStyle = this.color;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText(`Game over`, x, y);
			


		}
	}
	const  waitingText ={
		font : "30px Arial",
		color : "white",
		align : 'center',
		baseline : "middle",

		draw : function (){

			const x = canvas.width / 2;
			const y = canvas.height/2-10;
			ctx.font = this.font;
			ctx.fillStyle = this.color;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText(`Waiting to start`, x, y);
		}
	}

 	class Car{
 		constructor(column, row , blockSize){
 			this.row = row;
 			this.column = column;
 			this.size = blockSize;
 			this.velocity = 0;
 			this.nextmove = [];
 			this.life = 1
 		}
		draw(){
			let x = (this.column-2)*this.size
			let y = (this.row-1)*this.size
			ctx.drawImage(car_img, x, y )
		}

		moveup(){
			//jalan 2 ke 1
			if (this.row == 14.75){
				let move = setInterval(()=>{
					this.row -= 1/4
					if (this.row <= 11.5){
						clearInterval(move)
						
					}
				
			}, 1)
			}
			//jalan 3 ke 2
			else if (this.row == 18){
				let move = setInterval(()=>{
					this.row -= 1/4
					if (this.row<=14.75){
						clearInterval(move)
					}
				}, 1)
			}
		}
		movedown(){
			// jalan 2 ke 3
			if (this.row == 14.75){
				let move = setInterval(()=>{
					this.row += 1/4
					if (this.row >= 18){
						clearInterval(move)
						
					}
				
			}, 1)
			}
			//jalan 1 ke 2
			else if (this.row == 11.5){
				let move = setInterval(()=>{
					this.row += 1/4
					if (this.row>=14.75){
						clearInterval(move)
					}
				}, 1)
			}
		}
		infected(){
			covid.objects.forEach((object)=>{
				if ((this.column -3) <= object.column && object.column<= (this.column + 2.5) && this.row == object.row){
					this.life -- ;	
					covid.objects.shift()
					if (this.life == 0) {
						gameover = true;
						game_over.play()
						player = "";
						car.life = 1;
						game = false
						document.querySelector("#start_button").disabled = true;
						document.querySelector("#entry-task").disabled = false;
						
					}				
					}
			})

		}
		extralife(){
			masks.objects.forEach((object)=>{
				if ((this.column -2.5) <= object.column && object.column<= (this.column + 2.5) && this.row == object.row){
					this.life++;
					masks.objects.shift()

				}
			})
		}
	}
	class Road{
		constructor(){
			this.width = canvas.width;
			this.height = canvas.height;
			this.size = blockSize;
			this.blocks = [
				new Block(0, row),
				new Block(1, row),
				new Block(2, row),
				new Block(3, row),
				new Block(8, row),
				new Block(9, row),
				new Block(10, row),
				new Block(11, row),
				new Block(16, row),
				new Block(17, row),
				new Block(18, row),
				new Block(19, row),
				new Block(24, row),
				new Block(25, row),
				new Block(26, row),
				new Block(27, row),
				new Block(32, row),
				new Block(33, row),
				new Block(34, row),
				new Block(35, row),
			];

			this.rows = [11.5, 14.75, 18];
		}
		drawCement(){
			ctx.fillStyle = "gray";
			ctx.fillRect(0, this.height-190,this.width,this.height);
		}
		draw_road_Lines(){
			for (let counter = 0; counter < 3; counter++){
				let row = this.rows[counter];
				this.blocks.forEach((block)=>{
					block.row = row;
					block.square("white");
				});
			}
		}

		drawDivider(){
			ctx.fillStyle = "yellow";
			ctx.fillRect(0, canvas.height - 65, canvas.width, 5);
			ctx.fillRect(0, canvas.height - 130, canvas.width, 5);
		}

		draw(){
			road.drawCement();
			road.draw_road_Lines();
			road.drawDivider();
			
		}

		move(velocity){
			
			for (let counter = 0; counter < 3; counter++){
				let newBlocks = [];
				this.blocks.forEach((block)=>{
					if (block.column- 1/4-velocity < 0){
						newBlocks .push(new Block(40,row));
					}
					else {newBlocks.push(new Block(block.column-1/4,row ))};
				})
				this.blocks = newBlocks;
			}
		}
	}

	class Objects{
		constructor(){
			this.objects = [];
			this.column = (canvas.width - blockSize)/20;
			this.size = blockSize;
		}

		location_covid(){
			let rows = [11.5, 14.75, 18];
			let objectsN = Math.floor(Math.random()*3);
			for (let n = 0; n < objectsN; n++){
				let row = Math.floor(Math.random()*rows.length);
				this.objects.push(new Block ((canvas.width - blockSize)/20, rows[row]));
				delete rows[row];
			}
		}

		location_mask(){
			let rows = [11.5, 14.75, 18];
			let objectsN = Math.floor(Math.random()*2);
			for (let n = 0; n < objectsN; n++){
				let row = Math.floor(Math.random()*rows.length);
				if(new Block((canvas.width - blockSize)/20, rows[row]) in covid.objects){
					delete covid.objects[indexOf(Block((canvas.width - blockSize)/20, rows[row]))];
				}
				this.objects.push(new Block ((canvas.width - blockSize)/20, rows[row]));
			}
		}
		draw_covid(){
			this.objects.forEach((object)=>{
				ctx.drawImage(covid_img, (object.column-1)*20, (object.row-1)*20);
			})
		}

		draw_mask(){
			this.objects.forEach((object)=>{
				ctx.drawImage(mask_img, (object.column-1)*20, (object.row-1)*20);
			})
		}
		move(velocity){
			let new_objects = [];
			this.objects.forEach((object)=>{
				if (object.column-1/2-velocity > -(velocity)){
					new_objects.push(new Block(object.column-1/2-velocity, object.row));
				}				
			})
			this.objects = new_objects;
		}
	}
	

	

	addEventListener("keydown", ()=>{
		if (game == true){
			switch (event.code){
				case "KeyW":

					if (car.row > 11.75){
						car.moveup();
						beep.play();
					}
					break;

				case "Space":
					if (car.row > 11.75){

						car.moveup();
						beep.play();
					}
					break;

				case "KeyS":
					if (car.row < 18){
						car.movedown();
						beep.play();
					}
					break;
			}
		}
	})

	let button = document.createElement("button")
	button.innerHTML = "START"
	button.id = "start_button"
	button.onclick = (()=>{
		game = true
		gameover = false
		car_Starting.play();
		document.querySelector("#start_button").disabled = true;
		score = 0;
		covid.objects = [];
	})
	document.querySelector("#btn").appendChild(button);
	document.querySelector("#start_button").disabled = true;
	document.querySelector("#submit-task").disabled=true;
	document.querySelector("#entry-task").onkeyup = () =>{
		if (document.querySelector("#entry-task").value.trim().length > 0)
		document.querySelector("#submit-task").disabled =false;
		else {
			document.querySelector("#submit-task").disabled=true;
		}
	}

	document.querySelector("#form-task").onsubmit = ()=>{
		document.querySelector("#start_button").disabled = false;
		player = document.querySelector("#entry-task").value;
		document.querySelector("#entry-task").disabled = true;
		document.querySelector("#submit-task").disabled =true;
		document.querySelector("#entry-task").value = "";


		return false
	}

	let car = new Car (4, 14.75,blockSize);	
	let road = new Road();
	let covid = new Objects();
	let masks = new Objects();

	
	let mainloop = setInterval(()=>{
		ctx.clearRect(0,0,canvas.width,canvas.height);
		scoreText.draw_score();
		scoreText.draw_highscore();
		dataText.draw_mask();
		console.log(gameover)

		road.draw();
		car.draw();

		if (game == true){
			dataText.draw_player();
			document.querySelector("#entry-task").disabled=true;
			if (real_time % 15 == 0 && real_time > 0){
				covid.location_covid();
			}
			
			if (real_time % 500 == 0 && score > 0){
				masks.location_mask();
				velocity=velocity+1/4;
			}
			road.move(velocity);
			covid.move(velocity);
			covid.draw_covid()
			car.infected();
			masks.move(velocity);
			masks.draw_mask();
			car.extralife();
			real_time++;
			if (real_time % 2 == 0){
				score++;
			}
		}
		else if (game ==false){
			if (score > highscore)sessionStorage.setItem("highscore", score)
			
			mask.objects = []
			waitingText.draw();
			covid.draw_covid()
			real_time = 0 ;
			
			velocity = 0;
			car.life = 1;
			if(gameover)gameoverText.draw()

		}
	

	}, 45);

})
