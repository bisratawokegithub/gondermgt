# Copyright (c) 2022, 360ground and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class sparepartrequest(Document):
	
	def before_save(self):

		print('--------------- in spare parts request before save hook-----------------')

		self.ጠቅላላ_ዋጋ = str(float(self.የአንዱ_ዋጋ) * float(self.ብዛት))

		print(self.docstatus)

		currentUser = dict()

		currentUser["id"] = frappe.auth.get_logged_user()

		currentUser["roles"] = frappe.get_roles(currentUser["id"])

		print(f" current user = {currentUser['id']} and there roles = {currentUser['roles']}")

		if self.workflow_state == "Requested":

			print('----------- in requested-----------------')

			print('------------- about to print the vehicle info----------------')

			docInfo = self.as_dict()

			vehicle = docInfo['ተሽከርካሪ_ይምረጡ'][0]
			#self.መለዋወጫዉን_የጠየቀዉ_መካኒክ_ስም
			self.መለዋወጫዉን_የጠየቀዉ_መካኒክ_ስም = currentUser["id"]
			

			self.የተሽከርካዉ_የሰሌዳ_ቁጥር = vehicle['name']

			print(vehicle)
			pass
		
		if self.workflow_state == "Approved":
			
			self.መለዋወጫዉን_እንዲሰጥ_ጥያቄዉን_የፈቀደዉ_የተሸከርካሪ_ስምሪትና_ጋራዥ_አስተባባሪ = currentUser["id"]

			self.የተፈቀደበት_ቀን = str(frappe.utils.getdate())
			
			pass


		if self.workflow_state == "Received":

			self.መለዋወጫዉን_የተረከበዉ_ሹፌር_ስም = currentUser["id"]

			self.በዚህ_ቀን_ተቀብለዋል = str(frappe.utils.getdate())
		
		pass


	def before_cancel(self):
		
		print('----------------in cancel ----------------')

		currentUser = dict()

		currentUser["id"] = frappe.auth.get_logged_user()

		currentUser["roles"] = frappe.get_roles(currentUser["id"])

		self.የሰረዘ_ሰው = currentUser["id"]

		self.የተሰረዘበት_ቀን = str(frappe.utils.getdate())

	

	def before_submit(self):

		print('------------------------------ in before submit---------------------')
		
		currentUser = dict()

		currentUser["id"] = frappe.auth.get_logged_user()

		currentUser["roles"] = frappe.get_roles(currentUser["id"])
		
		if self.workflow_state == "Rejected":

			self.የከለከለው_ሰው = currentUser["id"]

			self.ቀን = str(frappe.utils.getdate())