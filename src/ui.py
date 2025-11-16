from .logger import setup_logger
from .config import Config
from .agent import chat
from gradio import ChatInterface

logger = setup_logger("ui")

ui_config = Config().get()['ui']

Interface = ChatInterface(chat,
              type='messages',
              title=ui_config['title'],
              description=ui_config['description'],
              theme=ui_config['theme'],
              save_history=ui_config['save_history'],
              )

logger.info("Setup UI is complete")
