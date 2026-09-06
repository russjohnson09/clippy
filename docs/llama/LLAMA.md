


# Startup
## Requirements
llama.ccp is installed. https://llama.app/


## Basic cli command
```
llama cli -hf Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q3_K_M --reasoning off -n 1000 --verbose-prompt --single-turn --temp 0.0 -p "hi"
```


## Server running a single model
```
llama serve --port 8081 -hf Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q3_K_M
```
http://127.0.0.1:8081/#/

## Server running all cached models

```
 llama cli -cl
number of models in cache: 5
   1. empero-ai/Qwen3.8-4B-Distill-GGUF:Q4_K_M
   2. Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q3_K_M
   3. Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q4_K_M
   4. unsloth/gemma-4-E2B-it-GGUF:Q4_K_X
```

http://127.0.0.1:8081/models
```
llama serve --port 8081
```
