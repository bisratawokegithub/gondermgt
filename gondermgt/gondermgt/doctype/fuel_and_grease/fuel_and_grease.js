// Copyright (c) 2022, 360ground and contributors
// For license information, please see license.txt

function setReadOnly(fields,form) {

    try {
        
        fields.forEach(field => {


            form.set_df_property(field,'read_only',1)


        })

    } catch (err) {
        
        frappe.throw(err)

    }

}
frappe.ui.form.on("Fuel and Grease", {
    after_workflow_action: function (form) {
		//alert(form.doc.workflow_state)
        frappe.show_alert({
            
            message:__(form.doc.workflow_state),
            
            indicator:form.doc.workflow_state == 'Rejected' || form.dock_workflow_state == 'canceled' ? 'red' : 'green'
        
        },5 )

    },
    onload(form) {

        let fields = ['የኩፖን_ቁጥር','የመኪናው_ዓይነት','የሰሌዳ_ቁጥር','ኪሎ_ሜትር',"የነዳጅ_ቅጽ","የቅባት_ቅጽ","ዘይት_ቅጽ"]
        
        switch(form.doc.workflow_state) {

            case "Approved":

                setReadOnly(fields,form)

                return

            default:

                return


        }
            //alert(frappe.user_roles)
           // form.toggle_display('የጠያቂ_ስምና',frappe.user_roles.includes('Guard'))
    },
 });
