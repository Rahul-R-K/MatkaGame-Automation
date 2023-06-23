import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui

CommonSP = "(//div[contains(text(),'Common SP')])[1]"
one = "(//div[contains(text(),'140.0')])[1]"
two = "(//div[contains(text(),'140.0')])[2]"
three = "(//div[contains(text(),'140.0')])[3]"
four = "(//div[contains(text(),'140.0')])[4]"
five = "(//div[contains(text(),'140.0')])[5]"
six = "(//div[contains(text(),'140.0')])[6]"
seven = "(//div[contains(text(),'140.0')])[7]"
eight = "(//div[contains(text(),'140.0')])[8]"
nine = "(//div[contains(text(),'140.0')])[9]"
zero = "(//div[contains(text(),'140.0')])[10]"

def condformBet(driver):
    WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "(//tr/button)[1]")))
    driver.find_element(By.XPATH, "(//tr/button)[1]").click()
    driver.find_element(By.XPATH, '//button[contains(text(),"Place bets")]').click()

def CSPOne_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, CommonSP).click()
    driver.find_element(By.XPATH, one).click()
    condformBet(driver)

def CSPtwo_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, CommonSP).click()
    driver.find_element(By.XPATH, two).click()
    condformBet(driver)

def CSPthree_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, CommonSP).click()
    driver.find_element(By.XPATH, three).click()
    condformBet(driver)

def CSPfour_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, CommonSP).click()
    driver.find_element(By.XPATH, four).click()
    condformBet(driver)

def CSPfive_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, CommonSP).click()
    driver.find_element(By.XPATH, five).click()
    condformBet(driver)

def CSPsix_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, CommonSP).click()
    driver.find_element(By.XPATH, six).click()
    condformBet(driver)

def CSPseven_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, CommonSP).click()
    driver.find_element(By.XPATH, seven).click()
    condformBet(driver)

def CSPeight_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, CommonSP).click()
    driver.find_element(By.XPATH, eight).click()
    condformBet(driver)

def CSPnine_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, CommonSP).click()
    driver.find_element(By.XPATH, nine).click()
    condformBet(driver)

def CSPzero_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, CommonSP).click()
    driver.find_element(By.XPATH, zero).click()
    condformBet(driver)

