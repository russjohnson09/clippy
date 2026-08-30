

# Windows
https://github.com/ggml-org/llama.cpp/blob/master/docs/docker.md


https://llama.app/



http://127.0.0.1:8081/


```
0.00.120.626 I srv  llama_server: starting server in router mode. models will be automatically loaded on-demand
0.00.137.370 I srv  llama_server: listening on http://127.0.0.1:8081
0.09.541.007 I srv  ensure_model: model name=Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q3_K_M is not loaded, loading...
0.09.541.220 I srv          load: spawning server instance with name=Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q3_K_M on port 53998
0.09.541.247 I srv          load: spawning server instance with args:
0.09.541.247 I srv          load:   C:\Users\russj\AppData\Local\Microsoft\WindowsApps\llama.exe
0.09.541.248 I srv          load:   serve
0.09.541.248 I srv          load:   --host
0.09.541.248 I srv          load:   127.0.0.1
0.09.541.248 I srv          load:   --port
0.09.541.249 I srv          load:   53998
0.09.541.249 I srv          load:   --alias
0.09.541.249 I srv          load:   Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q3_K_M
0.09.541.249 I srv          load:   --hf-repo
0.09.541.249 I srv          load:   Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q3_K_M
0.09.547.977 I srv  ensure_model: waiting until model name=Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q3_K_M is fully loaded...
```



https://pi.dev/
```
# 2. Install the pi-llama plugin
npm install -g --ignore-scripts @earendil-works/pi-coding-agent

pi install git:github.com/huggingface/pi-llama
````



```
nvm use 24
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
pi install git:github.com/huggingface/pi-llama
```


```
irm https://llama.app/install.ps1 | iex
llama serve --port 8080 --host 127.0.0.1

http://127.0.0.1:8080/
```
llama serve --port 8081 --host 0.0.0.0


```
 pi -p "hello"
pi
```



https://github.com/earendil-works/pi/issues/6922



 pi -p "hello"



 https://pi.dev/docs/latest/models



 ```
 pi uninstall git:github.com/huggingface/pi-llama
 ```



C:\Users\russj\.pi\agent\settings.json
```{
  "packages": [],
  "lastChangelogVersion": "0.84.4",
  "theme": "dark",
  "defaultProvider": "test"
}

```

https://pi.dev/docs/latest/models

C:\Users\russj\.pi\agent\models.json
 ```
 {
  "providers": {
    "test": {
      "baseUrl": "http://localhost:8081/v1",
      "api": "openai-completions",
      "apiKey": "ollama",
      "models": [
        { "id": "Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q3_K_M" }
      ]
    }
  }
}
```


```
pi --mode json
```


{
  "providers": {
    "test": {
      "baseUrl": "http://localhost:8081/v1",
      "api": "openai-completions",
      "apiKey": "ollama",
      "models": [
        { "id": "Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q3_K_M" }
      ]
    }
  }
}


http://localhost:8081/v1/models




https://www.youtube.com/watch?v=XhliUzOmSa8

oh my pi



pi install npm:pi-permission-system



```
pi --mode json "Your prompt"
```



[/installation#windows](https://pt-act-pi-mono.mintlify.app/installation#windows)




irm https://omp.sh/install.ps1 | iex
