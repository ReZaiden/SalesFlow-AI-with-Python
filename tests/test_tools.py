import pytest
from src.logger import setup_logger
from src.tools import send_notification

logger = setup_logger("tests")

def test_notification():
    notification = send_notification("test", "this is a test notification")
    assert notification
    logger.info("Notification sending is successfully!")
