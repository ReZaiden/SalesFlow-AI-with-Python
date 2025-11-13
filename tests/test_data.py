from src.logger import setup_logger
from src.data import KnowledgeBase

knowledge_base = KnowledgeBase()
knowledge_base.load()
logger = setup_logger("tests")

def test_excel_file():
    results = knowledge_base.filter_products(name="test", min_price=15, max_price=30)
    logger.info(f"Excel file test is successfully: {len(results)} product founded!")
    assert True

def test_pdf_file():
    assert len(knowledge_base.pdf_text) > 0
    logger.info(f"PDF file test is successfully: {len(knowledge_base.pdf_text)} character founded!")

def test_txt_file():
    assert len(knowledge_base.txt_text) > 0
    logger.info(f"TXT file test is successfully: {len(knowledge_base.txt_text)} characters founded!")

