document.addEventListener("DOMContentLoaded", function () {
  const tabButtons = document.querySelectorAll(".tab-button");
  const tabContents = document.querySelectorAll(".tab-content");

  // Show the first tab by default
  tabContents[0].classList.add("active");

  // Handle tab button clicks
  tabButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const targetTab = button.getAttribute("data-tab");

      // Hide all tab contents
      tabContents.forEach((content) => {
        content.classList.remove("active");
      });

      // Show the clicked tab content
      document.getElementById(`${targetTab}-content`).classList.add("active");
    });
  });

  const getVideoIDButton = document.getElementById("getVideoIDButton");
  const videoIDDisplay = document.getElementById("videoIDDisplay");
  const requestList = document.getElementById("requestList");
  const controversialsLists = document.getElementById("getControversialTopic");
  const controversialsTopicSearchBtn = document.getElementById("controversialsTopicSearchBtn");
  const controversialIDDisplay = document.getElementById(
    "controversialIDDisplay"
  );
  const controversialSearchDisplay = document.getElementById("controversialSearchDisplay");

  controversialsTopicSearchBtn.addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      chrome.tabs.sendMessage(
        tabs[0].id,
        { message: "getVideoID" },
        function (response) {
          if (response && response.videoID) {
            if(document.getElementById("controversialsTopicSearch").value!=""){
              chrome.tabs.sendMessage(tabs[0].id, {
                search: document.getElementById("controversialsTopicSearch").value,
                message: "controversialsTopicSearch",
                videoID: response.videoID,
              });
            }else{
              controversialSearchDisplay.textContent="type search bar";
            }
          } else {
            controversialSearchDisplay.textContent = "Video ID not found.";
          }
        }
      );
    });
  });

  getVideoIDButton.addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      chrome.tabs.sendMessage(
        tabs[0].id,
        { message: "getVideoID" },
        function (response) {
          if (response && response.videoID) {
            videoIDDisplay.textContent = "Video ID: " + response.videoID;
            // Send message to content script to fetch user requests
            chrome.tabs.sendMessage(tabs[0].id, {
              message: "fetchUserRequests",
              videoID: response.videoID,
            });
          } else {
            videoIDDisplay.textContent = "Video ID not found.";
          }
        }
      );
    });
  });

  controversialsLists.addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      chrome.tabs.sendMessage(
        tabs[0].id,
        { message: "getVideoID" },
        function (response) {
          if (response && response.videoID) {
            controversialIDDisplay.textContent =
              "Video ID: " + response.videoID;
            // Send message to content script to fetch user requests
            chrome.tabs.sendMessage(tabs[0].id, {
              message: "controversialsLists",
              videoID: response.videoID,
            });
          } else {
            controversialIDDisplay.textContent = "Video ID not found.";
          }
        }
      );
    });
  });
});

// Listen for messages from the content script to display the results or errors
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.message === "contentScriptReady") {
    // Once the content script is ready, send a message to fetch the video ID
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      chrome.tabs.sendMessage(tabs[0].id, { message: "getVideoID" });
    });
  } else if (request.message === "displayResults") {
    const data = request.data;
    console.log("Received user requests:", data);
    displayResults(data); // Display the received data in the popup
  } else if (request.message === "displayError") {
    console.log("ava 2");
    const error = request.error;
    console.error("Error fetching data:", error);
    displayError(error); // Handle error in the popup
  } else if (request.message === "displayControversialsResults") {
    console.log("ava", request);
    const data = request.data;
    console.log("Received user requests:", data);
    displayConveResults(data); // Display the received data in the popup
  } else if (request.message === "displayControversialsComments") {
    console.log("ava 11", request);
    const data = request.data;
    console.log("Received user requests:", data);
    displayConveResultsComments(data); // Display the received data in the popup
  }
});

function displayResults(data) {
  console.log(data);
  const results = data.results;
  // Check if results is an array
  if (!Array.isArray(results)) {
    requestList.textContent = "Error: Invalid data received.";
    return;
  }
  if (results.length === 0) {
    requestList.textContent = "No user requirements found in comments.";
  } else {
    requestList.textContent = "User Requirements:";
    const ul = document.createElement("ul");
    results.forEach((request) => {
      const li = document.createElement("li");
      li.textContent = request;
      ul.appendChild(li);
    });
    requestList.appendChild(ul);
  }
}

function displayConveResults(data) {
  console.log("data ava", data);
  const results = data;
  if (results.length === 0) {
    controversialList.textContent = "No user requirements found in comments.";
  } else {
    const jsonObject = JSON.parse(results.predictions);
    controversialList.textContent = "Controversial Topics";
    const entries = Object.entries(jsonObject);
    const ul = document.createElement("ul");

    if (entries.length > 0) {
      for (const [key, value] of entries) {
        let row = `${key} : ${value}`;
        const li = document.createElement("li");
        li.textContent = row;
        ul.appendChild(li);
      }

      const mathMarks = [80, 75, 90, 85, 70];
      const scienceMarks = [70, 85, 80, 90, 95];

      // Get the canvas element
      const canvas = document.getElementById("marksChart");

      const div = document.createElement("h2");
      //div.textContent = "Overall Rating = " + results.overall_count + "%";

      controversialList.appendChild(ul);
      controversialList.appendChild(div);
    } else {
      const div = document.createElement("div");
      div.textContent = "No Controversial comment found";
      controversialList.appendChild(div);
    }

    // results.forEach((request) => {
    //   const li = document.createElement("li");
    //   li.textContent = request;
    //   ul.appendChild(li);
    // });
    // requestList.appendChild(ul);
  }
}


function displayConveResultsComments(data) {
  console.log("data ava 11", data);
  const results = data;
  if (results.length === 0) {
    controversialList.textContent = "No found in comments.";
  } else {
    const jsonObject = JSON.parse(results.predictions);
    controversialList.textContent = "Comments";
    const entries = Object.entries(jsonObject);
    const ul = document.createElement("ul");

    if (entries.length > 0) {
      for (const [key, value] of entries) {
        let row = `${key} : ${value}`;
        const li = document.createElement("li");
        li.textContent = row;
        ul.appendChild(li);
      }

      const mathMarks = [80, 75, 90, 85, 70];
      const scienceMarks = [70, 85, 80, 90, 95];

      // Get the canvas element
      const canvas = document.getElementById("marksChart");

      const div = document.createElement("h2");
      //div.textContent = "Overall Rating = " + results.overall_count + "%";

      controversialList.appendChild(ul);
      controversialList.appendChild(div);
    } else {
      const div = document.createElement("div");
      div.textContent = "No comment found";
      controversialList.appendChild(div);
    }
    
  }
}

function displayError(error) {
  requestList.textContent = "Error fetching data: " + error;
}
