from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_application():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("http://localhost:8000/docs")
        # Vérifiez "Swagger UI" ou "Churn" au lieu de "FastAPI"
        assert "Swagger UI" in driver.title 
    finally:
        driver.quit()
