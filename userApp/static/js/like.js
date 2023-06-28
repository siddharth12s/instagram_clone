document.addEventListener("DOMContentLoaded", function() {
    var likeButton = document.getElementById("myIcons");
    var likeCount = document.getElementById("likeCount");
  
    likeButton.addEventListener("click", function(event) {
      event.preventDefault();
      var url = this.getAttribute("href");
  
      fetch(url)
        .then(function(response) {
          return response.json();
        })
        .then(function(data) {
          if (data.is_liked) {
            likeButton.classList.add("liked");
          } else {
            likeButton.classList.remove("liked");
          }
  
          likeCount.textContent = data.like_count;
        })
        .catch(function(error) {
          console.error("Error:", error);
        });
    });
  });
  