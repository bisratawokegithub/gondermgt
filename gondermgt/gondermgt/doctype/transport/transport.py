# Copyright (c) 2022, 360ground and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_days, getdate, formatdate, get_first_day, date_diff, add_years

class transport(Document):
	
	def getCurrentUser(self):

		self.currentUser = dict()

		self.currentUser["id"] = frappe.auth.get_logged_user()

		self.currentUser["roles"] = frappe.get_roles(self.currentUser["id"])

		
	def before_save(self):
		
		print('-----------------in save------------\n')
		
		try:

			self.getCurrentUser()

			print(f" The current user is {self.currentUser['id']} and its role is {self.currentUser['roles']}")

			#self.has_been_saved = 1

			#self.cover = "<div style='width:100vh;height:100vh;background-color:black;'> hello<div>"

			if self.workflow_state == "Requested":
				
				self.የጠያቂ_ስም= self.currentUser["id"]
			
			if self.workflow_state == "In Trip":

				self.የተሽከርካሪ_መነሻ_ቀን = str(frappe.utils.getdate())

				self.የተሽከርካሪ_መነሻ_ቀን_አረጋጋጭ_ስም = self.currentUser['id']

				pass
			
			if self.workflow_state == "Returned from trip":

				self.ተሽከርካሪው_የተመለሰበት_ቀን = str(getdate())

				self.ተሽከርካሪው_የተመለሰበት_ቀን_አረጋጋጭ_ስም = self.currentUser['id']

				pass

			if self.workflow_state == "verified":

				self.አረጋጋጭ_ስም = self.currentUser['id']

			if self.workflow_state == "Approved":

				print('---------------in approved-------------')



				self.ቀን = str(frappe.utils.getdate())
				self.አጽዳቂው_ስም = self.currentUser['id']
				print(f"--------in approved who are you = {self.አጽዳቂው_ስም}----------")

			if self.workflow_state == "Rejected":

				self.ይህን_ጥያቄ_ውድቅ_ያደረገ_ሰው = self.currentUser["id"]

				self.ውድቅ_የተደረገበት_ቀን = str(frappe.utils.getdate())

			
			if self.workflow_state == "vehicle has departed":

				print('--------------------- in vehicle has departed--------------\n')

				self.የተሽከርካሪ_መነሻ_ቀን_አረጋጋጭ_ስም = self.currentUser['id']

				self.የተሽከርካሪ_መነሻ_ቀን = str(frappe.utils.getdate())

			
			if self.workflow_state == "vehicle has returned":

				print('------------------------- in vehicle has returned---------\n')

				self.ተሽከርካሪው_የተመለሰበት_ቀን_አረጋጋጭ_ስም = self.currentUser['id']

				self.ተሽከርካሪው_የተመለሰበት_ቀን = str(frappe.utils.getdate())

		except Exception as ex:

			print(ex)

		


	

	def before_submit(self):

		try:
			
			self.getCurrentUser()

			print('----------------------------- in before submit-------------------\n')

			if self.workflow_state == "verified":

				print('-------------- in verified----------------')

				self.አረጋጋጭ_ስም = self.currentUser['id']

			if self.workflow_state == "canceled":
				
				self.ይህን_ጥያቄ_የሰረዘው_ሰው = self.currentUser['id']

				self.የተሰረዘበት_ቀን = str(frappe.utils.getdate())
			
			if self.workflow_state == "Approved":

				print('---------------in approved-------------')

				self.ቀን = str(frappe.utils.getdate())
				
				self.አጽዳቂው_ስም = self.currentUser['id']

				print(f"--------in approved who are you = {self.አጽዳቂው_ስም}----------")

		
			if self.workflow_state == "Rejected":

				self.ይህን_ጥያቄ_ውድቅ_ያደረገ_ሰው = self.currentUser["id"]

				self.ውድቅ_የተደረገበት_ቀን = str(frappe.utils.getdate())
	

		except Exception as ex:

			print(ex)


	def before_cancel(self):

		self.getCurrentUser()

		print('------------------------------- in cancel ----------------------------------')

		self.ይህን_ጥያቄ_የሰረዘው_ሰው = self.currentUser['id']

		self.የተሰረዘበት_ቀን = str(frappe.utils.getdate())
		
	
	

	


		



