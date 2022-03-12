var count = 3;
var countElement = document.querySelector("#likes");


console.log(countElement);

function plus1() {
    count++;
    countElement.innerText = count + " like(s)";
    console.log(count);
}