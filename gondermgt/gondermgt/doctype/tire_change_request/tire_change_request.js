// Copyright (c) 2022, 360ground and contributors
// For license information, please see license.txt

// frappe.ui.form.on("tire change request", {
// 	refresh(frm) {
    
// 	},
// });


frappe.ui.form.on("tire change request", {
    after_workflow_action: function (form) {
		//alert(form.doc.workflow_state)
        frappe.show_alert({
            
            message:__(form.doc.workflow_state),
            
            indicator:form.doc.workflow_state == 'Rejected' || form.dock_workflow_state == 'canceled' ? 'red' : 'green'
        
        },5 )

    },
    onload(form) {


        //show_alert('hey brother have you seen avicii...ow wait he died... its about time',5)
        switch(form.doc.workflow_state) {

            case "Draft":

                return
            
            default:

                form.set_df_property('የጎማ_ጥያቄ_መረጃ','read_only',1)


        }

    },

})
