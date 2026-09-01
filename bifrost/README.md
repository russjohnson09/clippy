https://stackoverflow.com/questions/69027224/the-nvmrc-file-is-not-read

Windows .nvmrc support is limited



# Setup
https://docs.getbifrost.ai/quickstart/gateway/setting-up

```
nvm use 24

npx -y @maximhq/bifrost -app-dir ./my-bifrost-data


start http://localhost:8080


llama serve --port 8081

0.01.465.679 I cmn  common_param: common_params_print_info: verbosity = 3 (adjust with the `-lv N` CLI arg)
```


```

curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"ollama/Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q3_K_M","messages":[{"role":"system","content":""},{"role":"user","content":"hi"}]}'
```


http://localhost:8080/workspace/prompt-repo?promptId=3cdf5af0-ab23-47c0-86af-bfaaaec1708f


Qwen3.8-4B-Q4_K_M.gguf	Q4_K_M	2.783 GB	Recommended. Best quality/size balance for most users.

