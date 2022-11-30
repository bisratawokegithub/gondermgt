# Copyright (c) 2022, 360ground and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
class maintenancerequest(Document):
	

	def getCurrentUser(self):

		self.currentUser = dict()

		self.currentUser['id'] = frappe.auth.get_logged_user()

		self.currentUser['roles'] = frappe.get_roles(self.currentUser['id'])

		print(f"----------- the current user is {self.currentUser['id']} with the following roles {self.currentUser['roles']} \n")


	def before_save(self):

		print('---------------in before save------------ \n')

		self.request_name = f"{self.ፋካሊቲ}-{self.የጥገናዉ_ዓይነት}{frappe.utils.getdate()}"

		self.getCurrentUser()
		
		print(self.workflow_state)

		if self.workflow_state == "Requested":

			print('--------in requested----------')

			self.ጥገናዉን_የጠየቀዉ_ሠራተኛ_ስም = self.currentUser["id"]
		
		if self.workflow_state == "maintenance started":

			print('---------------------in maintenace started--------------')

			self.ጥገናውን_የሚያከናውነው_ሰው = self.currentUser["id"]

			self.የጥገና_መጀመሪያ_ቀን = str(frappe.utils.getdate())

		if self.workflow_state == "maintenance ended":

			print('----------------------in maintenance ended---------------')

			self.ጥገናው_የተጠናቀቀበት_ቀን = str(frappe.utils.getdate())
		
		#if self.workflow_state == "ma"
		pass

	def before_submit(self):

		try:

			self.getCurrentUser()

			print('---------in submit----------\n')

			print(self.workflow_state)

			if self.workflow_state == "Approved":
				
				self.ጥገናዉን_የተረከበዉ = self.currentUser["id"]

				self.ተረከበዉ_ቀን = str(frappe.utils.getdate())

			if self.workflow_state == "Rejected":

				print('------------in rejected baby-------------\n')

				self.ይህን_ጥያቄ_ውድቅ_ያደረገ_ሰው = self.currentUser["id"]

				self.ቀን = str(frappe.utils.getdate())

				print(self.ይህን_ጥያቄ_ውድቅ_ያደረገ_ሰው)
		
		except Exception as ex:
			
			print(ex)

		

	def before_cancel(self):

		self.getCurrentUser()

		self.ጥገናዉን_የሰረዘው = self.currentUser["id"]

		self.የተሰረዘበት_ቀን = str(frappe.utils.getdate())

