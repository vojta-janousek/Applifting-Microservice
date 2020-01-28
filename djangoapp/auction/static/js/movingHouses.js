var options = ["hidden", "hidden", "visible"];
var i = 2;
var j = 1;
var k = 0;

function firstHouseBuildingGif() {
  document.getElementById("firstHouse").style.visibility = options[i];
  i++;

  if (i > options.length - 1) {
    i = 0;
  }
}

function secondHouseBuildingGif() {
  document.getElementById("secondHouse").style.visibility = options[j];
  j++;

  if (j > options.length - 1) {
    j = 0;
  }
}

function thirdHouseBuildingGif() {
  document.getElementById("thirdHouse").style.visibility = options[k];
  k++;

  if (k > options.length - 1) {
    k = 0;
  }
}

setInterval(firstHouseBuildingGif, 1000);
setInterval(secondHouseBuildingGif, 1000);
setInterval(thirdHouseBuildingGif, 1000);
