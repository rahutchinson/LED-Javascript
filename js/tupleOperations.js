/**
 * Created by theso_000 on 2/8/2017.
 */
/*
 tuplesub: If u is an n-tuple and 1 ≤ i ≤ n,
  then we may write u[i] for the i'th coordinate of u.
   This operation is left-associative, i.e., we may write  u[i][j] for (u[i])[j]
 tupleq:
 If u is an m-tuple and v is an n-tuple,
  then u = v is true if m = n and u[i] = v[i] for all i in {1..n},  and false otherwise.
 If u is a tuple and r is a number, atom, set, or lambda expression,
  then the statements u = r and r = u are both false.
 */

function tuplesub(u,i){
    if(1<=i<=u.length){
        return u[i];
    }else{
        return undefined;
    }
}

function tupleq(u,v){
    if(u.length==v.length){
        for(i=0;i<u.length;i++){
            if(u[i] instanceof Array && v[i] instanceof Array){
                if(tupleq(u[i],v[i]) == false){
                    return false
                }
            }else{
                if (u[i] !== v[i]) {
                    return false;
                }
            }
        }
        return true;
    }else{
        return false;
    }
}