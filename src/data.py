from pathlib import Path
import pandas as pd
from .config import Config
from .logger import setup_logger
from typing import List, Dict
from pypdf import PdfReader

logger = setup_logger("knowledge")

class KnowledgeBase:
    """Handles loading and querying product knowledge from multiple sources"""

    def __init__(self):
        self.config = Config.get()["sources"]
        self.products: List[Dict[str, str]] = []
        self.pdf_text: str = ""
        self.txt_text: str = ""
        self.loaded = False

    def load(self) -> None:
        """Load all knowledge sources"""
        if self.loaded:
            return

        logger.info("Loading knowledge sources...")

        # 1. Load Excel
        if self.config.get("excel_file"):
            self._load_excel()

        # 2. Load PDF
        if self.config.get("pdf_file"):
            self._load_pdf()

        # 3. Load TXT
        if self.config.get("txt_file"):
            self._load_txt()

        self.loaded = True
        logger.info(f"Knowledge sources loaded successfully: {len(self.products)} products")

    def _load_excel(self) -> None:
        """Load excel file"""
        path = Path(self.config.get("excel_file"))
        if not path.exists() or not path.is_file():
            logger.warning("Excel file not found")
            return

        try:
            df = pd.read_excel(path)

            # Normalize column names
            df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

            self.products = df.to_dict(orient="records")

            logger.info(f"Excel file loaded successfully: {len(df)} rows")
        except Exception as e:
            logger.error(f"Failed to load excel file: {e}")

    def filter_products(self, name: str=None, min_price: float=None, max_price: float=None) -> List[Dict[str, str]]:
        """Find a product in the knowledge sources with name or min and max price"""
        self.load()
        results = self.products
        if name is not None:
            results = [product for product in results if name.lower() in product["name"].lower()]
        if min_price is not None:
            results = [product for product in results if min_price < float(product["price"])]
        if max_price is not None:
            results = [product for product in results if max_price > float(product["price"])]

        return results

    def get_all_products(self) -> List[Dict[str, str]]:
        """Get all products"""
        self.load()
        return self.products

    def _load_pdf(self) -> None:
        """Load pdf file"""
        path = Path(self.config.get("pdf_file"))
        if not path.exists() or not path.is_file():
            logger.warning("Pdf file not found")
            return

        try:
            reader = PdfReader(path)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

            self.pdf_text = text
            logger.info(f"Pdf file loaded successfully: {len(text)} characters")
        except Exception as e:
            logger.error(f"Failed to load pdf file: {e}")

    def _load_txt(self) -> None:
        """Load txt file"""
        path = Path(self.config.get("txt_file"))
        if not path.exists() or not path.is_file():
            logger.warning("Text file not found")
            return

        try:
            with open(path, "r", encoding="utf-8") as f:
                self.txt_text = f.read()
            logger.info(f"Text file loaded successfully: {len(self.txt_text)} characters")
        except Exception as e:
            logger.error(f"Failed to load txt file: {e}")



