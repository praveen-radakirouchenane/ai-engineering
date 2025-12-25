### Ollama

1. Pull ollama/ollama image from docker hub 
    docker run ollama/ollama

2. Run Openwebui docker image 
    docker pull ghcr.io/open-webui/open-webui:v0.6.42
    docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main

3. Run Ollama in Docker + same network
    docker run -d \
  --name ollama \
  --restart unless-stopped \
  -p 11434:11434 \
  ollama/ollama

Then start Open-WebUI like this:

    docker run -d \
    --name open-webui \
    --restart unless-stopped \
    -p 3000:8080 \
    --add-host=host.docker.internal:host-gateway \
    -e OLLAMA_BASE_URL=http://host.docker.internal:11434 \
    ghcr.io/open-webui/open-webui:main


### FastAPI

1. To run the FastAPI server in local
    fastapi dev <file_name.py>


### Hugging Face
1. Install hugging face
    pip install -U "huggingface_hub"
2. Login to HF
    hf auth login
### Install transformers

        pip install transformers 

        pip install torch 