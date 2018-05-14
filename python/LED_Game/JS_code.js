function initialState(){
return(toSet([toSet([1,"x"])]));
}
function displayImages(S){
return(union(union(union(gridDisplay(),piecesOnGrid(S)),resetButton()),gameOverImage(S)));
}
function piecesOnGrid(S){
return(union(union(union(union(union(union(union(union(cell1(S),cell2(S)),cell3(S)),cell4(S)),cell5(S)),cell6(S)),cell7(S)),cell8(S)),cell9(S)));
}
function cell1(S){
if(inSet(toSet([1,"x"]),S)){
return(xIcon(150,150));
}
 else if(inSet(toSet([1,"o"]),S)){
return(oIcon(150,150));
}
 else { 
 return([]); 
}
}
function cell2(S){
if(inSet(toSet([2,"x"]),S)){
return(xIcon(250,150));
}
 else if(inSet(toSet([2,"o"]),S)){
return(oIcon(250,150));
}
 else { 
 return([]); 
}
}
function cell3(S){
if(inSet(toSet([3,"x"]),S)){
return(xIcon(350,150));
}
 else if(inSet(toSet([3,"o"]),S)){
return(oIcon(350,150));
}
 else { 
 return([]); 
}
}
function cell4(S){
if(inSet(toSet([4,"x"]),S)){
return(xIcon(150,250));
}
 else if(inSet(toSet([4,"o"]),S)){
return(oIcon(150,250));
}
 else { 
 return([]); 
}
}
function cell5(S){
if(inSet(toSet([5,"x"]),S)){
return(xIcon(250,250));
}
 else if(inSet(toSet([5,"o"]),S)){
return(oIcon(250,250));
}
 else { 
 return([]); 
}
}
function cell6(S){
if(inSet(toSet([6,"x"]),S)){
return(xIcon(350,250));
}
 else if(inSet(toSet([6,"o"]),S)){
return(oIcon(350,250));
}
 else { 
 return([]); 
}
}
function cell7(S){
if(inSet(toSet([7,"x"]),S)){
return(xIcon(150,350));
}
 else if(inSet(toSet([7,"o"]),S)){
return(oIcon(150,350));
}
 else { 
 return([]); 
}
}
function cell8(S){
if(inSet(toSet([8,"x"]),S)){
return(xIcon(250,350));
}
 else if(inSet(toSet([8,"o"]),S)){
return(oIcon(250,350));
}
 else { 
 return([]); 
}
}
function cell9(S){
if(inSet(toSet([9,"x"]),S)){
return(xIcon(350,350));
}
 else if(inSet(toSet([9,"o"]),S)){
return(oIcon(350,350));
}
 else { 
 return([]); 
}
}
function xIcon(centerX,centerY){
return([segment(point((centerX-50),(centerY-50)),point((centerX+50),(centerY+50)),BLUE()),segment(point((centerX-50),(centerY+50)),point((centerX+50),(centerY-50)),BLUE())]);
}
function oIcon(centerX,centerY){
return([disc(point(centerX,centerY),50,RED())]);
}
function gameOverImage(S){
return([text(gameOverText(S),point(600,250),20,BLACK())]);
}
function gridDisplay(){
return([segment(point(200,100),point(200,400),BLACK()),segment(point(300,100),point(300,400),BLACK()),segment(point(100,200),point(400,200),BLACK()),segment(point(100,300),point(400,300),BLACK())]);
}
function resetButton(){
return([segment(point(550,300),point(650,300),BLACK()),segment(point(650,300),point(650,350),BLACK()),segment(point(650,350),point(550,350),BLACK()),segment(point(550,350),point(550,300),BLACK()),text("reset",point(600,325),20,BLACK())]);
}
function centerX(c){
return((150+(100*((c-1)%3))));
}
function centerO(c){
return((350-(100*floor(((c-1)/3)))));
}
function xMin(c){
return((100+(100*((c-1)%3))));
}
function xMax(c){
return((200+(100*((c-1)%3))));
}
function yMin(c){
return((300-(100*floor(((c-1)/3)))));
}
function yMax(c){
return((400-(100*floor(((c-1)/3)))));
}
function clickXInCell(){
return(floor((mouseX()/100)));
}
function clickYInCell(){
return(floor((mouseY()/100)));
}
function cellEmpty(cell,S){
return(!inSet(toSet([cell,"x"]),S)||inSet(toSet([cell,"o"]),S));
}
function cellClicked(){
if((clickXInCell()>0)&&(clickXInCell()<4)&&(clickYInCell()>0)&&(clickYInCell()<4)){
return((clickXInCell()+((clickYInCell()-1)*3)));
}
 else { 
 return("no cell clicked"); 
}
}
function resetClicked(){
return((mouseX()>550)&&(mouseX()<650)&&(mouseY()>300)&&(mouseY()<350));
}
function even(n){
return(((n%2)==0));
}
function playerToMove(S){
if(even(card(S))){
return("x");
}
 else { 
 return("o"); 
}
}
function gameOver(S){
if((card(S)==9)||xWon(S)||oWon(S)){
return(true);
}
 else { 
 return(false); 
}
}
function gameOverText(S){
if(xWon(S)){
return("X Wins!");
}
 else if(oWon(S)){
return("O Wins!");
}
 else if((card(S)>9)){
return("Cat's Game");
}
 else { 
 return(""); 
}
}
function threeInARow(S){
if(xRow(S)){
return("x");
}
 else if(oRow(S)){
return("o");
}
 else { 
 return(""); 
}
}
function moveMade(S){
if((cellClicked()=="no cell clicked")||!cellEmpty(cellClicked(),S)){
return(toSet([]));
}
 else { 
 return(toSet([cellClicked(),playerToMove(S)])); 
}
}
function transition(S){
if(resetClicked()){
return(toSet([]));
}
 else if(gameOver(S)){
return(union(S,toSet(["GAMEOVER"])));
}
 else if(!inSet(moveMade(S),toSet([toSet([])]))){
return(union(S,toSet([moveMade(S)])));
}
 else { 
 return(S); 
}
}
function xWon(S){
return(xTopRow(S)||xMiddleRow(S)||xBottomRow(S)||xLeftCol(S)||xMiddleCol(S)||xRightCol(S)||xDownDiag(S)||xUpDiag(S));
}
function oWon(S){
return(oTopRow(S)||oMiddleRow(S)||oBottomRow(S)||oLeftCol(S)||oMiddleCol(S)||oRightCol(S)||oDownDiag(S)||oUpDiag(S));
}
function xTopRow(S){
return(inSet(toSet([1,"x"]),S)&&inSet(toSet([2,"x"]),S)&&inSet(toSet([3,"x"]),S));
}
function xMiddleRow(S){
return(inSet(toSet([4,"x"]),S)&&inSet(toSet([5,"x"]),S)&&inSet(toSet([6,"x"]),S));
}
function xBottomRow(S){
return(inSet(toSet([7,"x"]),S)&&inSet(toSet([8,"x"]),S)&&inSet(toSet([9,"x"]),S));
}
function xLeftCol(S){
return(inSet(toSet([1,"x"]),S)&&inSet(toSet([4,"x"]),S)&&inSet(toSet([7,"x"]),S));
}
function xMiddleCol(S){
return(inSet(toSet([2,"x"]),S)&&inSet(toSet([5,"x"]),S)&&inSet(toSet([8,"x"]),S));
}
function xRightCol(S){
return(inSet(toSet([3,"x"]),S)&&inSet(toSet([6,"x"]),S)&&inSet(toSet([9,"x"]),S));
}
function xDownDiag(S){
return(inSet(toSet([1,"x"]),S)&&inSet(toSet([5,"x"]),S)&&inSet(toSet([9,"x"]),S));
}
function xUpDiag(S){
return(inSet(toSet([3,"x"]),S)&&inSet(toSet([5,"x"]),S)&&inSet(toSet([7,"x"]),S));
}
function oTopRow(S){
return(inSet(toSet([1,"o"]),S)&&inSet(toSet([2,"o"]),S)&&inSet(toSet([3,"o"]),S));
}
function oMiddleRow(S){
return(inSet(toSet([4,"o"]),S)&&inSet(toSet([5,"o"]),S)&&inSet(toSet([6,"o"]),S));
}
function oBottomRow(S){
return(inSet(toSet([7,"o"]),S)&&inSet(toSet([8,"o"]),S)&&inSet(toSet([9,"o"]),S));
}
function oLeftCol(S){
return(inSet(toSet([1,"o"]),S)&&inSet(toSet([4,"o"]),S)&&inSet(toSet([7,"o"]),S));
}
function oMiddleCol(S){
return(inSet(toSet([2,"o"]),S)&&inSet(toSet([5,"o"]),S)&&inSet(toSet([8,"o"]),S));
}
function oRightCol(S){
return(inSet(toSet([3,"o"]),S)&&inSet(toSet([6,"o"]),S)&&inSet(toSet([9,"o"]),S));
}
function oDownDiag(S){
return(inSet(toSet([1,"o"]),S)&&inSet(toSet([5,"o"]),S)&&inSet(toSet([9,"o"]),S));
}
function oUpDiag(S){
return(inSet(toSet([3,"o"]),S)&&inSet(toSet([5,"o"]),S)&&inSet(toSet([7,"o"]),S));
}
/*

SET OPERATIONS

*/


/**
 * Created by theso_000 on 1/30/2017.
 */
// takes an array and converts it to a sorted set with no duplicates
function toSet(arr){
    if(typeof arr !== "object"){return arr;}
    //sorts the array, then filters out repeat occurrences by position
    return sortSet(arr).filter(function (item, pos, self) {
      return self.indexOf(item) == pos;
    });
}

// returns true if element ∈ setA, false otherwise
function inSet(element, setA){
    //setA = toSet(setA)
    //element = toSet(element)
    for (i in setA){
      if (JSON.stringify(setA[i]) == JSON.stringify(element)){
        return true;
      }
    }
    return setA.indexOf(element) != -1;
}


// returns setA ∪ setB
function union(setA, setB) {
    //concat A and B then remove duplicates
    return setA.concat(setB).filter(function (item, pos, self) {
      return self.indexOf(item) == pos;
    });
}

// returns setA ∩ setB
function intersect(setA, setB){
    return setA.concat(setB).sort().filter(function(item, pos, self) {
        return self.indexOf(item) != pos;
    });
}

// returns setA / setB
function setDiff(setA, setB){
    //removes from A all items in setA ∩ setB
    return setA.filter(function (item, pos, self){
        return !inSet(item,intersect(setA,setB));
    });
}

// returns setA x setB
function cross(setA, setB){

    cross_product = []
    for(i=0; i<setA.length; i++){
        for(j=0; j<setB.length; j++) {
            cross_product = cross_product.concat([[i, j]])
        }
    }
    return cross_product
}

// returns true if setA is a subset of setB
function isSubset(setA, setB){


}

// returns cardinality of setA
function card(setA) {
    return setA.length;
}

function pow(setA){

}

/*
      ARITHMETIC OPERATOINS
      written by Beau Miller 4/2/2018
*/

// returns the floor of a floating point number
function floor(N){
  return Math.floor(N);
}


function isEqual(var1, var2) { // Break the comparison out into a neat little function
  if (typeof var1 !== "object") {
    return var1===var2;
  } else {
    return deepEqual(var1, var2);
  }
}

function deepEqual(var1, var2) {
   for (i in var1) {
      if(typeof var2[i] === "undefined") { // Quick check, does the property even exist?
         return false;
      }
      if (!isEqual(var1[i], var2[i])) {
         return false;
      }
   }
   return true;
}

function seteq(obj1, obj2) {
   return deepEqual(obj1, obj2) && deepEqual(obj2, obj1); // Two-way checking
}


function sortSet(arr) { // Recursivly sort a nested array
  for(var i = 0; i <arr.length; i++){
    if (typeof arr[i] !== "object") {
      arr[i] = arr[i];
    } else {
      arr[i] = toSet(arr[i]);
    }
  }
  return arr.sort();
}

