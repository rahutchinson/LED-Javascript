/*******************************************************************


                        EASELJS
  _________________________________
  Date of last edit: May 7th, 2018
  Authors:  Beau Miller
            Ryan Hutchinson
  Texas Tech University
  _________________________________

EaselJS is composed of LED functions and the PLAYGAME function and associated helpers

  LED FUNCTIONS
  provided by the user:

    initialState()
    displayImages()
    transition()
    sounds()

    and all helpers



********************************************************************/


/*
                        LED functions
-----*/



/*-----
                        END LED
*/


var COLORS = {'RED': '#FF0000',
              'GREEN': '#00FF00',
              'BLUE' : '#0000FF',
              'BLACK': '#000000',
              'WHITE': '#FFFFFF'};

function BLACK(){
  return('BLACK');
}
function BLUE(){
  return('BLUE');
}
function WHITE(){
  return('WHITE');
}
function GREEN(){
  return('GREEN');
}
function RED(){
  return('RED');
}

function point(x, y){
  return([x, y]);
}

function segment(point1, point2, color){
  return(['seg', point1, point2, color])
}

function text(textstring, point1, size, color){
  return(['txt', textstring, point1, size, color])
}

function circle(center, radius, color){
  return(['circ', center, radius, color])
}

function disc(center, radius, color){
  return(['disc', center, radius, color])
}

function drawSegment(type, startPoint, endPoint, color){
  var canvas = document.getElementById('easel');
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(startPoint[0],startPoint[1]);
    ctx.lineTo(endPoint[0],endPoint[1]);
    ctx.strokeStyle = COLORS[color];
    ctx.stroke();
   }
}

function drawCircle(type, center, radius, color){
  var canvas = document.getElementById('easel');
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d');
    ctx.beginPath();
    ctx.arc(center[0], center[1], radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = color;
    ctx.fill();
  }
}

function drawFilledTriangle(type, p, q, r, color){
  var canvas = document.getElementById('easel');
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(p[0], p[1]);
    ctx.lineTo(q[0], q[1]);
    ctx.lineTo(r[0], r[1]);
    ctx.fillStyle = color;
    ctx.fill();
  }
}

function drawText(type, text, center, size, color){
  var canvas = document.getElementById('easel');
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d');
    ctx.font = size.toString() + "px Arial";
    ctx.fillStyle = color;
    ctx.textAlign = "center";
    ctx.fillText(text,center[0],center[1]);
  }
}

function drawDisc(type, center, radius, color){
  var canvas = document.getElementById('easel');
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d');
    ctx.beginPath();
    ctx.arc(center[0], center[1], radius, 0, 2 * Math.PI, false);
    ctx.strokeStyle = color;
    ctx.stroke();
  }
}


/*
..................................
     PLAYGAME Helper functions
..................................
*/
function keyPress(e) {
  var key = e.keyCode ? e.keyCode : e.which;
  console.log(key);
  K.push(key);
  console.log(K);
}

function storeGuess(event) {
    var x = event.offsetX;
    var y = event.offsetY;
    addClick(x,y);
    console.log("x coords: " + x + ", y coords: " + y);
}

function addClick(x,y){
  c.x = x;
  c.y = y;
}

function mouseX(){
  return(I.c.x)
}

function mouseY(){
  return(I.c.y)
}

function cleanCanvas(){
  var canvas = document.getElementById('easel');
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }
}

function cleanInput() {

  c.x = -1;
  c.y= -1;
  K = [];

}

function render(images){
  for(var i=0; i<images.length; i++){
    var image = images[i];
    switch(image[0]){
      case "seg":
        drawSegment(image[0],image[1],image[2],image[3]);
        break;
      case "circ":
        drawCircle(image[0],image[1],image[2],image[3]);
        break;
      case "fTri":
        drawFilledTriangle(image[0],image[1],image[2],image[3], image[4]);
        break;
      case "txt":
        drawText(image[0],image[1],image[2],image[3], image[4]);
        break;
      case "disc":
        drawDisc(image[0],image[1],image[2],image[3]);
        break;
      default:
        //console.log("Image error");
    }
  }
  return(image);
}

function play(sound){
  var audio = document.getElementById(sound);
  audio.load();
  audio.play();
}

function playSounds(sounds){
  for(var i=0; i<sounds.length; i++){
    var sound = sounds[i];
    play(sound);
  }
}

/*
......................................................................
                            PLAYGAME
......................................................................

  PLAY GAME ALGORITHM

  State variables
     S: State,
     C: click,
     K: A set of single-character strings,
     I: Input
     lastFrameTime: time-in-seconds


    S := initialState
    while True:
      set lastFrameTime to the current time
      set screen display to images(S)
      If the left mouse button has clicked downward since the last frame, and the mouse is positioned in the game window,
      store the mouse position in C otherwise set C equal to `none.
      Set K equal to the set of pressed keys
      I := (C,K)
      play all of the sounds in (sounds(I,S))
      S := transition(I,S)
      Pause until currentTime>=lastFrameTime + 0.03

.............................................
         STATE VARIABLES INITIALIZATION
.............................................
*/

var S = initialState(); //State
var c = { // Mouse input, x and y coordinates
  x: -1,
  y: -1
};
var K = []; // keyboard input: a set of single character strings
var I = { // combined mouse and keyboardInput
  c: c,
  k: []
};
var soundSet = [];

var game = setInterval(playGame, 100);

/*
......................................................................
                            PLAYGAME
......................................................................
*/

function playGame(){

  if(S == 'Stop'){
    clearInterval(game);
  }
  cleanCanvas();
// Set screen display to images(S)
  render(displayImages(S));

// I := (C,K)
  I.c = c;
  I.k = K;
// S := transition(I,S)
  S = transition(S);
  ///soundSet = sounds(S);

   cleanInput();
}

