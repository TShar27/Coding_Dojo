console.log("Loading...");

 var username = document.querySelector("#name");

 var requestSpan = document.querySelector("#requests");
 var connectionSpan = document.querySelector("#connections");
//  console.log(countElement);

function changeName() {
    username.innerText = "Timmy Shar";
    console.log();
}

function accept(id) {
    var element = document.querySelector(id);
    element.remove();
    requestSpan.innerText--;
    connectionSpan.innerText++;
}

function ignore(id) {
    var element = document.querySelector(id);
    element.remove();
    requestSpan.innerText--;
}

// var count = 2;
// var countElement = document.querySelector("connections");

// function subtract1(){
//    count--;
//    console.log(count) 
// }
