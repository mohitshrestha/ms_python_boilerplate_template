"""
Centralized configuration and paths for the project.
Handles environment variables, data directories, and credentials paths.
"""

from pathlib import Path
from dotenv import load_dotenv

# -------------------------
# Load environment variables
# -------------------------
load_dotenv()  # Loads variables from .env file at project root

# -------------------------
# Base directories
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent  # Root of project
DATA_DIR = BASE_DIR / "data"                        # Main data folder
RAW_DIR = DATA_DIR / "raw"                          # Raw/unprocessed data
PROCESSED_DIR = DATA_DIR / "processed"              # Processed/cleaned data

# Credentials directory (gitignored for sensitive info)
CREDENTIALS_DIR = BASE_DIR / "config" / "credentials"

# -------------------------
# Helper functions
# -------------------------
def get_data_path(file_name: str, processed: bool = False) -> Path:
    """
    Get the full path to a data file.

    Args:
        file_name (str): Name of the file.
        processed (bool): If True, returns path in processed folder. Default is False (raw).

    Returns:
        Path: Full path to the file.
    """
    folder = PROCESSED_DIR if processed else RAW_DIR
    folder.mkdir(parents=True, exist_ok=True)  # Ensure folder exists
    return folder / file_name

def get_credential_path(file_name: str) -> Path:
    """
    Get the full path to a credentials file.

    Args:
        file_name (str): Name of the credential file.

    Returns:
        Path: Full path to the credential file.
    """
    CREDENTIALS_DIR.mkdir(parents=True, exist_ok=True)  # Ensure folder exists
    return CREDENTIALS_DIR / file_name
