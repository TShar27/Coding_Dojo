//scratch
// function print(i){
//     for(var i=1; i<=100;i++){
//         if(i % 3 == 0){
//             console.log("Fizz");
//         }
//         else console.log(i);
//     }
// }

// console.log(print(1));

// // else if (i % 5 == 0){
// //     console.log("Buzz");
// // }

// console.log(i);

// else(i % 5 == 0){
//     console.log("Buzz");
// }



for (let i=1; i<=100; i++) {
     if (i%15 == 0) {
     console.log("FizzBuzz");
     }

     else if ((i%3) == 0) {
        console.log("Fizz" );
     }

     else if ((i%5) == 0) {
        console.log("Buzz");
     }

     else {
        console.log(i);
     }
}