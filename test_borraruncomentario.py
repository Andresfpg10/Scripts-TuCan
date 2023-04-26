# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBorraruncomentariodelmuro():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_borraruncomentariodelmuro(self):
    self.driver.get("https://tucan.toolsincloud.net/home.php")
    self.driver.set_window_size(1382, 736)
    self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(7) font > font").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".wrapper-left-active > strong")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-ellipsis-h").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-ellipsis-h").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-ellipsis-h").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-ellipsis-h").click()
  