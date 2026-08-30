

# Windows
https://github.com/ggml-org/llama.cpp/blob/master/docs/docker.md


https://llama.app/
irm https://llama.app/install.ps1 | iex
llama serve --port 8081 --host 127.0.0.1


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


