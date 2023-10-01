chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.message === "getVideoID") {
    const videoID = getYouTubeVideoID();
    sendResponse({ videoID: videoID });
  } else if (request.message === "fetchUserRequests") {
    const videoID = request.videoID;
    if (videoID) {
      fetchUserRequests(videoID);
    }
  }
});

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.message === "getVideoID") {
    const videoID = getYouTubeVideoID();
    sendResponse({ videoID: videoID });
  } else if (request.message === "controversialsLists") {
    const videoID = request.videoID;
    if (videoID) {
      fetchControversialsLists(videoID);
    }
  }
});

function getYouTubeVideoID() {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get("v") || "";
}

function fetchUserRequests(videoID) {
  console.log("Fetching user requests for video ID:", videoID);
  fetch(`http://localhost:5000/user_requirements/?video_id=${videoID}`)
    .then((response) => response.json())
    .then((data) => {
      console.log("Received user requests:", data);
      chrome.runtime.sendMessage({ message: "displayResults", data: data });
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      chrome.runtime.sendMessage({
        message: "displayError",
        error: error.message,
      });
    });
}

function fetchControversialsLists(videoID) {
  console.log("Fetching user requests for video ID:", videoID);
  fetch(`http://localhost:5000/controversyKeywords/?video_id=${videoID}`)
    .then((response) => response.json())
    .then((data) => {
      console.log("Received user requests ava:", data);
      chrome.runtime.sendMessage({
        message: "displayControversialsResults",
        data: data,
      });
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      chrome.runtime.sendMessage({
        message: "displayError",
        error: error.message,
      });
    });
}
