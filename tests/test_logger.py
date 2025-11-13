import pytest
from src.logger import setup_logger
import logging

def test_logger():
    logger = setup_logger("tests")
    assert type(logger) == logging.Logger
    logger.info('Test logger is successfully!')
