// script.js

window.addEventListener("load", function () {
  var animatedImage = document.getElementById("animated-image");

  setTimeout(function () {
    animatedImage.src = "{% static 'images/home2.png' %}";
  }, 1000); // Change the image source after 1 second (adjust the timing as needed)
});
