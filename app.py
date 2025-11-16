from src.logger import setup_logger
from src.config import Config
from src.ui import Interface

logger = setup_logger("app")
server_config = Config().get()['server']

if __name__ == '__main__':
    logger.info("Luch server is started...")
    try:
        Interface.launch(server_name=server_config["name"], server_port=server_config["port"])
    except Exception as e:
        logger.error(f"Error in launching server: {e}")
