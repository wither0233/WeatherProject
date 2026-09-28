from  pathlib import Path

def get_config():
    PROJECT_ROOT = Path(__file__).resolve().parent
    DATA_ROOT = PROJECT_ROOT / 'raw'
    return DATA_ROOT