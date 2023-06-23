import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui


single = "(//div[contains(text(),'Single')])"
one = "(//div[contains(text(),'9.5')])[1]"
two = "(//div[contains(text(),'9.5')])[2]"
three = "(//div[contains(text(),'9.5')])[3]"
four = "(//div[contains(text(),'9.5')])[4]"
five = "(//div[contains(text(),'9.5')])[5]"
six = "(//div[contains(text(),'9.5')])[6]"
seven = "(//div[contains(text(),'9.5')])[7]"
eight = "(//div[contains(text(),'9.5')])[8]"
nine = "(//div[contains(text(),'9.5')])[9]"
zero = "(//div[contains(text(),'9.5')])[10]"
Low = "(//div[contains(text(),'Low | 1.95')])"
High = "(//div[contains(text(),'High | 1.95')])"
Odd = "(//div[contains(text(),'Odd | 1.95')])"
Even = "(//div[contains(text(),'Even | 1.95')])"

def condformBet(driver):
    WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "(//tr/button)[1]")))
    driver.find_element(By.XPATH, "(//tr/button)[1]").click()
    driver.find_element(By.XPATH, '//button[contains(text(),"Place bets")]').click()

def One_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, single).click()
    driver.find_element(By.XPATH, one).click()
    condformBet(driver)

def two_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, single).click()
    driver.find_element(By.XPATH, two).click()
    condformBet(driver)

def three_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, single).click()
    driver.find_element(By.XPATH, three).click()
    condformBet(driver)

def four_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, single).click()
    driver.find_element(By.XPATH, four).click()
    condformBet(driver)

def five_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, single).click()
    driver.find_element(By.XPATH, five).click()
    condformBet(driver)

def six_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, single).click()
    driver.find_element(By.XPATH, six).click()
    condformBet(driver)

def seven_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, single).click()
    driver.find_element(By.XPATH, seven).click()
    condformBet(driver)

def eight_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, single).click()
    driver.find_element(By.XPATH, eight).click()
    condformBet(driver)

def nine_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, single).click()
    driver.find_element(By.XPATH, nine).click()
    condformBet(driver)

def zero_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, single).click()
    driver.find_element(By.XPATH, zero).click()
    condformBet(driver)

def Low_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, single).click()
    driver.find_element(By.XPATH, Low).click()
    condformBet(driver)

def High_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, single).click()
    driver.find_element(By.XPATH, High).click()
    condformBet(driver)

def Odd_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, single).click()
    driver.find_element(By.XPATH, Odd).click()
    condformBet(driver)

def Even_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, single).click()
    driver.find_element(By.XPATH, Even).click()
    condformBet(driver)
