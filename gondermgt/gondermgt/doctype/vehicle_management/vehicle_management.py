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


	def on_update(self):

		pass
		#frappe.msgprint(f"{self.workflow_state}")
		#frappe.msgprint(f"{self.workflow_state}")

	def before_save(self):

		try:

			print('----------------- in before save ------------------')

			self.getCurrentUser()

			if self.workflow_state == "Waiting for new driver to be assigned":
				

				print(' just removed old user')

				#docInfo = self.as_dict()
				 
				#driverInfo = docInfo['የተመደበ_ሹፌር'][0]

				#frappe.db.sql(f"""
				#	update `tabUser` set is_assigned_car = 0 where email = '{driverInfo['user']}' 
				#""")
			
			if self.workflow_state == "Added new vehicle entry":

				self.አስረካቢ = self.currentUser['id']

			if self.workflow_state == "receiver confirmed":

				self.ተረካቢ = self.currentUser['id']


			if self.workflow_state == "mechanic confirmed":

				self.አረካካቢየተሽከርካሪ_ባለሙያመካኒክ = self.currentUser['id']

				pass

			if self.workflow_state == "Waiting for driver confirmation":

				print('-------------------- waiting for driver confirmation------------------')

				docInfo = self.as_dict()
				
				print(docInfo['ሹፌር_ይምረጡ'])
				#driverInfo = docInfo['የተመደበ_ሹፌር'][0]
				driverInfo = docInfo['ሹፌር_ይምረጡ'][0]
				
				print(driverInfo)
				
				print(self.currentUser['id'])


				print('-------------------- time to update the users info-------------------')

					#self.assigned_driver = driverInfo['user']
				self.የተመደበ_ሹፌር = driverInfo['user']


					#remove this during production
					#frappe.db.sql(f"""
					#	update `tabUser` set is_assigned_car = 1 where email = '{driverInfo['user']}' 
					#""")

				
				mssg = f"You have been assigned to vehicle please follow link below to confirm. https://gondermgt.localhost:8000/app/vehicle management/{self.name}"

				#frappe.sendmail(recipients=[self.የተመደበ_ሹፌር],content=mssg)
					
				print('----------------------all good in the hood----------------------------')

			pass

			if self.workflow_state == "Driver assigned" :
				
				print('-------------------- in driver assigned------------------')

				docInfo = self.as_dict()
				
				print(docInfo['ሹፌር_ይምረጡ'])
				#driverInfo = docInfo['የተመደበ_ሹፌር'][0]
				driverInfo = docInfo['ሹፌር_ይምረጡ'][0]
				
				print(driverInfo)
				
				print(self.currentUser['id'])

				if self.currentUser['id'] != driverInfo['user']:
			
					raise Exception(f"You are not {driverInfo['user']} so you can not confirm on there behalf")

				else:

					print('-------------------- time to update the users info-------------------')

					#self.assigned_driver = driverInfo['user']
					self.የተመደበ_ሹፌር = driverInfo['user']


					#remove this during production

					
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