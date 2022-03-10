//Always hungry

function alwaysHungry(arr) {
    var foodCount = 0;
     for(var i =0;i<arr.length;i++){
         if(arr[i] =="food"){
             console.log("yummy");
             foodCount++
            }
     }
     if(foodCount == 0) {
        console.log("I'm hungry")
     }
}
   
alwaysHungry([3.14, "food", "pie", true, "food"]);
// this should console log "yummy", "yummy"
alwaysHungry([4, 1, 5, 7, 2]);
// this should console log "I'm hungry"









// High pass filter
function highPass(arr, cutoff) {
    var filteredArr = [];
    for(i=0;i<arr.length;i++){
        if(arr[i]>cutoff){
            filteredArr.push(arr[i]);
        }
    }
        
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // we expect back [6, 8, 10, 9]





// Better than average 
function betterThanAverage(arr) {
    var sum = 0;
    for(var i=0; i<arr.length;i++){
        sum += arr[i];
    }

    var avg = sum / arr.length;
    var count = 0

    for(var i=0; i<arr.length; i++) {
        if(arr[i] > avg) {
            count++;
        }
    
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); 
// we expect back 4

//Revesre Array
function reverse(arr) {
    var left = 0;
    var right = arr.length - 1;
    while(left < right) {
        var temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
    // your code here
    return arr;
}
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); 