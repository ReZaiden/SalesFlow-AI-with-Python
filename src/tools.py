import requests
from .config import Config
from .logger import setup_logger

logger = setup_logger("tools")

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