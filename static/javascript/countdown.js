var final_date = new Date("Jul 24, 2021");

var x = setInterval(function() {

  // Dnešní datum
  var now = new Date();
  // Vzdálenost do finálního data
  var distance = final_date - now;
    
  // Převod na dny
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));

  document.getElementById("countdown").innerHTML = days + " days left until the Olympics";
  
  // Vypsání chybové hlášky
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("countdown").innerHTML = "Olympics have already begun";
    }
}, 100);



