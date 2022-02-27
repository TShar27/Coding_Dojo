// example 1

function subtractBy2(num){
    var results = num-2;
    console.log(results);
    return results
}

console.log(subtractBy2(8))

// example 2 

function returnEven(arr){
    var arr2 = [];
    for(var i = 0; i<arr.length;i++){
            if(arr[i] % 2 == 0){ //if array of i is divisibile by 2 with no remainder
                arr2.push(arr[i])
            }  
    }
    return arr2
}

console.log(returnEven([2,4,5,9]))



// example 3
var start = 0;
var end = 10;
    
while(start <= end) {
    console.log("start: " + start + ", end: " + end);
    start++;
    end--;
}


