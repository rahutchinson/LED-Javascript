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

