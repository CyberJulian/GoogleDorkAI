import ollama
import sys
import time
import threading
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from prompts import google_dork_prompt
import os
from rich.align import Align
# Importing the necessary libraries

console = Console()

# Clear the terminal function
def clear_terminal():
    # Clear the terminal based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

# Loading annimation
class SlidingSpinner:
    def __init__(self, message="Thinking..."):
        self.frames = [
            "[0    ]", "[ O   ]", "[  o  ]", "[   O ]",
            "[    0]", "[   O ]", "[  o  ]", "[ O   ]"
        ]
        self.message = message
        self.is_running = False
        self.thread = None

    def start(self):
        self.is_running = True
        self.thread = threading.Thread(target=self._animate)
        self.thread.start()

    def stop(self):
        self.is_running = False
        if self.thread:
            self.thread.join()
        sys.stdout.write('\r' + ' ' * (len(self.message) + 10) + '\r')
        sys.stdout.flush()

    def _animate(self):
        while self.is_running:
            for frame in self.frames:
                if not self.is_running:
                    break
                output = f'\r{self.message} {frame} '
                sys.stdout.write(output)
                sys.stdout.flush()
                time.sleep(0.1)

# Generate the Google Dork
def start_chat():
    clear_terminal()  # Clear the terminal at the start

    # Welcome Header
    console.print(Align.center(Panel.fit(
        "[bold cyan]DorkGPT (Google Dork Generator)[/bold cyan]\n"
        "Type '[bold red]exit[/bold red]' to quit.",
        title="Welcome", subtitle="Using gemma3:12b <3")))
    console.print()  # spacing
    # Helpful Examples
    console.print(Align.center(Panel.fit(
        "[bold yellow]Example Search Prompts:[/bold yellow]\n"
        "- webcamXP live cams\n"
        "- Find login portals on .gov sites\n"
        "- Look for resume PDFs\n"
        "- PowerPoint files on nasa.gov\n"
        "- John Doe in Japan\n"
        "- Phone number of John Doe",
        title="Try Searching For...", border_style="bright_blue")))
    console.print()  # spacing

    model_name = "gemma3:12b" # Model name and version (change if needed)

    # Dividing line
    console.rule("[black]Google Dork Search Query[/black]", style="black")

    # Main loop for user input
    while True:
        user_input = Prompt.ask("[bold green]Describe your search goal[/bold green]")
        if user_input.lower() == 'exit':
            console.print(Align.center("[bold red]Goodbye![/bold red]"))
            break

        spinner = SlidingSpinner("Generating Google Dork...")
        spinner.start()

        try:
            prompt = google_dork_prompt(user_input)
            response = ollama.chat(
                model=model_name,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            reply = response['message']['content'].strip()
        except Exception as e:
            reply = f"[ERROR] Could not connect to Ollama: {e}"
        finally:
            spinner.stop()

        # Response handling
        console.print(Align.center(Panel.fit(reply or "No response received.", title="[bold magenta]Google Dork[/bold magenta]", border_style="magenta")))
        console.print()  # spacing

if __name__ == '__main__':
    try:
        start_chat()
    # Handle keyboard interrupt (Ctrl+C)
    except KeyboardInterrupt:
        console.print(Align.center("\n[bold red]Manual shutdown...Goodbye![/bold red]"))
        console.print() # Add spacing