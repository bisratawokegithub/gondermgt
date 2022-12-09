# Copyright (c) 2022, 360ground and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class vehiclemaintenanceservice(Document):
	

	def getCurrentUser(self):

		self.currentUser = dict()
		
		self.currentUser['id'] = frappe.auth.get_logged_user()

		self.currentUser['roles'] = frappe.get_roles(self.currentUser['id'])



	def before_save(self):

		print('--------------------- in before save---------------')

		self.getCurrentUser()

		if self.workflow_state == 'Requested':
			
			docInfo = self.as_dict()

			drivers_list = docInfo['ተሽከርካሪ_ይምረጡ'][0]
			
			print(drivers_list)

			self.የሰሌዳ_ቁጥር = drivers_list['name']


		elif self.workflow_state == "deployment coordinator approved":

			self.የስምሪት_አስተባባሪ_ስም = self.currentUser['id']


		elif self.workflow_state == "Vehicle distribution and garage coordinator approved":

			self.የተሽከርካሪ_ስምሪትና_ጋራዥ_አስተባባሪ_ስም = self.currentUser['id']

		elif self.workflow_state == "waiting for mechanic confirmation":
			
			print('---------------- in waiting for mechanic confirmation--------------------')

			docInfo = self.as_dict()

			choosen_mechanic = docInfo['ጥገናውን_የሚያከናውን_መካኒክ_ይምረጡ'][0]
			
			print(choosen_mechanic)

			self.ጥገናውን_የሚያከናውን_መካኒክ_ስም = choosen_mechanic['user']

		elif self.workflow_state == "mechanic confirmed":
			
			if self.ጥገናውን_የሚያከናውን_መካኒክ_ስም != self.currentUser['id']:

				frappe.throw("You cant confirm an assignment thats not yours !")

			else:

				pass

		else:

			pass
			