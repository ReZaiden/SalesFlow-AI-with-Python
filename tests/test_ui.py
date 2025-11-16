import pytest
from src.logger import setup_logger
from src.ui import Interface
import threading
import time

import requests

logger = setup_logger("tests")

server_name = "localhost"
server_port = 8000
global checked, check_result
checked = False
check_result = None

def run_ui():
    Interface.launch(server_name=server_name, server_port=server_port)

def check_ui():
    time.sleep(5)
    response = requests.get(f"http://{server_name}:{server_port}/")
    global checked, check_result
    checked = True
    check_result = response.status_code == 200

def test_ui():
    run_ui_thread = threading.Thread(target=run_ui)
    check_ui_thread = threading.Thread(target=check_ui)
    run_ui_thread.start()
    check_ui_thread.start()
    global checked, check_result
    while not checked:
        time.sleep(1)
    assert check_result == True
    logger.info("Test ui is successfully!")
