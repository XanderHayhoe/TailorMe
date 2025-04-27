console.log("TailorMe content script initialized");

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  console.log("Received message:", request);
  if (request.action === "scrape_job") {
    const jobDescription = document.title; // get the title of the job for now
    console.log("Sending back title:", jobDescription);
    sendResponse({ jobDescription: jobDescription });
    return true;
  }
});
