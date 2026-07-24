# Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
#
# SPDX-License-Identifier: MIT

import logging
import subprocess
import time
import os


def message_string(proc: subprocess.CompletedProcess) -> str:
    if proc.returncode == 0:
        return "successfully"

    return f"failed with return code {proc.returncode}."


def run_capture(cmd, check=False, **kwargs):
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=check,
        **kwargs
    )


def aup_setup():

    logging.info("Setting up AI Medicine Assistant Environment")


    # Upgrade pip
    proc = run_capture(
        ["python3", "-m", "pip", "install", "--upgrade", "pip"],
        check=True
    )

    logging.info(
        "Pip upgraded %s",
        message_string(proc)
    )


    # Install required packages

    packages = [
        "langgraph",
        "langchain",
        "langchain-ollama",
        "langchain-openai",
        "langchain-mcp-adapters",
        "mcp",
        "pydantic",
        "pygraphviz",
        "grandalf"
    ]


    proc = run_capture(
        [
            "pip",
            "install",
            *packages
        ],
        check=True
    )


    logging.info(
        "AI packages installed %s",
        message_string(proc)
    )


    # Check Ollama installation

    proc = run_capture(
        ["which", "ollama"]
    )


    if proc.stdout.strip() == "":

        logging.info(
            "Installing Ollama..."
        )

        run_capture(
            "curl -fsSL https://ollama.com/install.sh | sh",
            shell=True,
            check=True
        )

    else:

        logging.info(
            "Ollama already installed"
        )


    # Ollama environment settings

    os.environ["OLLAMA_FLASH_ATTENTION"] = "1"
    os.environ["OLLAMA_NO_CLOUD"] = "1"
    os.environ["OLLAMA_CONTEXT_LENGTH"] = "16000"



    # Start Ollama server

    proc = run_capture(
        ["ollama", "list"]
    )


    if proc.returncode != 0:

        subprocess.Popen(
            [
                "ollama",
                "serve"
            ],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )

        logging.info(
            "Ollama server started"
        )

        time.sleep(5)

    else:

        logging.info(
            "Ollama already running"
        )



    # Pull Llama 3.1 model

    model_list = [
        "llama3.1:8b"
    ]


    logging.info(
        "Downloading Llama3.1 model..."
    )


    for model in model_list:

        proc = run_capture(
            [
                "ollama",
                "pull",
                model
            ],
            check=True
        )

        logging.info(
            "%s downloaded %s",
            model,
            message_string(proc)
        )


    logging.info(
        "Environment setup completed"
    )


    return model_list



if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO
    )

    models = aup_setup()

    print(
        "Installed Models:",
        models
    )