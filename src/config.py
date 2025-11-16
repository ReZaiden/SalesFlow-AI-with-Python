import os
from pathlib import Path
import yaml
from dotenv import load_dotenv
from .logger import setup_logger

# Setup logger
logger = setup_logger("config")

# Load environment variables
load_dotenv(override=True)

# Project root
ROOT_DIR = Path(__file__).parent.parent

class Config:
    """Central configuration manager"""

    # AI config
    AI_API_KEY = os.getenv("AI_API_KEY", None)
    AI_BASE_URL = os.getenv("AI_BASE_URL", None)
    AI_MODEL = os.getenv("AI_MODEL", None)

    # ntfy
    NTFY_TOPIC = os.getenv("NTFY_TOPIC", None)
    NTFY_SERVER = os.getenv("NTFY_SERVER", None)

    # Load YAML config
    @staticmethod
    def load_yaml():
        config_path = ROOT_DIR / "config.yaml"
        if not config_path.exists() or not config_path.is_file():
            raise FileNotFoundError(f"config.yaml file not found in: {config_path}")

        with open(config_path, "r", encoding='utf-8') as f:
            logger.info(f"Loading config from {config_path}")
            return yaml.safe_load(f)

    @staticmethod
    def get():
        return Config.load_yaml()

# Validate required env variables
if not Config.AI_API_KEY:
    logger.error("AI_API_KEY not set")
    raise ValueError("AI_API_KEY not set")
if not Config.NTFY_TOPIC:
    logger.error("NTFY_TOPIC not set")
    raise ValueError("NTFY_TOPIC not set")

logger.info("Config loaded successfully!")
