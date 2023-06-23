import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui

id1 = "//span[@id='Matka-Cards-0']"
id2 = "//span[@id='Matka-Cards-1']"
id3 = "//span[@id='Matka-Cards-2']"
Value = "//span[@class='ng-tns-c105-11 total_val']"


def getresult(driver):
    wait = WebDriverWait(driver, 100)
    elements = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".animation_blink")))
    element = driver.find_element(By.XPATH, Value)
    value = int(element.get_attribute("innerHTML"))
    print(f'Value = {value}')
    return value


def SP_Result(driver):
    global order
    order = {'2': 2,
             '3': 3,
             '4': 4,
             '5': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             '10': 10,
             'J': 11,
             'Q': 12,
             'K': 13,
             'A': 1}
    WebDriverWait(driver, 100).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".animation_blink")))
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id1)))
    span_element = driver.find_element(By.XPATH, id1)
    card1text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card1 = card1text.split(" ")
    print(f'Card1 = {card1[0]}')
    player = card1[0]
    card11 = order[player]
    Card1 = int(card11)

    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id2)))
    span_element = driver.find_element(By.XPATH, id2)
    card2text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card2 = card2text.split(" ")
    print(f'Card1 = {card2[0]}')

    player = card2[0]
    card22 = order[player]
    Card2 = int(card22)

    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id3)))
    span_element = driver.find_element(By.XPATH, id3)
    card3text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card3 = card3text.split(" ")
    print(f'Card1 = {card3[0]}')

    player = card3[0]
    card33 = order[player]
    Card3 = int(card33)

    if Card1 < Card2 < Card3 and Card1 < Card3 and Card1 != card2 and Card1 != Card3 and Card2 != Card3:
        element = driver.find_element(By.XPATH, Value)
        value = int(element.get_attribute("innerHTML"))
        print(f'Value = {value}  ')
        return "Case1"
    elif Card1 != card2 and Card1 != Card3 and Card2 != Card3:
        element = driver.find_element(By.XPATH, Value)
        value = int(element.get_attribute("innerHTML"))
        print(f'Value = {value}  ')
        return "Case2"
    elif Card1 == card2 or Card1 == Card3 or Card2 == Card3:
        print(f'Not in SP')
        return "Case3"


def TRIO_REsult(driver):
    global order
    order = {'2': 2,
             '3': 3,
             '4': 4,
             '5': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             '10': 10,
             'J': 11,
             'Q': 12,
             'K': 13,
             'A': 1}
    WebDriverWait(driver, 100).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".animation_blink")))
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id1)))
    span_element = driver.find_element(By.XPATH, id1)
    card1text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card1 = card1text.split(" ")
    print(f'Card1 = {card1[0]}')
    player = card1[0]
    card11 = order[player]
    Card1 = int(card11)

    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id2)))
    span_element = driver.find_element(By.XPATH, id2)
    card2text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card2 = card2text.split(" ")
    print(f'Card1 = {card2[0]}')

    player = card2[0]
    card22 = order[player]
    Card2 = int(card22)

    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id3)))
    span_element = driver.find_element(By.XPATH, id3)
    card3text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card3 = card3text.split(" ")
    print(f'Card1 = {card3[0]}')

    player = card3[0]
    card33 = order[player]
    Card3 = int(card33)

    if Card1 == card2 and Card1 == Card3 and Card2 == Card3:
        element = driver.find_element(By.XPATH, Value)
        value = int(element.get_attribute("innerHTML"))
        print(f'Value = {value}  ')
        return "Case1"
    elif Card1 != card2 and Card1 != Card3 and Card2 != Card3:
        element = driver.find_element(By.XPATH, Value)
        value = int(element.get_attribute("innerHTML"))
        print(f'Value = {value}  ')
        return "Case2"


def DP_Result(driver):
    global order
    order = {'2': 2,
             '3': 3,
             '4': 4,
             '5': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             '10': 10,
             'J': 11,
             'Q': 12,
             'K': 13,
             'A': 1}
    WebDriverWait(driver, 100).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".animation_blink")))
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id1)))
    span_element = driver.find_element(By.XPATH, id1)
    card1text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card1 = card1text.split(" ")
    print(f'Card1 = {card1[0]}')
    player = card1[0]
    card11 = order[player]
    Card1 = int(card11)

    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id2)))
    span_element = driver.find_element(By.XPATH, id2)
    card2text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card2 = card2text.split(" ")
    print(f'Card1 = {card2[0]}')

    player = card2[0]
    card22 = order[player]
    Card2 = int(card22)

    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id3)))
    span_element = driver.find_element(By.XPATH, id3)
    card3text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card3 = card3text.split(" ")
    print(f'Card1 = {card3[0]}')

    player = card3[0]
    card33 = order[player]
    Card3 = int(card33)

    if Card1 == Card2 < Card3 or Card3 == Card1 < Card2 and Card1 == card2 or Card1 == Card3 or Card2 == Card3:
        element = driver.find_element(By.XPATH, Value)
        value = int(element.get_attribute("innerHTML"))
        print(f'Value = {value}  ')
        return "Case1"
    elif Card1 == card2 and Card1 == Card3 and Card2 == Card3:
        element = driver.find_element(By.XPATH, Value)
        value = int(element.get_attribute("innerHTML"))
        print(f'Value = {value}  ')
        return "Case2"
    else:
        return "Case3"


def CommonSP_Result(driver):
    global order
    order = {'2': 2,
             '3': 3,
             '4': 4,
             '5': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             '10': 10,
             'J': 11,
             'Q': 12,
             'K': 13,
             'A': 1}
    WebDriverWait(driver, 100).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".animation_blink")))
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id1)))
    span_element = driver.find_element(By.XPATH, id1)
    card1text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card1 = card1text.split(" ")
    print(f'Card1 = {card1[0]}')
    player = card1[0]
    card11 = order[player]
    Card1 = int(card11)

    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id2)))
    span_element = driver.find_element(By.XPATH, id2)
    card2text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card2 = card2text.split(" ")
    print(f'Card1 = {card2[0]}')

    player = card2[0]
    card22 = order[player]
    Card2 = int(card22)

    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id3)))
    span_element = driver.find_element(By.XPATH, id3)
    card3text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card3 = card3text.split(" ")
    print(f'Card1 = {card3[0]}')

    player = card3[0]
    card33 = order[player]
    Card3 = int(card33)

    Cards_Value = [Card1, Card2, Card3]

    if Card1 != card2 and Card1 != Card3 and Card2 != Card3:
        element = driver.find_element(By.XPATH, Value)
        value = int(element.get_attribute("innerHTML"))
        print(f'Value = {value}  ')
        return "Case1"
    else:
        return "Case2"


def CommonDP_Result(driver):
    global order
    order = {'2': 2,
             '3': 3,
             '4': 4,
             '5': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             '10': 10,
             'J': 11,
             'Q': 12,
             'K': 13,
             'A': 1}
    WebDriverWait(driver, 100).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".animation_blink")))
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id1)))
    span_element = driver.find_element(By.XPATH, id1)
    card1text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card1 = card1text.split(" ")
    print(f'Card1 = {card1[0]}')
    player = card1[0]
    card11 = order[player]
    Card1 = int(card11)

    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id2)))
    span_element = driver.find_element(By.XPATH, id2)
    card2text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card2 = card2text.split(" ")
    print(f'Card1 = {card2[0]}')

    player = card2[0]
    card22 = order[player]
    Card2 = int(card22)

    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id3)))
    span_element = driver.find_element(By.XPATH, id3)
    card3text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card3 = card3text.split(" ")
    print(f'Card1 = {card3[0]}')

    player = card3[0]
    card33 = order[player]
    Card3 = int(card33)

    Cards_Value = [Card1, Card2, Card3]

    if Card1 == card2 or Card1 == Card3 or Card2 == Card3:
        element = driver.find_element(By.XPATH, Value)
        value = int(element.get_attribute("innerHTML"))
        print(f'Value = {value}  ')
        return "Case1"
    else:
        return "Case2"

def Cards_Result(driver):
    global order
    order = {'2': 2,
             '3': 3,
             '4': 4,
             '5': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             '10': 10,
             'J': 11,
             'Q': 12,
             'K': 13,
             'A': 1}
    WebDriverWait(driver, 100).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".animation_blink")))
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id1)))
    span_element = driver.find_element(By.XPATH, id1)
    card1text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card1 = card1text.split(" ")
    #print(f'Card1 = {card1[0]}')
    player = card1[0]
    card11 = order[player]
    Card1 = int(card11)

    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id2)))
    span_element = driver.find_element(By.XPATH, id2)
    card2text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card2 = card2text.split(" ")
    #print(f'Card1 = {card2[0]}')

    player = card2[0]
    card22 = order[player]
    Card2 = int(card22)

    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, id3)))
    span_element = driver.find_element(By.XPATH, id3)
    card3text = span_element.get_attribute("innerHTML")
    # TO CONVERT STRING TO ARRAY
    card3 = card3text.split(" ")
    #print(f'Card1 = {card3[0]}')

    player = card3[0]
    card33 = order[player]
    Card3 = int(card33)

    Cards_Value = [Card1, Card2, Card3]
    return Cards_Value
