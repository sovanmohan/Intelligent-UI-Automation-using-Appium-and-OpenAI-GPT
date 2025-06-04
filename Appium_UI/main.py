from config import setup_llm
from appium_utils import setup_driver, perform_action, scroll_and_tap
from ui_parser import get_page_source
from interface import run_ui

if __name__ == "__main__":
    selected_llm, gemini_model = setup_llm()
    driver, _ = setup_driver()
    run_ui(driver, selected_llm, gemini_model, perform_action, get_page_source)
