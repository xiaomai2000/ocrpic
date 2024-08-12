from transformers import AutoModelForCausalLM, AutoTokenizer
import os

import torch
print("torch.cuda.is_available(): ", torch.cuda.is_available())


class llm_service:

    def __init__(self, model_name="Qwen/Qwen2-0.5B", local_dir="models/Qwen2-0.5B"):
        self.model_name = model_name
        self.local_dir = local_dir
        self.model = None
        self.tokenizer = None
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def init_service(self):
        if not os.path.exists(self.local_dir):
            print(f"local_dir {self.local_dir} not exists.")
            os.makedirs(self.local_dir)
        
        tokenizer_path = os.path.join(self.local_dir, "tokenizer.json")
        print(f"tokenizer_path = {tokenizer_path}")

        # If model has been downloaded, skip the internet connect and load local model directly. Otherwise, connect to Huggingface to download
        if not os.path.exists(tokenizer_path):
            print("Model not found locally. Downloading from Hugging Face...")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name, device_map="auto")
        else:
            print("Model found locally. Loading from local directory...")
            self.tokenizer = AutoTokenizer.from_pretrained(self.local_dir)
            self.model = AutoModelForCausalLM.from_pretrained(self.local_dir, device_map="auto")
        
        # Move model to the device (GPU if available)
        #self.model.to(self.device)

    def query_service(self, query_str):
        if self.model is None or self.tokenizer is None:
            raise ValueError("Error. Model is not initialized. Please call init_llm_service() first.")
            
        prompt = query_str
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
        
        text = self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
        )
        
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.device)

        generated_ids = self.model.generate(
            model_inputs.input_ids,
            max_new_tokens=100
        )
        
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]    
        return response


import torch
print("torch.cuda.is_available(): ", torch.cuda.is_available())


# Example usage
if __name__ == "__main__":
    service = llm_service()
    service.init_service()
    
    #query = "What is the capital of France? "
    query = 'Write a SQL to get the 1st record from table xyz'
    response = service.query_service(query)
    print("Response:", response)
