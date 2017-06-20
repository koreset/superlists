from selenium import webdriver
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
		self.fail('Finish the test!')

		# He is invited to enter a to-do item straight away

		# He enters "Learn TDD the right way" into a text box (Jome's hobby is writing code)

		# When he hits Enter, the page updated, and noe the page lists
		# "1: Learn TDD the right way" as an item in the to-do list

		# There is still a text box inviting her to add another item. He enters
		# "Setup iMac to complete the course"

		# The page updates again and shows both items on his list

		# Jome wonders if the site will remember his list. Then he sees that the site
		# has generated a unique URL for him.

		# He visits the URL - hsi to-do list is still there.

		# He goes to play FIFA


if __name__ == "__main__":
	unittest.main(warnings='ignore')