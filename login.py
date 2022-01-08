from selenium import webdriver
from time import sleep
from os import system
from tkinter import *

def log(username, password):
    url = "https://edt.esiea.fr"

    driver = webdriver.Safari()
    driver.maximize_window()

    driver.get(url)
    sleep(1.5)
    driver.find_element_by_id("GInterface_bouton_3").click()

    sleep(2)

    driver.find_element_by_id("id_59").send_keys(username)
    driver.find_element_by_id("id_63").send_keys(password)
    sleep(1)
    driver.find_element_by_id("id_51").click()
    driver.switch_to.new_window("tab")

    sleep(0.5)
    url = "https://learning.esiea.fr/login/index.php"

    driver.get(url)
    driver.find_element_by_id("username").send_keys(username.lower() + "@et.esiea.fr")
    sleep(0.5)
    driver.find_element_by_id("password").send_keys(password)
    sleep(1)
    driver.find_element_by_id("loginbtn").click()
    quit = input()
    

username = "USERNAME"
password = "PASSWORD"
filepath = "Filepath to executable file of MS Teams"

log(username, password)
system(filepath)
