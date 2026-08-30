from vllm import LLM, SamplingParams


llm = LLM(model="Qwen/Qwen2.5-0.5B-Instruct")
 
prompts = [
    "Explain vLLM in one paragraph.",
    "List three production risks for self-hosted LLM serving.",
]
 
sampling_params = SamplingParams(
    temperature=0.2,
    top_p=0.95,
    max_tokens=160,
)


# vllm serve Qwen/Qwen2.5-0.5B-Instruct --host 0.0.0.0 --port 8000


# vllm serve Qwen/Qwen2.5-7B-Instruct --gpu-memory-utilization 0.85


# https://github.com/OpenHands/OpenHands

# Error: pull model manifest: file does not exist

# ollama --version
# ollama pull  Qwen/Qwen2.5-0.5B-Instruct
# ollama run Qwen/Qwen2.5-0.5B-Instruct
# ollama ls
# ollama run qwen2.5-coder:1.5b-base


# docker model run hf.co/zai-org/GLM-5.3-Flash 


# https://docs.docker.com/ai/model-runner/


# docker model configure --context-size 8192 ai/qwen2.5-coder



https://github.com/unslothai/unsloth/


https://unsloth.ai/docs/models/glm-5.2
