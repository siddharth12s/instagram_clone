var modal = document.getElementById("myModal");
const userDataList = ["ramesh", "sureshi", "rajuan"];
// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function () {
  modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
  modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

// For extending the sidebar
const searchBtn = document.getElementById("searchBtn");
const inputField = document.getElementById("searchField");
const searchDiv = document.getElementById("searchDiv");
const sidebar = document.getElementById("sidebar");
searchDiv.classList.toggle("hidesearch");

// Toggle the width of the sidebar and open the search input box upon clicking the search button
searchBtn.addEventListener("click", function () {
  sidebar.classList.toggle("shrink");
  searchDiv.classList.toggle("slide");
  setTimeout(() => {
    searchDiv.classList.toggle("hidesearch");
  }, 300);
  // searchDiv.classList.toggle('hidesearch');
});
// searchField.addEventListener('input', function (event) {
//     console.log(event.target.value);
// });
// // Perform any desired actions with the new value
// function GFG_Fun() {
//     console.log("event");
// }

document.addEventListener("DOMContentLoaded", function () {
  // Get the search field element
  const searchField = document.getElementById("searchField");
  // Get the search results element
  const searchResults = document.getElementById("searchResults");

  // Attach an event listener for the 'input' event
  searchField.addEventListener("input", function () {
    // Get the current search value
    const searchValue = this.value;

    // Make an AJAX request to the search view in the backend
    const xhr = new XMLHttpRequest();
    xhr.open("GET", `/search/?search_query=${searchValue}`, true);
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        // Handle the response from the backend
        const response = JSON.parse(xhr.responseText);
        console.log(response);

        // Update the UI with the search results
        const searchResults = document.getElementById("searchResults");
        searchResults.innerHTML = ""; // Clear previous results

        if (response.length > 0) {
          response.forEach(function (result) {
            const resultElement = document.createElement("a");
            resultElement.href = `/profile/${result}`;
            resultElement.className = "btn btn-light search-name";
            resultElement.textContent = result;
            resultElement.setAttribute("data-search", result);
            searchResults.appendChild(resultElement);
          });
        } else {
          const noResultsElement = document.createElement("p");
          noResultsElement.textContent = "No search results found.";
          searchResults.appendChild(noResultsElement);
        }
      } else if (xhr.readyState === 4 && xhr.status !== 200) {
        // Handle the error
        console.log(xhr.status);
        console.error("Error:", xhr.status);
      }
    };
    xhr.send();
  });
});
