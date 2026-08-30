from vllm import LLM, SamplingParams

def ask_simple_question(model_name: str, question: str):
    """
    Initializes a vLLM LLM and asks a simple question.

    Args:
        model_name (str): The name of the model to load (e.g., 'meta-llama/Llama-2-7b-chat-hf').
        question (str): The simple question to ask the model.
    """
    print(f"--- Initializing vLLM for model: {model_name} ---")

    try:
        # 1. Initialize the LLM object
        # This step loads the model into memory and prepares it for inference.
        llm = LLM(model=model_name)
        print("Model loaded successfully.")

        # 2. Define the sampling parameters (how the output should look)
        sampling_params = SamplingParams(
            temperature=0.7,
            top_p=0.9,
            max_tokens=100
        )

        # 3. Define the prompt
        prompt = f"Explain the concept of quantum entanglement in one simple sentence. Question: {question}"
        print(f"\nSending prompt: '{prompt}'")

        # 4. Perform the inference (ask the question)
        print("\n--- Generating response ---")
        outputs = llm.generate(prompt, sampling_params)

        # 5. Process and print the results
        for output in outputs:
            prompt_text = output.prompt
            generated_text = output.outputs[0].text
            
            print("\n=========================================")
            print(f"Prompt: {prompt_text.strip()}")
            print(f"Response: {generated_text.strip()}")
            print("=========================================")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("\nNOTE: Ensure you have a valid model name and sufficient GPU memory.")


if __name__ == "__main__":
    # IMPORTANT: Replace this with a model that you have access to
    # For demonstration, we use a common placeholder.
    MODEL_TO_USE = "mistralai/Mistral-7B-Instruct-v0.2" 
    
    simple_query = "What is the capital of France?"
    
    ask_simple_question(MODEL_TO_USE, simple_query)