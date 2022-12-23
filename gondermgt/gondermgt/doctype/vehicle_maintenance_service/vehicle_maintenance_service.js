// Copyright (c) 2022, 360ground and contributors
// For license information, please see license.txt
//set fileds to read only

function setReadOnly(fields,form) {

    try {
        
        fields.forEach(field => {

            form.set_df_property(field,'read_only',1)

        })

    } catch (err) {
        
        console.log(err)
    }

}
 frappe.ui.form.on("vehicle maintenance service", {

    after_workflow_action: function (form) {
		//alert(form.doc.workflow_state)
        frappe.show_alert({
            
            message:__(form.doc.workflow_state),
            
            indicator:form.doc.workflow_state == 'Rejected' || form.dock_workflow_state == 'canceled' ? 'red' : 'green'
        
        },5 )

    },
 	onload(form) {
        


        form.toggle_display(['ተሽከርካሪ_ይምረጡ'],0)
        
        form.toggle_display(['ጥገናውን_የሚያከናውን_መካኒክ_ይምረጡ'],0)

        if(form.doc.workflow_state == "Draft" || form.doc.workflow_state == "Requested") form.toggle_display(['ተሽከርካሪ_ይምረጡ'],1)

        if(form.doc.workflow_state == "deployment coordinator approved" || form.doc.workflow_state == "mechanic confirmed") setReadOnly(['የመስርያቤቱ_ስም','የብልሽት_አይነት',],form)

        if(form.doc.workflow_state == "Vehicle distribution and garage coordinator approved") {
            
            form.toggle_display(['ጥገናውን_የሚያከናውን_መካኒክ_ይምረጡ'],1)


        }
        getMechanics(form)

 	},
 });


 //fetch list of available mechanics

 function getMechanics(form){

    try{

        form.set_query('ጥገናውን_የሚያከናውን_መካኒክ_ይምረጡ',function() {

            return {

                query: 'gondermgt.api.getMechanics',

                from: 'maintenace'

            }


        })


    }catch(err) {

        console.log(err)

    }

 }
