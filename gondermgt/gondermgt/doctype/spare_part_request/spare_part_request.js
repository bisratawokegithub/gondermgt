// Copyright (c) 2022, 360ground and contributors
// For license information, please see license.txt
function setReadOnly(fields,form) {

    fields.forEach(field => {

        form.set_df_property(field,'read_only',1)

    })

}
frappe.ui.form.on("spare part request", {

    after_workflow_action: function (form) {
		//alert(form.doc.workflow_state)
        frappe.show_alert({
            
            message:__(form.doc.workflow_state),
            
            indicator:form.doc.workflow_state == 'Rejected' || form.dock_workflow_state == 'canceled' ? 'red' : 'green'
        
        },5 )

    },
    onload(form) {
        
        let fields = ['የመኪና_ዓይነት','የተሽከርካዉ_የሰሌዳ_ቁጥር','የአንዱ_ዋጋ','ብዛት','የመለዋወጫ_አይነት_መለያ_ቁጥር'] 
        

        switch(form.doc.workflow_state){

            case "Draft":
                
                getVehicles(form)

                return
            
            case "Requested":

                form.toggle_display(['ተሽከርካሪ_ይምረጡ'],0)
                
                setReadOnly(fields,form)
            default:

                setReadOnly(fields,form)

        }

    },
});




//get list of vehicles

function getVehicles(form) {

    form.set_query('ተሽከርካሪ_ይምረጡ',function(){

        return {

            query: "gondermgt.api.getCars",

            filters: {

                'from': 'spare'

            }

        };

    })



}