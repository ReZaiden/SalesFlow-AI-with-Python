import pytest
from src.logger import setup_logger
from src.agent import chat

logger = setup_logger("tests")

def test_chat():
    result = chat("If you got my message, just return the number 1.", [])
    assert int(result) == 1
    logger.info("Test chat with agent is successfully!")

def test_call_tools_send_notification():
    result = chat("This is my number:09123456789 if you passed it to the administrator correctly, return the number 1, otherwise the number 0. Just return the number 1 or 0.", [])
    assert int(result) == 1
    logger.info("Test send_notification tool with agent is successfully!")

def test_call_tools_filter_products():
    result = chat("Find products with the highest price of 10000000000 for me. Just return me the number of products you found without any additional information. Just return the number of products", [])
    assert int(result) > 0
    logger.info("Test filter_products tool with agent is successfully!")
