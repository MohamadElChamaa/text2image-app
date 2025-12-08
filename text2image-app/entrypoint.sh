#!/bin/bash
set -e


# Variables configurables
export GRADIO_SERVER_NAME=0.0.0.0
export GRADIO_SERVER_PORT=7860


# Lance l'application Gradio (main.py) via uvicorn / direct execution
python app/main.py