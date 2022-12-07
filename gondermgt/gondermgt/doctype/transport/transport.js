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


//form ui controller
frappe.ui.form.on("transport", {

    onload(form) {

        switch(form.doc.workflow_state) {

            case "Requested":

                getVehicles(form)

                form.toggle_display(['ተሽከርካሪ_ይምረጡ'],true)

                break

            default:

                form.toggle_display(['ተሽከርካሪ_ይምረጡ'],false)
                
                break

        }
/*
        let fields = [

            'ለአገልግሎት_የሚፈለግበት_ሰዓት__ከዚህ_ጊዜ_ይጀምራል',

            'ለአገልግሎት_የሚፈለግበት_ሰዓት_እስከዚህ_ጊዜ_ድረስ',
            
            'የተጓዥ_ስም',

            'የሚሄዱበት_ቦታ',

            'ምክንያት'


        ]

        fields = form.doc.workflow_state != "Draft" && form.doc.workflow_state != "Requested" ? fields = [...fields,'የሹፌር_ስም','የሰሌዳ_ቁጥር'] : fields

        
        
        if(form.doc.workflow_state != "Draft"){

            setFieldsToReadOnly(fields,form)
    
            //form.set_df_property('የሹፌር_ስም','read_only',1)

            //form.set_df_property('የሰሌዳ_ቁጥር','read_only',1)

        }

        if(form.doc.workflow_state == "Requested") {

            form.toggle_display(['ተሽከርካሪ_ይምረጡ'],true)

        }else {


        }
        
        /*
         //getDrivers(form)
         switch(form.doc.workflow_state) {

            case "Request":
                

                break

                
            default:
                
                form.toggle_display(['ተሽከርካሪ_ይምረጡ'],false)

                setFieldsToReadOnly(fields,form)

        }
        */
        /*
        if(form.doc.workflow_state == "Approved") {


            //form.toggle_display(['የተጓዥ_ስም'],false)
            form.set_df_property([], "read_only", 1);

        }   

        */

        /*
        let showStartTripBtn = frappe.user_roles.includes('Guard') && form.doc.workflow_state == "Approved"

        let showTripEndedBtn = frappe.user_roles.includes('Guard') && form.doc.workflow_state == "vehicle has left"

        console.log(showStartTripBtn)

        form.toggle_display(['record_start_of_trip_date'],showStartTripBtn)

        form.toggle_display(['record_vehicle_return_date',showTripEndedBtn])

        showStartTripBtn.addEventListener('click',e => alert('clicked start trip btn'))

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

function getVehicles(form) {

    form.set_query('ተሽከርካሪ_ይምረጡ',() => {

        return {

            query: "gondermgt.api.getCars",

        };

    })



}
/*

1. driver -->  stock manager --> completed
2. 

*/