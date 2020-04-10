//JUMP TO THE TOP BUTTON & SHRINKING HEADER
var mybutton = document.getElementById("myBtn");
// When the user scrolls down 20px from the top of the document, show the button
// When the user scrolls down 50px from the top of the document, resize the header's font size
window.onscroll = function () { scrollFunction(); };

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        document.getElementById("header").style.fontSize = "30px";
        document.getElementById("customize-script-container").style.display = "none";
    } else {
        document.getElementById("header").style.fontSize = "90px";
        document.getElementById("customize-script-container").style.display = "block";
    }
}
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}