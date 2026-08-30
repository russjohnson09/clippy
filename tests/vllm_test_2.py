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