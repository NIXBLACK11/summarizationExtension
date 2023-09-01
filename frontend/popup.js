document.addEventListener('DOMContentLoaded', function() {

  const pageContent = document.body.textContent;

  console.log(pageContent);

  // Get references to the input and output textareas and the button
  var inputTextarea = document.getElementById('inputText');
  var outputTextarea = document.getElementById('outputText');
  var summarizeButton = document.getElementById('summarizeButton');

  // Define the URL of your summarization API
  var apiUrl = "http://127.0.0.1:8000/summarizer/summarize/";

  // Add a click event listener to the button
  summarizeButton.addEventListener('click', function() {
    // Get the input text from the textarea
    var inputText = inputTextarea.value;
    // Check if the input text is not empty
    if (inputText.trim() === '') {
      alert("Please enter text to summarize.");
      return;
    }
    // console.log(inputText);
    // Create a JSON payload with the input text
    var payload = {
      "input_text": inputText
    };

    // Send a POST request to the API
    fetch(apiUrl, {
      method: 'POST',
      body: JSON.stringify(payload),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(function(response) {
      if (response.status === 200) {
        // Parse the response JSON
        return response.json();
      } else {
        throw new Error('Summarization failed.');
      }
    })
    .then(function(data) {
      // Extract the summarized text from the response JSON
      var summarizedText = data.summarized_text;

      // Set the summarized text in the output textarea
      outputTextarea.value = summarizedText;
    })
    .catch(function(error) {
      // Handle any errors here
      outputTextarea.value = "Summarization failed. Error: " + error.message;
    });
  });
});
