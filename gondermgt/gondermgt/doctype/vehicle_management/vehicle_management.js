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

        frappe.show_alert({
            
            message:__(form.doc.workflow_state),
            
            indicator:'green'
        
        },5 )
        //getDrivers(form)
        switch(form.doc.workflow_state) {

            case "receiver confirmed":
                
                getListOfDrivers(form)

                form.toggle_display('ሹፌር_ይምረጡ',1)

                break

            case "Waiting for new driver to be assigned":

                getListOfDrivers(form)

                form.toggle_display('ሹፌር_ይምረጡ',1)

                break

            
            case "Driver assigned":

                form.set_value('ሹፌር_ይምረጡ',[])

                form.toggle_display('ሹፌር_ይምረጡ',0)

                break
                
            default:
                
                form.toggle_display('ሹፌር_ይምረጡ',0)

        }

    },

    validate(form) {

        if(form.doc.workflow_state != "Draft") {

            let numberOfDrivers = form.doc.ሹፌር_ይምረጡ.length 
            
            if(numberOfDrivers > 1 ) frappe.throw('You can only assign one driver at a time')

            //frappe.show_alert(form.doc.workflow_state,5 )
        }


            
    },
})

//create choose driver field and auto populate

function getListOfDrivers(form) {

    form.set_query('ሹፌር_ይምረጡ',() => {

        return {

            query: "gondermgt.api.getDrivers",

        };

    })

}
//gets drivers by calling custom white listed function
function getDrivers(form) {

    form.set_query("የተመደበ_ሹፌር",  function() {
        
        return {
            query: "gondermgt.api.getDrivers",
        };
    })

}