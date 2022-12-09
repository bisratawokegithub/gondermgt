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
			docInfo = self.as_dict()

			if self.workflow_state == "Requested":
				print('------------------- in requested state--------')

				if 'Vehicle approver' not in self.currentUser['roles'] or self.የጠያቂ_ስም == None:
					
					self.የጠያቂ_ስም = self.currentUser["id"]
				
				else:

					print('--------- in before save-----------vehicle information')
					
				
				#self.የተመረጠው_ተሽከርካሪ_የሰሌዳ_ቁጥር = docInfo['ተሽከርካሪ_ይምረጡ'][0]

		
			if self.workflow_state == "vehicle assigned":

				print('------------in before save (vehicle assigned)----------')
				print( docInfo['ተሽከርካሪ_ይምረጡ'])

				selected_vehicle = docInfo['ተሽከርካሪ_ይምረጡ'][0]

				print(selected_vehicle)
				
				self.assignVehicleToTrip(selected_vehicle['vehicle'],self.ለአገልግሎት_የሚፈለግበት_ሰዓት_እስከዚህ_ጊዜ_ድረስ)

				self.የተመረጠው_ተሽከርካሪ_የሰሌዳ_ቁጥር = selected_vehicle['vehicle']
				
				print(f"--------in approved who are you = {self.አጽዳቂው_ስም}----------")
				
				self.የተመደበው_ተሽከርካሪ_የሰሌዳ_ቁጥር = self.የተመረጠው_ተሽከርካሪ_የሰሌዳ_ቁጥር

				driver = frappe.db.get_list('vehicle management',fields=['የተመደበ_ሹፌር'],filters=[["name","=",self.የተመደበው_ተሽከርካሪ_የሰሌዳ_ቁጥር]])

				print(driver)

				driver_name = driver[0]['የተመደበ_ሹፌር']

				print(driver_name)

				self.የተመደበው_ሹፌር_ስም = driver_name

				print('------------printed driver info---------------')
			
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

		
	#assign vehicle to trip
	def assignVehicleToTrip(self,license_plate,trip_end_date):
		
		try:
			
			print('---------- in assigning vehicle to trip-----------------')

			print(license_plate)
			
			frappe.db.set_value('vehicle management',license_plate,'isassignedtotrip',1)

			frappe.db.set_value('vehicle management',license_plate,'tripEndDate',trip_end_date)
			
			return

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
		
	
	

	


		



