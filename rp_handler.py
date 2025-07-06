import runpod
import time  
import os
from huggingface_hub import login, snapshot_download
import torch

def handler(event):
    HUGGING_FACE_TOKEN = os.getenv('HUGGING_FACE_TOKEN')

    login(HUGGING_FACE_TOKEN)
    
    print(f"Worker Start")
    # input = event['input']
    
    
    # prompt = input.get('prompt')  
    # seconds = input.get('seconds', 0)  

    # print(f"Received prompt: {prompt}")
    # print(f"Sleeping for {seconds} seconds...")
    
    # # Replace the sleep code with your Python function to generate images, text, or run any machine learning workload
    # time.sleep(seconds)  
    
    # return prompt 

    return "Hello, World!"

if __name__ == '__main__':
    runpod.serverless.start({'handler': handler })
