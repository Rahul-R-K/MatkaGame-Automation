#(//div[contains(text(),'Trio')])[2]
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui

TRIO1 = "(//div[contains(text(),'Trio')])[1]"
Trio = "(//div[contains(text(),'Trio')])[2]"


def condformBet(driver):
    WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "(//tr/button)[1]")))
    driver.find_element(By.XPATH, "(//tr/button)[1]").click()
    driver.find_element(By.XPATH, '//button[contains(text(),"Place bets")]').click()

def TRIO_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, TRIO1).click()
    driver.find_element(By.XPATH, Trio).click()
    condformBet(driver)

