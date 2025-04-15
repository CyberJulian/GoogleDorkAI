# GoogleDorkAI
AI powered Google Dork Command Generator

## Overview

GoogleDorkAI or DorkGPT provides a simiple terminal interface using rich and uses an tuned Ollama model to generate a Google Dork command based the user's search query.

## Installation

1. Clone the repository:
   ```bash
   https://github.com/CyberJulian/GoogleDorkAI.git
   cd GoogleDorkAI
   ```
2. Set up a Python virtual environment:
   ```bash
   python3 -m venv venv
   # Mac/Linux
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure the Ollama is installed and configured on your system - Visit [Ollama](https://ollama.com)'s website for installation instructions.

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
   ```
   ╭──────────────────────── Google Dork ─────────────────────────╮
   │ filetype:pdf inurl:resume after:2025-03-01 before:2025-04-30 │
   ╰──────────────────────────────────────────────────────────────╯
   ```

## Contributing
Please feel free to leave comments, recommendations, and contribute however you feel :)

### Other Notes:
I personally use gemma3:12b as my base AI but any model should work for this.
