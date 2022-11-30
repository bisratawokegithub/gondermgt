# Copyright (c) 2022, 360ground and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class tirechangerequest(Document):

	def getCurrentUser(self):

		self.currentUser = dict()

		self.currentUser["id"]= frappe.auth.get_logged_user()

		self.currentUser["roles"] = frappe.get_roles(self.currentUser["id"])
	
	def before_save(self):


		self.getCurrentUser()

		print('-----------------------------in before save --------------------------')

		print(f" the current user is {self.currentUser['id']} and the role of the current is {self.currentUser['roles']}")

		if self.workflow_state == "Requested":
			
			self.የጠያቂዉ_ሥም = self.currentUser["id"]

		if self.workflow_state == "verification passed" or self.workflow_state == "verification failed":

			self.ያረጋገጠዉ_ሥም = self.currentUser["id"]	


		pass

	def before_submit(self): 

		self.getCurrentUser()

		print('--------------------------in on submit-----------------------')

		print(f" The current user is {self.currentUser['id']} and there roles is as follows {self.currentUser['roles']}")


		if self.workflow_state == "Approved":

			self.ያፀደቀዉ_ስም = self.currentUser["id"]

			self.የፀደቀበት_ቀን = str(frappe.utils.getdate()) 


		if self.workflow_state == "Rejected":

			self.ይህን_ጥያቄ_ውድቅ_ያደረገ_ሰው = self.currentUser["id"]

			self.ውድቅ_የተደረገበት_ቀን = str(frappe.utils.getdate())

		pass

	def before_cancel(self):

		self.getCurrentUser()

		print('------------------------------- in cancel ----------------------------------')

		self.ይህን_ጥያቄ_የሰረዘው_ሰው = self.currentUser['id']

		self.የተሰረዘበት_ቀን = str(frappe.utils.getdate())
		