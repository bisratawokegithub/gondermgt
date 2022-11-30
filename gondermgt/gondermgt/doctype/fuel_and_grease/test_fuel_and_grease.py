# Copyright (c) 2022, 360ground and Contributors
# See license.txt

# import frappe
from frappe.tests.utils import FrappeTestCase
import frappe

class TestFuelandGrease(FrappeTestCase):
	
	def getCurrentUser(self):

		self.currentUser = dict()

		self.currentUser['id'] = frappe.auth.get_logged_user()

		self.currentUser['roles'] = frappe.get_roles(self.currentUser['id'])


		
	def before_save(self):
		
		try:

			print('--------- in before save--------- \n')

			self.getCurrentUser()

			if self.workflow_state == "Requested":

				print('-------------- in requested-------------\n')

				self.የጠያቂው_ስም = self.currentUser['id']

				pass
			
			if self.workflow_state == "Approved":
				
				print('----------------- in approved--------------\n')

				pass
		
		except Exception as ex:

			print(ex)

	def before_submit(self):

		pass