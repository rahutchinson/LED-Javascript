/**
 * Created by beaumiller on 2/1/17.
 * AND RYAN HUTCHINSON
 * */

function testPrimitives(){

    testTheseCases(plusCases);
    testTheseCases(minusCases);
    testTheseCases(unaryMinusCases);
    testTheseCases(unaryPlusCases);
    testTheseCases(timesCases);
    testTheseCases(divideCases);


}

function testTheseCases(Cases){
    // Addition test
    for(var i = 0; i < Cases.length; i++){
        console.log(Cases[i][0]+" -> "+Cases[i][1]);
        test(Cases[i][0],Cases[i][1]);
        console.log("\n");
    }
}

// Code before I realized that this function was general

/*
function testPlus(plusCases){
    // Addition test
    for(var i = 0; i < plusCases.length; i++){
        console.log(plusCases[i][0]+" -> "+plusCases[i][1]);
        test(plusCases[i][0],plusCases[i][1]);
        console.log("\n");
    }
}

function testMinus(minusCases){
    // Addition test
    for(var i = 0; i < minusCases.length; i++){
        console.log(minusCases[i][0]+" -> "+minusCases[i][1]);
        test(minusCases[i][0],minusCases[i][1]);
        console.log("\n");
    }
}

*/

var plusCases = [["2+3",5],["plus(1,undefined)",undefined],
                ["plus(1,div(2,0))",undefined],
                ["plus(div(2,0),1)",undefined],
                ["plus(0,0)",0],
                ["plus(uminus(2),uminus(4))" ,-6],
                ["plus(2,uminus(4))" ,-2],
                ["plus(0.4,0.3)",0.7],
                ["plus(0.7,uminus(0.3))",0.4],
                ["plus(1,uminus(1))",0],
                ["plus(0.00000001,0.00000002)",0.00000003],
                ["plus(1000000000,2000000000)",3000000000]];

var minusCases = [["minus(4,div(0,0))",undefined],
                ["minus(1,div(2,0))",undefined],
                ["minus(div(2,0),1)",undefined],
                ["minus(div(0,0),div(0,0))",undefined],
                ["minus(0,0)",0],
                ["minus(uminus(2),uminus(4))",2],
                ["minus(2,uminus(4))",6],
                ["minus(0.4,0.3)",0.1],
                ["minus(0.7,uminus(0.3))",1],
                ["minus(1,uminus(1))",2],
                ["minus(1,1)",0],
                ["minus(0.00000001,0.00000002)", -0.00000001],
                ["minus(1000000000,2000000000)" ,-1000000000]];

var unaryPlusCases = [["uplus(0)",0],
                ["div(uplus(3),0)",undefined],
                ["uplus(0)",0],
                ["uplus(-12)",12],
                ["uplus(uminus(10))",10],
                ["uplus(div(2,0))",undefined],
                ["uplus(1000000000)",1000000000],
                ["uplus(-0.000000001)",0.000000001]];

var unaryMinusCases = [["plus(uminus(1),4)",3],
                ["div(2,uminus(0))",undefined],
                ["uminus(0)",0],
                ["uminus(12)" ,-12],
                ["uminus(10)",-10],
                ["uminus(div(2,0))",undefined],
                ["uminus(1000000000)",-1000000000],
                ["uminus(0.000000001)",-0.000000001]];


var timesCases = [["plus(1,times(2,uminus(3))) ",-5],
                ["times(plus(1,2),uminus(3)) ",-9],
                ["times(div(1,0),0)",undefined],
                ["times(2,uminus(3))",-6],
                ["times(0,0)",0],
                ["times(1,0)",0],
                ["times(0,4)",0],
                ["times(0,div(2,0))",undefined],
                ["times(div(2,0),24)",undefined],
                ["times(div(2,0),div(2,0))",undefined],
                ["times(1000000,1000000)",1000000000000],
                ["times(0.000001,0.000002)",0.000000000002],
                ["times(uminus(4),uminus(6))",24]];

var divideCases = [["div(div(2,2),2)",0.5],
                ["div(6,times(2,3))",9],
                ["div(5,0)",undefined],
                ["div(0,0)",undefined],
                ["div(0,2)",0],
                ["div(2,div(0/0))",undefined],
                ["div(div(0,0),2)",undefined],
                ["div(1,1)",1],
                ["div(1,100)",0.01],
                ["div(0.01,100)",0.0001],
                ["div(0.04,0.02)",2],
                ["div(100,0.05)",2000],
                ["div(uminus(10),2)" ,-5],
                ["div(2,uminus(10))" ,-0.2],
                ["div(uminus(2),uminus(4))", 0.5]];


var floorCases = [["floor(5.2)",5],
                ["floor(-2.4)" ,-3],
                ["floor(0.(9..))",1],
                ["floor(0/0)",undefined],
                ["floor(16)",16],
                ["floor(uminus(16))",-16],
                ["floor(0)",0]];

var ceilCases = [["ceil(20.4)",21],
                ["ceil(uminus(0.9))",0],
                ["ceil(0^0)",undefined],
                ["ceil(25)",25],
                ["ceil(uminus(25))",25],
                ["ceil(uminus(24.5))",24],
                ["ceil(0)",0]];

var absoluteCases = [["abs(-2.4)",2.4],
                ["abs(floor(div(1,uminus(3))))",0],
                ["abs(0)",0],
                ["abs(1)",1],
                ["abs(uminus(1))",1],
                ["abs(uminus(1000000000000))",1000000000000],
                ["abs(uminus(div(2,0)))",undefined]];

var modCases = [["mod(5,3)",2],
                ["mod(5,1)",0],
                ["mod(5,0)",undefined],
                ["mod(5,uminus(1))",undefined],
                ["mod(5,1.5)",undefined],
                ["mod(uminus(5),2)" ,-1],
                ["mod(0,0)",undefined],
                ["mod(0,1)",0],
                ["mod(5,5)",1],
                ["mod(5,10)",0],
                ["mod(uminus(5),uminus(2))",undefined],
                ["mod(5,div(1,0))",undefined]];


function div(X, Y) {
    if(Y != 0){
        return X / Y;
    } else {
        return undefined;
    }
}

function times(X,Y) {
    return X * Y;
}

function plus(X,Y){
    //console.log(typeof X + "TEST");
    if((X == undefined )|| (Y == undefined)){
        console.log("HELO");
        return undefined;
    } else {
        return X + Y;
    }
}
function minus(X,Y){
    //console.log(typeof X + "TEST");
    if((X == undefined )|| (Y == undefined)){
        console.log("HELO");
        return undefined;
    } else {
        return X - Y;
    }
}

function uminus(X){
    if(X != undefined){
        return -X;
    } else {
        return undefined
    }
}

function uplus(X){
    if(X != undefined){
        return Math.abs(X);
    } else {
        return undefined
    }
}


function test(caseString,result){

    if (eval(caseString) == result){
        console.log("GOOD");
        return
    } else {
        console.log("Error: test case \n" + caseString + "\nreturned \n" + eval(caseString)+"\ninstead of \n"+ result+"\n");
        return
    }
}

testPrimitives();
