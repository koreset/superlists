from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):


		# Jome has heard about the latest to-do list app and wants to check it out.
		self.browser.get('http://localhost:8000')

		# He notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		

		# He is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'), 'Enter a to-do item')

		# He enters "Learn TDD the right way" into a text box (Jome's hobby is writing code)
		inputbox.send_keys('Learn TDD the right way')
		# When he hits Enter, the page updated, and now the page lists
		# "1: Learn TDD the right way" as an item in the to-do list
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(any(row.text) == '1: Learn TDD the right way' for row in rows)

		# There is still a text box inviting her to add another item. He enters
		# "Setup iMac to complete the course"

		# The page updates again and shows both items on his list

		# Jome wonders if the site will remember his list. Then he sees that the site
		# has generated a unique URL for him.

		# He visits the URL - hsi to-do list is still there.

		# He goes to play FIFA
		self.fail('Finish the test!')


if __name__ == "__main__":
	unittest.main(warnings='ignore')