// Best way to grab the last # of an array?
var arr = [5,10,12,90,3,7]
console.log(arr[arr.length-1])

// Warm up exercise 
function findChar(arr, targetLetter){
    var is_found = false
    for(var i=0; i<arr.length;i++){
        if(arr[i]==targetLetter){
            is_found = true
        }
    }
    return is_found
}

console.log(findChar(["r","a","c","e","c","a","r"], "c"))
console.log(findChar(["r","a","c","e","c","a","r"], "f"))

// Fibonaci example
function fibonaciArray(n){
    // the [0,1] are the starting values of the array to calculate the rest from
    var fibArr = [0,1];
    var sum = 0;
    for(var i = 0; i<n-2; i++){ // Or you could do for(var i=0; fibArr.length< n;i++)
        sum = fibArr[i] + fibArr[i+1]
        fibArr.push(sum)
        }
    return fibArr
}

var result = fibonaciArray(10);
console.log(result); 


// Fibonaci example 2 (While loop)
function fibonaciArray(n){
    // the [0,1] are the starting values of the array to calculate the rest from
    var fibArr = [0,1];
    sum = 0;
    while(n>2){
        sum = fibArr[fibArr.length-2] + fibArr[fibArr.length-1]
        fibArr.push(sum);
        n--;

    }
    return fibArr
}

var result = fibonaciArray(10);
console.log(result); 