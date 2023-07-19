window.onscroll = function() { scrollFunction() };

function scrollFunction() {
    if(document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        document.getElementById("top-btn").style.display = "block";
    } else {
        document.getElementById("top-btn").style.display = "none";
    }
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}