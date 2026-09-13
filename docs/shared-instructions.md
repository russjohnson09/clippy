# Shared AI Infrastructure Setup

## Prerequisites

### llama.cpp Setup
Install llama.cpp: https://llama.app/

### Basic CLI Command
```bash
llama-cli -hf Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q3_K_M --reasoning off -n 1000 --verbose-prompt --single-turn --temp 0.0 -p "hi"
```

### Server Configuration
Run llama.cpp server on port 8081:
```bash
llama-serve --port 8081
```

Visit: http://127.0.0.1:8081/#/

For multiple cached models:
```bash
llama-serve --port 8081
```

## Bifrost AI Gateway

### Setup
See: https://github.com/gobifrost/bifrost

Bifrost provides:
- **Drop-in Replacement**: Treat AI requests as raw material with refined output
- **Load Balancing**: Model-specific filtering and routing

### Prerequisites
- llama.cpp setup completed

### Bifrost Configuration
See: https://docs.getbifrost.ai/features/skills-repository

## pi.dev Integration

### Installation
```bash
nvm use 24
pi --version  # Should show 0.84.4+
```

### Configure Bifrost Provider
Create `~/.pi/settings.json`:
```json
{
  "providers": {
    "bifrost": {
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

### Bifrost Provider Installation
```bash
pi install npm:pi-bifrost-provider
pi --login bifrost
```

### Logs
View logs at: http://localhost:8080/workspace/logs

## Alternative: Nimbalyst Skills
For automated repo tasks: https://nimbalyst.com/skills/commit/

## Code Project Ideas
- Download repo → perform task → push results to branch
- See: https://openai.com/codex/
