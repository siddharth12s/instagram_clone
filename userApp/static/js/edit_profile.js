$(document).ready(function () {
  // Get the modal
  var modal = document.getElementById("editProfileModal");

  // Get the button element
  var button = document.getElementById("editProfileButton");
  var span = document.getElementsByClassName("edit-close")[0];

  // When the button is clicked, display the modal
  button.onclick = function () {
    modal.style.display = "block";
  };

  span.onclick = function () {
    modal.style.display = "none";
  };
  // Close the modal when the user clicks outside the modal or presses the Esc key
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };

  $(document).keyup(function (e) {
    if (e.key === "Escape") {
      modal.style.display = "none";
    }
  });
});
