from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest
import time

class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):

		# Jome has heard about the latest to-do list app and wants to check it out.
		self.browser.get(self.live_server_url)

		# He notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		

		# He is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

		# He enters "Learn TDD the right way" into a text box (Jome's hobby is writing code)
		inputbox.send_keys('Learn TDD the right way')
		# When he hits Enter, he is taken to a new url, and now the page 
		# lists "1: Learn TDD the right way" as an item in the to-do list table
		inputbox.send_keys(Keys.ENTER)
		jome_list_url = self.browser.current_url
		self.assertRegex(jome_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Learn TDD the right way')
		
		# There is still a text box inviting her to add another item. He enters
		# "Setup iMac to complete the course"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Setup iMac to complete the course')
		inputbox.send_keys(Keys.ENTER)

		self.browser.get(self.live_server_url)
		self.check_for_row_in_list_table('1: Learn TDD the right way')
		self.check_for_row_in_list_table('2: Setup iMac to complete the course')

		# The page updates again and shows both items on his list

		# Jome wonders if the site will remember his list. Then he sees that the site
		# has generated a unique URL for him.

		# He visits the URL - his to-do list is still there.

		# He goes to play FIFA
		self.browser.quit()

		self.browser = webdriver.Firefox()
		
		# Francis visits the home page. There is no sign of Edith's
		# list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('1: Learn TDD the right way', page_text)
		self.assertNotIn('Setup iMac to complete the course', page_text)
		# Francis starts a new list by entering a new item. He
		# is less interesting than Edith...
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)
		# Francis gets his own unique URL
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, jome_list_url)
		# Again, there is no trace of Edith's list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)
		# Satisfied, they both go back to sleep
		
		# self.fail('Finish the test!')


if __name__ == "__main__":
	unittest.main(warnings='ignore')