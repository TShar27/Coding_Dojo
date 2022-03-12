console.log("Working");
var count = 0;
var countElement = document.querySelector("#cart_num");
var img = document.getElementById("#imgClickAndChange");

function message() {
    alert("This game is supported on Linux")
}

function plus1() {
    count++;
    countElement.innerText = count;
    console.log(count);
}
function changeImage() {
        
    if (document.getElementById("imgClickAndChange").src == "images/stonepunk.png") 
        {
            document.getElementById("imgClickAndChange").src = "images/cafe-neko.png";
        }
        else 
        {
            document.getElementById("imgClickAndChange").src = "images/pixel-ninjas-2.png";
        }
    }
 
function changeImageBack() {
        
    if (document.getElementById("imgClickAndChange").src == "images/pixel-ninjas-2.png") 
        {
            document.getElementById("imgClickAndChange").src = "images/cafe-neko.png";
        }
        else 
        {
            document.getElementById("imgClickAndChange").src = "images/stonepunk.png";
        }
    }