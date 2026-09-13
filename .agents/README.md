test




https://agentskills.io/specification


docker-compose.yml

# Start the llama cpp server on host
```
LLAMA_ARG_PORT=9931 LLAMA_ARG_VERBOSE=1 LLAMA_ARG_HOST=0.0.0.0 HF_HUB_CACHE=./models llama server
```


# Start ubuntu for the devin client

```
docker compose up --build
docker compose exec -it ubuntu-basic bash
curl -fsSL https://cli.devin.ai/install.sh | bash
```

enter the token manually


Restart your shell or run: source /root/.bashrc. Then run devin to get started.
So include a volume for this so it isn't lost?


<!-- root@4bb4deb48d83:/data# ls ~/.local/bin/devin 
/root/.local/bin/devin -->

