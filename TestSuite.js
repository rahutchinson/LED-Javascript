/**
 * Created by beaumiller on 2/1/17.
 * AND RYAN HUTCHINSON
 * */

function testPrimitives(){

    testTheseCases(plusCases);
    testTheseCases(minusCases);
    testTheseCases(unaryMinusCases);
    testTheseCases(unaryPlusCases);


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




function div(X, Y) {
    if(Y != 0){
        return X / Y;
    } else {
        return undefined;
    }
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
