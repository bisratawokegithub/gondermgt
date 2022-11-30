import frappe

# get a list of drivers
@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def getDrivers(doctype, txt, searchfield, start, page_len, filters):

    print('-------------------------- in get drivers ---------------------')
    
    return frappe.db.sql("""
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