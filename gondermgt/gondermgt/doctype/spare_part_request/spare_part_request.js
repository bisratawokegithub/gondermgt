// Copyright (c) 2022, 360ground and contributors
// For license information, please see license.txt
function setReadOnly(fields,form) {

    fields.forEach(field => {

        form.set_df_property(field,'read_only',1)

    })

}
frappe.ui.form.on("spare part request", {

    
    onload(form) {

        let fields = ['የመኪና_ዓይነት','የተሽከርካዉ_የሰሌዳ_ቁጥር','የአንዱ_ዋጋ','ብዛት','የመለዋወጫ_አይነት_መለያ_ቁጥር'] 
        
        switch(form.doc.workflow_state){

            case "Draft":

                return

            default:

                setReadOnly(fields,form)

        }


        


       
    },
	refresh(frm) {
 	},
});
