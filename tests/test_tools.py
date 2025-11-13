import pytest

from src.logger import setup_logger
from src.tools import send_notification, filter_products

logger = setup_logger("tests")

def test_notification():
    notification = send_notification("test", "this is a test notification")
    assert notification
    logger.info("Notification sending is successfully!")

def test_filter_products():
    results = filter_products(name="test", min_price=15, max_price=30)
    assert len(results) > 0
    logger.info("Filtering products test is successfully!")
