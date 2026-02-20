from huggingface_hub import snapshot_download
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

snapshot_download(
    repo_id="saveerjain/marchmadness",
    repo_type="dataset",
    local_dir=DATA_DIR,
)

print(f"Data downloaded to {DATA_DIR}")
