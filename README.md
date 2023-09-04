# Chrome Extension for Text Summarization with BERT Integration

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)

## Overview
<a name="overview"></a>

The Chrome Extension for Text Summarization is a powerful tool that allows users to easily summarize text content from webpages they visit or input manually. Leveraging the capabilities of the BERT-based summarization model (sshleifer/distilbart-cnn-12-6) and a robust Django backend, this extension provides concise summaries while retaining critical information. The user-friendly interface, built with HTML, CSS, and JavaScript, enhances the browsing experience by simplifying lengthy content.


## Features
<a name="features"></a>

- Efficient Summarization: Utilizes the BERT-based summarization model for accurate and efficient text summarization.
- Browser Integration: Seamlessly integrates with the Chrome browser for quick access to text summarization.
- User-Friendly Interface: Provides an intuitive and easy-to-use interface for summarizing text from both websites and user input.
- Customizable Settings: Allows users to adjust summarization parameters to meet their specific needs.
- Cross-Platform Compatibility: Works on various platforms, providing text summaries wherever Chrome is installed.

## Installation
<a name="installation"></a>

To install the Chrome Extension, follow these steps:

1. Clone the repository to your local machine:

        git clone https://github.com/your-username/chrome-extension-text-summarization.git

2. Open Google Chrome.

3. Navigate to chrome://extensions/.

4. Enable "Developer mode" in the top-right corner.

5. Click on "Load unpacked" and select the extension folder from the cloned repository.

## Usage
<a name="usage"></a>

1. Click on the extension icon in the Chrome toolbar to open the summarization tool.

2. To summarize content from a webpage, click the "Summarize Current Page" button.

3. To summarize custom text, enter or paste the text into the input field and click the "Summarize Text" button.

4. Adjust summarization parameters (if needed) and click "Summarize" to generate a summary.

5. The summarized text will be displayed, and you can copy it to your clipboard or perform additional actions as needed.

## Tech Stack
<a name="tech-stack"></a>

- Backend: Python, Django
- Summarization Model: BERT (sshleifer/distilbart-cnn-12-6)
- Frontend: HTML, CSS, JavaScript
- Chrome Extension: Manifest JSON, JavaScript

## Contributing
<a name="contributing"></a>

Contributions are welcome! To contribute to this project:

    Fork the repository.

    Create a new branch with a descriptive name.

    Make your changes and commit them.

    Push your changes to your fork.

    Submit a pull request, detailing the changes made and the purpose.

