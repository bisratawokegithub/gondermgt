// Copyright (c) 2022, 360ground and contributors
// For license information, please see license.txt

// frappe.ui.form.on("tire change request", {
// 	refresh(frm) {
    
// 	},
// });


frappe.ui.form.on("tire change request", {

    onload(form) {

        //show_alert('hey brother have you seen avicii...ow wait he died... its about time',5)
        switch(form.doc.workflow_state) {

            case "Draft":

                return
            
            default:

                form.set_df_property('የጎማ_ጥያቄ_መረጃ','read_only',1)


        }

        /*
        if(form.doc.workflow_state == "verification passed"){

            //frappe.user_roles.includes('head mechanic')

            form.toggle_display('የጎማ_ጥያቄ_መረጃ',false)

        }

        if(form.doc.workflow_state == "Requested") {

            form.toggle_display('የጎማ_ጥያቄ_መረጃ',false)


        }

        */

    },

})
