var is_clean = true

if(is_clean == true){
    console.log("Good Shit")
}
else if(){

}
else {
    console.log("How could you")
}

// Variety Grill example

function order() {
    console.log(document.getElementById("food-menu").value)
    if(document.getElementById("food-menu").value =="Burger"){
        console.log("Serve with Fries")
    } 
    else if(document.getElementById("food-menu").value =="Salmon"){
        console.log("Serve with Coleslaw")
    }
    else{
        console.log("Serve with Sushi")
    }
}