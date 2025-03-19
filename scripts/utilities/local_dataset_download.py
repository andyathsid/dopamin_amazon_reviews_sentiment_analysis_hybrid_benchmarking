import kagglehub
from pathlib import Path
import shutil

def download_dataset():
    """Download dataset dari kaggle dan simpan di folder data"""
    project_root = Path(__file__).resolve().parent.parent.parent
    
    data_dir = project_root / "data"
    downloaded_path = Path(kagglehub.dataset_download("kritanjalijain/amazon-reviews"))
    
    data_dir.mkdir(parents=True, exist_ok=True)

    for file_name in ["train.csv", "test.csv"]:
        src = downloaded_path / file_name
        dest = data_dir / file_name
        
        if not src.exists():
            raise FileNotFoundError(f"Source file {file_name} tidak ditemukan di dataset")
            
        if not dest.exists() or (src.stat().st_size != dest.stat().st_size):
            shutil.copy(src, dest)
            print(f"{file_name} di-copy ke {dest}")
        else:
            print(f"{file_name} sudah ada")
            
    print(f"Lokasi cache (kalo dihapus bakal redownload terus): {downloaded_path}")