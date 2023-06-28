// Get the follow/unfollow button element
const followButton = document.getElementById("followButton");

// Get the followers count element
const followersCount = document.querySelector(".followers");

// Add a click event listener to handle the AJAX request
followButton.addEventListener("click", function (event) {
  event.preventDefault(); // Prevent the default link behavior

  // Send an AJAX request to update the follow/unfollow status in the database
  const url = followButton.getAttribute("href");
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      // Update the button state based on the response
      const isFollowing = data.is_following;

      if (isFollowing) {
        followButton.textContent = "Unfollow";
        followButton.classList.add("unfollow");
        followButton.classList.remove("follow");
        followButton.classList.remove("btn-primary");
        followButton.classList.add("btn-light");

        // Increase the followers count by 1
        const newFollowersCount = parseInt(followersCount.textContent) + 1;
        followersCount.textContent = newFollowersCount + " Followers";
      } else {
        followButton.textContent = "Follow";
        followButton.classList.add("follow");
        followButton.classList.remove("unfollow");
        followButton.classList.remove("btn-light");
        followButton.classList.add("btn-primary");

        // Decrease the followers count by 1
        const newFollowersCount = parseInt(followersCount.textContent) - 1;
        followersCount.textContent = newFollowersCount + " Followers";
      }
    })
    .catch((error) => {
      // Error handling if needed
    });
});
