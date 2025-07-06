import os
from huggingface_hub import login, snapshot_download

HUGGING_FACE_TOKEN = os.getenv('HUGGING_FACE_TOKEN', '')

login(HUGGING_FACE_TOKEN)

MODEL_DIR = "/model"
os.makedirs(MODEL_DIR, exist_ok=True)

print("Downloading black-forest-labs/FLUX.1-Kontext-dev model...")
snapshot_download(
    repo_id="black-forest-labs/FLUX.1-Kontext-dev",
    local_dir=MODEL_DIR,
    token=HUGGING_FACE_TOKEN,
    ignore_patterns=["*.md", "*.txt", "*.pdf"]
)

print("Model downloaded successfully!") 