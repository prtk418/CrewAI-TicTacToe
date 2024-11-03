from pathlib import Path
from dotenv import load_dotenv

# Get the absolute path to the .env file (will be in project root)
env_path = Path(__file__).parent.parent.parent / '.env'

# Load environment variables
if env_path.exists():
    load_dotenv(dotenv_path=env_path, override=True)  # override=True forces it to take precedence
else:
    print(f"Warning: No .env file found at {env_path}")
