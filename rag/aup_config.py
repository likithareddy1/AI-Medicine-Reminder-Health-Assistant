# setup.py
# AI Medicine Reminder & Health Assistant Setup
# team : Fusion minds
# team mates:K.Likitha,G.Naveen,Thahiya

import subprocess
import time
import logging

logging.basicConfig(level=logging.INFO)


def run(cmd, shell=False):
    """Run a command."""
    try:
        result = subprocess.run(
            cmd,
            shell=shell,
            check=True,
            text=True,
            capture_output=True
        )
        print(f"SUCCESS: {' '.join(cmd) if not shell else cmd}")
        return result
    except subprocess.CalledProcessError as e:
        print(f"ERROR:\n{e.stderr}")
        return None


def install_packages():
    """Install all required Python packages."""

    packages = [
        "langchain",
        "langchain-community",
        "langchain-text-splitters",
        "langchain-experimental",
        "langchain-openai",
        "langchain-ollama",
        "langgraph",
        "langchain-chroma",
        "chromadb",
        "faiss-cpu",
        "pypdf",
        "ollama",
        "fastapi",
        "uvicorn",
        "gradio",
        "ipywidgets",
        "requests",
        "beautifulsoup4",
        "openai",
    ]

    print("Upgrading pip...")
    run(["python3", "-m", "pip", "install", "--upgrade", "pip"])

    print("Installing required packages...")
    run(["pip", "install"] + packages)


def check_ollama():
    """Check whether Ollama is installed."""

    print("Checking Ollama installation...")

    result = subprocess.run(
        ["which", "ollama"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print("Ollama is not installed. Installing...")

        run(
            "curl -fsSL https://ollama.com/install.sh | sh",
            shell=True,
        )
    else:
        print("Ollama is already installed.")


def start_ollama():
    """Start Ollama if it is not already running."""

    print("Checking Ollama server...")

    result = subprocess.run(
        ["ollama", "list"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )

        time.sleep(5)

        print("Ollama server started.")
    else:
        print("Ollama server is already running.")


def pull_models():
    """Download required Ollama models."""

    models = [
        "llama3.1:8b",
        "nomic-embed-text",
    ]

    print("Pulling required models...")

    for model in models:
        print(f"Pulling {model}")
        run(["ollama", "pull", model])

    print("All models downloaded.")


def verify_installation():
    """Display installed Ollama models."""

    print("Installed Ollama models:")
    run(["ollama", "list"])


def main():

    print("=" * 60)
    print("AI Medicine Reminder & Health Assistant Setup")
    print("=" * 60)

    install_packages()

    check_ollama()

    start_ollama()

    pull_models()

    verify_installation()

    print("\nSetup completed successfully.")


if __name__ == "__main__":
    main()