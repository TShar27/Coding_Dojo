var nameInput = document.querySelector("#name");
var foodToOrder = "Pizza";

function setName(element) {
    console.log(element.value);
    nameInput.innertext = element.value;
}

function pickFood(element) {
    console.log("The foood is " + element.value); 
    foodToOrder = element.value;
}

function order() {
    alert("ordering a " + foodToOrder);
}