/**
 * Created by theso_000 on 1/30/2017.
 */
function testOne() {
    window.alert(JSON.stringify(toSet([1,1,"apple",2,2,"apple", [1,2,3]])));
}
// takes an array and converts it to a sorted set with no duplicates
function toSet(arr){
    //sorts the array, then filters out repeat occurrences by position
    return arr.sort().filter(function(item, pos, self) {
        return self.indexOf(item) == pos;
    });
}

// returns true if element ∈ setA, false otherwise
function inSet(element, setA){
    return setA.indexOf(element) != -1;
}

// returns true if setA = setB false otherwise
function seteq(setA, setB) {
    if(setA.length != setB.length){
        return false
    }else{
        for(i=0; i<setA.length; i++){
            if(setA[i] instanceof Array && setB[i] instanceof Array){
                if(seteq(setA[i],setB[i])==false){
                    return false
                }
            }else {
                if (setA[i] !== setB[i]) {
                    return false
                }
            }
        }
        return true;
    }
}

// returns setA ∪ setB
function union(setA, setB) {
    //concat A and B then remove duplicates
    return toSet(setA.concat(setB));
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

}

// returns cardinality of setA
function card(setA) {
    setA.length;
}

function pow(setA){

}