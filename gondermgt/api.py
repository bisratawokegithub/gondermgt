import frappe


# get list of cars
@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def getCars(doctype, txt, searchfield, start, page_len, filters):

    print('------------------------ in get cars-----------------------')

    car_list = [(car['የታርጋ_ቁጥር'],) for car in frappe.db.get_list('vehicle management',fields=['የታርጋ_ቁጥር','አቅም'])]


    print(car_list)

    return car_list
# get a list of drivers
@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def getDrivers(doctype, txt, searchfield, start, page_len, filters):

    print('-------------------------- in get drivers ---------------------')
    
    drivers = frappe.db.sql("""
        SELECT name, email , job_title
        FROM `tabUser`
        Where job_title  = 'Driver' and is_assigned_car != 1
    """.format(**{
            'key': searchfield,
        }), {
        'txt': "%{}%".format(txt),
        '_txt': txt.replace("%", ""),
        'start': start,
        'page_len': page_len
    })

    #dv = frappe.db.get_list('User',fields=['email','name'])
    #assigned_driver = [driver['assigned_driver'] for driver in frappe.db.get_list('vehicle management',fields=['assigned_driver']) ]
    assigned_driver = [driver['የተመደበ_ሹፌር'] for driver in frappe.db.get_list('vehicle management',fields=['የተመደበ_ሹፌር']) ]
    
    drivers_ls = [(user['email'],user['name']) for user in frappe.db.get_list('User',fields=['email','name']) if "Driver" in frappe.get_roles(user["name"]) if user['name'] not in assigned_driver]

    #print(assigned_driver)
    #print(assigned_driver)

    print(drivers_ls)


  
    #print(vech)
    #print(drivers)

    #return [('bisrat@360ground.com','bisrat@360ground.com'),]
    return drivers_ls