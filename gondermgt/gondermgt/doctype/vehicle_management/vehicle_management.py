# Copyright (c) 2022, 360ground and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
#from frappe.utils.pdf import get_pdf

class vehiclemanagement(Document):
	

	def getCurrentUser(self):

		self.currentUser = dict()

		self.currentUser['id'] = frappe.auth.get_logged_user()

		self.currentUser['roles'] = frappe.get_roles(self.currentUser['id'])



	def before_save(self):

		try:

			print('----------------- in before save ------------------')

			self.getCurrentUser()

			if self.workflow_state == "Waiting for new driver to be assigned":
				

				print(' just removed old user')

				docInfo = self.as_dict()
				
				driverInfo = docInfo['የተመደበ_ሹፌር'][0]
				
				frappe.db.sql(f"""
					update `tabUser` set is_assigned_car = 0 where email = '{driverInfo['user']}' 
				""")



			if self.workflow_state == "Driver assigned":

				docInfo = self.as_dict()
				
				driverInfo = docInfo['የተመደበ_ሹፌር'][0]
				
				print(driverInfo)
				
				if self.currentUser['id'] != driverInfo['user']:
			
					raise Exception(f"You are not {driverInfo['user']} so you can confirm on there behalf")

				else:

					print('-------------------- time to update the users info-------------------')

					frappe.db.sql(f"""
						update `tabUser` set is_assigned_car = 1 where email = '{driverInfo['user']}' 
					""")
					
					print('----------------------all good in the hood----------------------------')

			pass
			
			
		except Exception as ex:
			
			print(ex)

			frappe.throw("error")

	"""
	def before_save(self):	


		try:
			#if self.workflow_state != "Draft":
			info = self.as_dict()
			
			print('--------------------------- in before save--------------------')
			
			print(info['ሹፌር_ይምረጡ'])

			chossenDrivers = [assignedUser for assignedUser in info['ሹፌር_ይምረጡ'] if assignedUser['ይምረጡ']]

			length = len(chossenDrivers)

			print(chossenDrivers)

			print(length)

			pass

		except Exception as ex:

			print(ex)
		
	def validate(self):
		
		self.getCurrentUser()

		info = self.as_dict()
			
		print('--------------------------- in validate--------------------')
			
		print(info['ሹፌር_ይምረጡ'])

		chossenDrivers = [assignedUser for assignedUser in info['ሹፌር_ይምረጡ'] if assignedUser['ይምረጡ']]

		length = len(chossenDrivers)

		print(chossenDrivers)
		
		if self.workflow_state == "Driver assigned":

			if chossenDrivers[0]['የአሽከርካሪዎች_ስም'] != self.currentUser['id']:
					
				print('------------------- in driver assigned---------------------------')

				frappe.throw('Who the fuck are you')
	
	def validate(self):

		try:

			self.getCurrentUser()

			if self.workflow_state == "Driver assigned" and self.currentUser['id'] != driver and "BizAdmin" not in self.currentUser['roles']:

				frappe.throw("You can not confirm what has not been assigned to you !!!")

				return


		except Exception as ex:

			frappe.throw(ex)
	"""