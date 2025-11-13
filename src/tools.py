import requests
from .config import Config
from .logger import setup_logger
from .data import KnowledgeBase
from typing import List, Dict

logger = setup_logger("tools")

knowledge_base = KnowledgeBase()
knowledge_base.load()

# === Notification Tool ===
def send_notification(title: str, message: str) -> bool:
    """
        Send notification via ntfy.sh
        Returns True if successful
    """
    try:
        url = f"{Config.NTFY_SERVER}/{Config.NTFY_TOPIC}"
        response = requests.post(url, data=message)
        requests.post(url, data=message, headers={"Title": title, "Tags": "loudspeaker"})

        if response.status_code == 200:
            logger.info(f"notification sent: {title} - {message}")
            return True
        else:
            logger.info(f"notification failed: {title} - {message}")
            return False
    except Exception as e:
        logger.info(f"notification failed {title} - {message}. error: {e}")
        return False

# === Filter Product Tool ===
def filter_products(name: str = None, min_price: float = None, max_price: float = None) -> List[Dict[str, str]]:
    """Find a product in the knowledge sources with name or min and max price"""
    results = knowledge_base.filter_products(name, min_price, max_price)
    logger.info(f"Found {len(results)} products in knowledge source")
    return results