import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui



def Betamount1(driver):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
                                                                     '((//div[contains(text(),"Markets")]/following::div)[3]/descendant::div)[2]')))  # waiting till the element found
    Bet_Markets = driver.find_element(By.XPATH,
                                      '((//div[contains(text(),"Markets")]/following::div)[3]/descendant::div)[2]').text
    #print("Bet_Markets =" + Bet_Markets)
    Bet_odds = driver.find_element(By.XPATH,
                                   '((//div[contains(text(),"Markets")]/following::div)[3]/descendant::div)[3]').text
    #print("Bet_odds =" + Bet_odds)
    Bet_Stakes1 = driver.find_element(By.XPATH,
                                      '((//div[contains(text(),"Markets")]/following::div)[3]/descendant::div)[4]').text
    print("Bet_amount =" + Bet_Stakes1)
    Bet_stakes1 = float(Bet_Stakes1)
    return Bet_stakes1


