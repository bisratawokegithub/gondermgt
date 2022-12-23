// Copyright (c) 2022, 360ground and contributors
// For license information, please see license.txt

//set fields to read only 
//preventing users from tampering with recorded data

function setFieldsToReadOnly(fields,form){

    try {
        
        console.log('disableing all fields execpt for driver info')

        fields.forEach( field => {

            form.set_df_property(field,'read_only',1)

        })

    } catch (err) {
        
        console.log(err)
        frappe.throw(err)
    }

}

//allow fields to be changed
function allowWrite(fields,form) {

    try{

        fields.forEach(field => {

            form.set_df_property(field,'read_only',0)

        })

    }catch(err) {

        console.log(err)

    }


}

let fields = [

    'ለአገልግሎት_የሚፈለግበት_ሰዓት__ከዚህ_ጊዜ_ይጀምራል',

    'ለአገልግሎት_የሚፈለግበት_ሰዓት_እስከዚህ_ጊዜ_ድረስ',
    
    'የተጓዥ_ስም',
    
    'የሚሄዱበት_ቦታ',

    'ምክንያት',

    'የመውጫ_አይነት'
    
    
] 
//let showStartTripBtn = frappe.user_roles.includes('Guard') && form.doc.workflow_state == "Approved"
//form ui controller

frappe.ui.form.on("transport", {
    
    after_workflow_action: function (form) {
		//alert(form.doc.workflow_state)
        frappe.show_alert({
            
            message:__(form.doc.workflow_state),
            
            indicator:form.doc.workflow_state == 'Rejected' || form.dock_workflow_state == 'canceled' ? 'red' : 'green'
        
        },5 )

    },
    onload(form) {


        form.toggle_display(['ተሽከርካሪ_ይምረጡ'],false)
        
        if(form.doc.workflow_state == "Approved"){

            getVehicles(form,form.doc.ለአገልግሎት_የሚፈለግበት_ሰዓት__ከዚህ_ጊዜ_ይጀምራል)

            form.toggle_display(['ተሽከርካሪ_ይምረጡ'],true)
            

        }
        
        if(form.doc.workflow_state == "vehicle assigned"){
            
            form.toggle_display(['ተሽከርካሪ_ይምረጡ'],false)
            
            form.toggle_display(['የተመረጠው_ተሽከርካሪ_የሰሌዳ_ቁጥር'],false)

        }
        
        let readOnlyState = ['vehicle assigned','vehicle has departed','vehicle has returned']
                
         if(readOnlyState.includes(form.doc.workflow_state)) {
        
                setFieldsToReadOnly(fields,form)
        
            }
        /*
 
            if(form.doc.workflow_state == "Requested"){

                                    
                    form.toggle_display(['ተሽከርካሪ_ይምረጡ'],true)
                                
            
            }

                

                
                
                    
                 */   
    
                

    
       
        
    },
    validate(form) {

        console.log(form.doc.status)

        let startDate = form.fields_dict.ለአገልግሎት_የሚፈለግበት_ሰዓት__ከዚህ_ጊዜ_ይጀምራል.last_value

        let endDate = form.fields_dict.ለአገልግሎት_የሚፈለግበት_ሰዓት_እስከዚህ_ጊዜ_ድረስ.last_value

        let daysDiff = moment(startDate).diff(endDate,'days',true)

        console.log(daysDiff)
        
        if(daysDiff >= 0) {

            frappe.throw("የጊዜ ቆጠራ ስህተት \n")


        }
        
    },
})


//get list of vehicles

function getVehicles(form,start_date) {
    
    console.log(start_date)
    form.set_query('ተሽከርካሪ_ይምረጡ',function(){


        
        return {

            query: "gondermgt.api.getCars",

            filters: {

                'start_date': start_date,

                'from': 'transport'

            }
        };

    })



}
/*

1. driver -->  stock manager --> completed
2. 

*/