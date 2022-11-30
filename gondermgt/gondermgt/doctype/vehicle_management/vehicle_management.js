// Copyright (c) 2022, 360ground and contributors
// For license information, please see license.txt


/*
function setReadOnly(fields,form) {

    try {
        
        fields.forEach(field => {

            form.set_df_property(field,'read_only',1)


        })
    } catch (err) {
        frappe.throw(err)
    }

}

*/
//
frappe.ui.form.on("vehicle management", {

    onload(form) {
        
        getDrivers(form)
       

    },

    validate(form) {

        if(form.doc.workflow_state != "Draft") {

            let numberOfDrivers = form.doc.የተመደበ_ሹፌር.length 
            
            if(numberOfDrivers > 1 ) frappe.throw('You can only assign one driver at a time')

        }


            
    },
})
//gets drivers by calling custom white listed function
function getDrivers(form) {

    form.set_query("የተመደበ_ሹፌር",  function() {
        
        return {
            query: "gondermgt.api.getDrivers",
        };
    })

}