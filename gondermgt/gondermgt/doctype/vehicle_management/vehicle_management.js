// Copyright (c) 2022, 360ground and contributors
// For license information, please see license.txt

//
frappe.ui.form.on("vehicle management", {
    after_workflow_action: function (form) {
		//alert(form.doc.workflow_state)
        frappe.show_alert({
            
            message:__(form.doc.workflow_state),
            
            indicator:form.doc.workflow_state == 'Rejected' || form.dock_workflow_state == 'canceled' ? 'red' : 'green'
        
        },5 )

    },
    onload(form) {

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
    refresh(form) {

        /*
        frappe.show_alert({
            
            message:__(form.doc.workflow_state),
            
            indicator:'green'
        
        },5 )
        */

    },

    validate(form) {

        frappe.show_alert({
            
            message:__(form.doc.workflow_state),
            
            indicator:'green'
        
        },5 )

        if(form.doc.workflow_state == "Waiting for driver confirmation") {

            try{

                let numberOfDrivers = form.doc.ሹፌር_ይምረጡ.length 
                
                if(numberOfDrivers > 1 ) frappe.throw('You can only assign one driver at a time')
            }catch(err) {

                console.log(err)

            }
            

            //frappe.show_alert(form.doc.workflow_state,5 )
        }


            
    },
})

//create choose driver field and auto populate

function getListOfDrivers(form) {

    form.set_query('ሹፌር_ይምረጡ',() => {

        return {

            query: "gondermgt.api.getDrivers",
            
            from: "vehicle_mgt"

        };

    })

}
//gets drivers by calling custom white listed function
function getDrivers(form) {

    form.set_query("የተመደበ_ሹፌር",  function() {
        
        return {
            
            query: "gondermgt.api.getDrivers",

            from: "vehicle_mgt"

        };
    })

}