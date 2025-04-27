document.getElementById("scrapeButton").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(
      tabs[0].id,
      { action: "scrape_job" },
      (response) => {
        console.log("Response received from content.js:", response);
        if (response && response.jobDescription) {
          console.log("Scraped job description:");
          console.log(response.jobDescription);
          alert(
            "Scraped first 100 characters: " +
              response.jobDescription.substring(0, 100)
          );
        } else {
          console.error("Failed to scrape job description.");
        }
      }
    );
  });
});
