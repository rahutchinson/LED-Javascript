/**
 * Created by theso_000 on 1/30/2017.
 */
// takes an array and converts it to a sorted set with no duplicates
function toSet(arr){
    //sorts the array, then filters out repeat occurrences by position
    if(typeof arr[0] == "number") {
        return arr.sort(function (a, b) {
            return (a - b);
        }).filter(function (item, pos, self) {
            return self.indexOf(item) == pos;
        });
    }else{
            return arr.sort().filter(function (item, pos, self) {
                return self.indexOf(item) == pos;
            });
        }
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
    setA.length;
}

function pow(setA){

}

console.log(cross(toSet([1,2,3,1,2,1,0]),toSet([1,2,3,1,2,1,0])));