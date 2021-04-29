function changeInput() {
    var a = document.getElementById("timeInput");
    var b = document.getElementById("pointInput");

    if (a.style.display === "none") {
        a.style.display = "inline";
        b.style.display = "none";
    }
    else {
        a.style.display = "none";
        b.style.display = "inline";
    }
}


