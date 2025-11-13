import pytest
from src.config import Config
from src.logger import setup_logger

logger = setup_logger("tests")

def test_env_vars():
    assert Config.AI_API_KEY is not None
    assert Config.NTFY_TOPIC is not None
    logger.info('Test .env variables is successfully!')