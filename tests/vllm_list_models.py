from huggingface_hub import list_models
import os

def fetch_hf_model_list():
    """
    Fetches a list of models available on the Hugging Face Hub.
    """
    print("--- Fetching list of models from Hugging Face Hub ---")
    
    try:
        # list_models() fetches a list of models based on various filters
        model_list = list_models()
        
        print(f"\nSuccessfully retrieved {len(model_list)} models.\n")
        
        # Print the first 10 models for a concise view
        print("--- Top 10 Available Models ---")
        for i, model in enumerate(model_list[:10]):
            print(f"{i+1}. Name: {model.model_name}")
            print(f"   ID: {model.model_id}")
            print(f"   Likes: {model.downloads}")
            print("-" * 20)
            
        print("\nTo use these models with vLLM, you would replace 'model_name' in the LLM() constructor.")

    except Exception as e:
        print(f"An error occurred while fetching the model list: {e}")

if __name__ == "__main__":
    fetch_hf_model_list()