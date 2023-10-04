from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.keybr.com/")
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/a").click()
driver.find_element(By.CSS_SELECTOR, "body").click()

theSleep = 0.1

def findWords():
    wordsHolder = driver.find_element(By.XPATH, "/html/body/main/section/div[3]/div/div[2]/div")
    wordsElements = wordsHolder.find_elements(By.CSS_SELECTOR, "span")
    words = []

    next = False
    for word in wordsElements:
        if word.text == "" or word.text == "⸱":
            next = True
        elif next:
            next = False
            words.append(word.text.replace("⸱",""))

    return words

def typeWords(words):
    body = driver.find_element(By.CSS_SELECTOR, "body")
    wordsString = " ".join(words)

    for key in wordsString:
        body.send_keys(key)
        sleep(theSleep)




while True:
    print("\nRunning with", theSleep, "second timeout between keys")

    words = findWords()
    print(words)
    print("Words:", len(words))
    typeWords(words)

    sleep(1)
    theSleep *= 0.99