/**
 * Created by ryan on 2/6/2017.
 */
var solution = "answer";
var operandOne;
var operandTwo;

function update() {
    operandOne = getFirst();
    operandTwo = getSecond();
}

function addition() {
    update();
    solution = operandOne + operandTwo;
    displayy(solution);
}
function subtraction() {
    update();
    solution = operandOne - operandTwo;
    displayy(solution);
}

function unary_plus() {
    update();
    solution = +operandOne;
    displayy(solution);
}

function unary_minus() {
    update();
    solution = -operandOne;
    displayy(solution);
}

function product() {
    update();
    solution = operandOne * operandTwo;
    displayy(solution);
}

function quotient() {
    update();
    if (operandTwo == 0) {
        solution = undefined;
    }
    else {
        solution = operandOne / operandTwo;
    }

    displayy(solution);
}


function floor() {
    update();
    displayy(floor(operandOne));
}

function ceiling() {
    update();
    displayy(ceiling(operandTwo));
}

function absolute_value() {
    update();
    displayy(Math.abs(operandOne));
}




function getFirst() {
    x = document.getElementById("First_Value");
    if (x != undefined){
        return Number(x.value);
    }
    else{
        return undefined
    }

}

function getSecond() {
    y = document.getElementById("Second_Value");
    if (x != undefined){
        return Number(y.value);
    }
    else{
        return undefined;
    }
}
function displayy() {
    var label = document.getElementById("display");
    label.value = solution;
}
