import frappe

# get list of cars
@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def getCars(doctype, txt, searchfield, start, page_len, filters):

    print('------------------------ in get cars-----------------------')

    print(filters)
    # filter cars are return those that are not assigned 
    # or return cars with  assignment end date that are before the new assignment start date,
    if len(txt) < 1:

        if filters['from'] == 'transport':
            
            car_list = [(car['name'],car['isassignedtotrip']) for car in frappe.db.get_list('vehicle management',fields=['የታርጋ_ቁጥር','አቅም','name','isassignedtotrip'],filters=[["isassignedtotrip","=",0]])]
        
        else:

            car_list = [(car['name'],car['isassignedtotrip']) for car in frappe.db.get_list('vehicle management',fields=['የታርጋ_ቁጥር','አቅም','name','isassignedtotrip'])]
    else:

        if filters['from'] == 'transport':
            
            car_list = [(car['name'],) for car in frappe.db.get_list('vehicle management',fields=['የታርጋ_ቁጥር','አቅም','name'],filters=[['name','like',f"%{txt}%"],["isassignedtotrip","=",0]])]
        
        else:

            car_list = [(car['name'],) for car in frappe.db.get_list('vehicle management',fields=['የታርጋ_ቁጥር','አቅም','name'],filters=[['name','like',f"%{txt}%"]])]
    
    print(car_list)

    return car_list


# get a list of drivers
@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def getDrivers(doctype, txt, searchfield, start, page_len, filters):

    print('-------------------------- in get drivers ---------------------')
    
    assigned_driver = [driver['የተመደበ_ሹፌር'] for driver in frappe.db.get_list('vehicle management',fields=['የተመደበ_ሹፌር']) ]
    
    if len(txt) < 1:

        drivers_ls = [(user['email'],user['name']) for user in frappe.db.get_list('User',fields=['email','name']) if "Driver" in frappe.get_roles(user["name"]) if user['name'] not in assigned_driver]

    else:  

        print('------------------- in filter search-----------------')

        print(txt)

        drivers_ls = [(user['email'],user['name']) for user in frappe.db.get_list('User',fields=['email','name'],filters=[["email","like",f"%{txt}%"]]) if "Driver" in frappe.get_roles(user["name"]) if user['name'] not in assigned_driver]
 
    print(drivers_ls)

    print(searchfield)

    print(len(txt))
  
    return drivers_ls


# get list of mechanics
@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def getMechanics(doctype, txt, searchfield, start, page_len, filters):

        if len(txt) < 1:

            mechanic_ls = [(user['email'],user['name']) for user in frappe.db.get_list('User',fields=['email','name']) if "mechanic" in frappe.get_roles(user["name"])]

        else:
            
            mechanic_ls = [(user['email'],user['name']) for user in frappe.db.get_list('User',fields=['email','name'],filters=[["name","like",f"%{txt}%"]]) if "mechanic" in frappe.get_roles(user["name"])]
        
        print(mechanic_ls)

        return mechanic_ls
    
