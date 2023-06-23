import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui



def BetStake(driver):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
                                                                     '((//div[contains(text(),"Markets")]/following::div)[3]/descendant::div)[2]')))  # waiting till the element found
    Bet_Markets = driver.find_element(By.XPATH,
                                      '((//div[contains(text(),"Markets")]/following::div)[3]/descendant::div)[2]').text
    #print("Bet_Markets =" + Bet_Markets)
    Bet_odds = driver.find_element(By.XPATH,
                                   '((//div[contains(text(),"Markets")]/following::div)[3]/descendant::div)[3]').text
    print("Bet_odds =" + Bet_odds)
    Bet_Stakes1 = driver.find_element(By.XPATH,
                                      '((//div[contains(text(),"Markets")]/following::div)[3]/descendant::div)[4]').text
    #print("Bet_Stakes =" + Bet_Stakes1)
    Bet_odds = float(Bet_odds)
    return Bet_odds


def BetStake2(driver):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[5]/descendant::div)[1]")))
    Bet_Markets2 = driver.find_element(By.XPATH,
                                       "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[5]/descendant::div)[1]").text
    print("Bet_Markets2 =" + Bet_Markets2)

    Bet_Odds2 = driver.find_element(By.XPATH,
                                    "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[5]/descendant::div)[2]").text
    print("Bet_odds2 =" + Bet_Odds2)

    Bet_Stakes2 = driver.find_element(By.XPATH,
                                      "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[5]/descendant::div)[3]").text
    print("Bet_Stakes2 =" + Bet_Stakes2)
    Bet_Stakes2 = int(Bet_Stakes2)
    return Bet_Stakes2


def BetStake3(driver):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[9]/descendant::div)[1]")))
    Bet_Markets3 = driver.find_element(By.XPATH,
                                       "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[9]/descendant::div)[1]").text
    print("Bet_Markets3 =" + Bet_Markets3)

    Bet_Odds3 = driver.find_element(By.XPATH,
                                    "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[9]/descendant::div)[2]").text
    print("Bet_Odds3 =" + Bet_Odds3)

    Bet_Stakes3 = driver.find_element(By.XPATH,
                                      "(((//div[contains(text(),'Markets')]/following::div)[3]/descendant::div)[9]/descendant::div)[3]").text
    print("Bet_Stake3 =" + Bet_Stakes3)
    Bet_Stakes3 = int(Bet_Stakes3)
    return Bet_Stakes3
