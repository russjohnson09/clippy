import os
import glob

def list_local_models(directory_path: str):
    """
    Scans a specified directory path and lists directories that appear
    to be model checkpoints (based on common file structure).

    Args:
        directory_path (str): The path to the directory to scan (e.g., your local model cache).
    """
    print(f"--- Scanning directory: {directory_path} ---")
    
    if not os.path.exists(directory_path):
        print(f"Error: Directory not found at '{directory_path}'")
        return

    # Use glob to find all directories within the path
    model_directories = [
        d for d in os.listdir(directory_path) 
        if os.path.isdir(os.path.join(directory_path, d))
    ]

    if not model_directories:
        print("No subdirectories found in the specified path.")
        return

    print(f"\nFound {len(model_directories)} potential model directories:")
    print("--------------------------------------------------")

    found_models = []
    
    # Check each directory to see if it contains common model files
    for model_dir in model_directories:
        full_path = os.path.join(directory_path, model_dir)
        
        # Check for key model files (e.g., config.json, model.safetensors)
        if os.path.exists(os.path.join(full_path, "config.json")) or \
           os.path.exists(os.path.join(full_path, "model.safetensors")) or \
           os.path.exists(os.path.join(full_path, "pytorch_model.bin")):
            
            found_models.append(model_dir)

    if found_models:
        print("\n✅ Models identified (based on file presence):")
        for model in found_models:
            print(f"- {model}")
    else:
        print("\nNo directories containing common model files were found.")


if __name__ == "__main__":
    # ==========================================================================
    # IMPORTANT: CONFIGURE THIS PATH
    # ==========================================================================
    
    # Example 1: Scan the standard Hugging Face cache (where downloaded models often reside)
    # On Linux/macOS, this is often ~/.cache/huggingface/hub
    # On Windows, this might be something like C:\Users\YourUser\.cache\huggingface\hub
    LOCAL_CACHE_PATH = os.path.expanduser("~/.cache/huggingface/hub")
    
    # Example 2: Scan a custom directory where you manually saved models
    # LOCAL_CACHE_PATH = "/path/to/your/local/models"
    
    list_local_models(LOCAL_CACHE_PATH)