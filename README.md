# GoogleDorkAI
AI powered Google Dork Command Generator (Still in Beta)

## Overview

GoogleDorkAI or DorkGPT provides a simiple terminal interface using rich and uses a tuned Ollama model to generate a Google Dork command based the user's search query.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CyberJulian/GoogleDorkAI.git
   cd GoogleDorkAI
   ```
2. Set up a Python virtual environment:
   ```bash
   python3 -m venv DorkGPT
   # Mac/Linux
   source DorkGPT/bin/activate
   # Windows
   DorkGPT\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure the Ollama is installed and configured on your system - Visit [Ollama](https://ollama.com)'s website for installation instructions.

5. Change the Ollama model if needed or desired my entering the name and parameter in the following vairable located in DorkGPT.py:
   ```python
   model_name = "gemma3:12b" # Model name and version (change if needed)
   ```

## Usage
1. Run the application:
   ```bash
   python3 DorkGPT.py
   ```
2. Enter the search query for what you want to find:
   ```
   Find me resume's between this year March and April
   ```
3. DorkGPT will generate a response:
   <pre>
   &#32;&#32;&#32;╭──────────────────────── Google Dork ─────────────────────────╮  
   &#32;&#32;&#32;│ filetype:pdf inurl:resume after:2025-03-01 before:2025-04-30 │  
   &#32;&#32;&#32;╰──────────────────────────────────────────────────────────────╯
   </pre>

## Contributing
Please feel free to leave comments, recommendations, and contribute however you feel. Also, if there is a better way to format the prompt for more efficient results, please let me know :)

### Other Notes:
I personally use gemma3:12b as my base AI but any model should work for this. You can also change the response result if you edit the prompt in prompts.py if desired.
