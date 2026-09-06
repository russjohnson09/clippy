https://pi.dev/

```
$ nvm use 24
Now using node v24.20.0 (64-bit)
(clippy) 
russj@beam MINGW64 ~/dev/clippy (feat/clippy-commits)
$ pi --version
0.84.4
(clippy) 
```

Should .pi\settings.json

be pointing at bifrost?

http://localhost:8080/workspace/logs

I'm not going to have llm logs with my current setup.



https://codesamplez.com/productivity/local-ai-coding-agent




cat ~/.pi/agent/models.json

```
{
  "providers": {
    "test2": {
      "baseUrl": "http://localhost:8081/v1",
      "api": "openai-completions",
      "apiKey": "ollama",
      "compat": {
        "supportsDeveloperRole": true,
        "supportsReasoningEffort": true
      },
      "models": [
        {
          "id": "Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q3_K_M",
          "reasoning": true
        }
      ]
    }
  }
}
```


# Bifrost AI Gateway provider for pi
https://github.com/lxdlam/pi-bifrost-provider

```
pi --version
pi install npm:pi-bifrost-provider
pi
/login bifrost
```


I should just be doing all of this in docker and avoiding windows altogether it seems.

I'll get there eventually. Pushing this up for now.