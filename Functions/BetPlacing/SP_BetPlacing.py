import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui

SP = "(//div[contains(text(),'SP')])[1]"
one = "(//div[contains(text(),'140.0')])[1]"
two = "(//div[contains(text(),'140.0')])[2]"
three = "(//div[contains(text(),'140.0')])[3]"
four = "(//div[contains(text(),'140.0')])[4]"
five = "(//div[contains(text(),'140.0')])[5]"
six = "(//div[contains(text(),'140.0')])[7]"
seven = "(//div[contains(text(),'140.0')])[8]"
eight = "(//div[contains(text(),'140.0')])[9]"
nine = "(//div[contains(text(),'140.0')])[10]"
zero = "(//div[contains(text(),'140.0')])[11]"
All = "(//div[contains(text(),'140.0')])[6]"

def condformBet(driver):
    WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "(//tr/button)[1]")))
    driver.find_element(By.XPATH, "(//tr/button)[1]").click()
    driver.find_element(By.XPATH, '//button[contains(text(),"Place bets")]').click()

def SPOne_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, SP).click()
    driver.find_element(By.XPATH, one).click()
    condformBet(driver)

def SPtwo_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, SP).click()
    driver.find_element(By.XPATH, two).click()
    condformBet(driver)

def SPthree_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, SP).click()
    driver.find_element(By.XPATH, three).click()
    condformBet(driver)

def SPfour_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, SP).click()
    driver.find_element(By.XPATH, four).click()
    condformBet(driver)

def SPfive_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, SP).click()
    driver.find_element(By.XPATH, five).click()
    condformBet(driver)

def SPsix_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, SP).click()
    driver.find_element(By.XPATH, six).click()
    condformBet(driver)

def SPseven_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, SP).click()
    driver.find_element(By.XPATH, seven).click()
    condformBet(driver)

def SPeight_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, SP).click()
    driver.find_element(By.XPATH, eight).click()
    condformBet(driver)

def SPnine_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, SP).click()
    driver.find_element(By.XPATH, nine).click()
    condformBet(driver)

def SPzero_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, SP).click()
    driver.find_element(By.XPATH, zero).click()
    condformBet(driver)

def SPAll_bet(driver):
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "timer-container")))
    driver.find_element(By.XPATH, SP).click()
    driver.find_element(By.XPATH, All).click()
    condformBet(driver)