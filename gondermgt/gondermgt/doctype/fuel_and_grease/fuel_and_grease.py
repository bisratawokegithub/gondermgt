# Copyright (c) 2022, 360ground and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe


	
class FuelandGrease(Document):

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

				self.የፈቃጅ_ስም = self.currentUser['id']

				self.የተፈቀደበት_ቀን = str(frappe.utils.getdate())

				pass
			


			if self.workflow_state == "Received":

				print('------- in Received-------')

				self.የተረከበው_ስም = self.currentUser['id']

				self.የተረከበበት_ቀን = str(frappe.utils.getdate())

				pass


			if self.workflow_state == "Did not receive item":

				self.እንዳልተቀበሉ_የሚገልጽ_ሰው = self.currentUser['id']

				self.እንዳልተቀበሉ_የገለጹበት_ቀን = str(frappe.utils.getdate())

				
		except Exception as ex:

			print(ex)


	def before_submit(self):

		try:

			self.getCurrentUser()

			print('---------------- in before submit-----------')

			if self.workflow_state == "verification passed":

				print('------------------ in verification passed-----------')

				print('---------- in verification passed')

				self.አረጋጋጭ_ስም = self.currentUser['id']

				self.የተረጋገጠበት_ቀን = str(frappe.utils.getdate())

				pass

			if self.workflow_state == "canceled":

				print('--------in cancel------')

				self.የሰረዘ_ሰው_ስም = self.currentUser['id']

				self.የተሰረዘበት_ቀን = str(frappe.utils.getdate())

			if self.workflow_state == "Rejected":

				print('-------------------- in rejected------------ \n')

				self.ጥያቄውን_ውድቅ_ያደረገ_ሰው = self.currentUser['id']

				self.ውድቅ_የተደረገበት_ቀን = str(frappe.utils.getdate())

			if self.workflow_state == "verification failed":

				print('----------------- in failed verification---------------')

				self.ያረጋገጠው_ሰው = self.currentUser['id']

				self.ቀን = str(frappe.utils.getdate())

		except Exception as ex:

			print(ex)

