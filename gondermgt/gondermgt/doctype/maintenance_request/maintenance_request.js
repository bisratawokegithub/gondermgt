// Copyright (c) 2022, 360ground and contributors
// For license information, please see license.txt

// frappe.ui.form.on("maintenance request", {
// 	refresh(frm) {
    
// 	},
// });

//

function setReadOnly(fields,form) {

    try {
        
        fields.forEach(field => {
            
            form.set_df_property(field,'read_only',1)
        
        })

    } catch (err) {
        
        frappe.throw(err)
    }

}

//allow users to edit the form
function setWrite(fields,form) {

    try {
        
        fields.forEach(field => {

            form.set_df_property(field,'read_only',0)

        })
    } catch (err) {
        
        frappe.throw(err)
    }

}

// form ui controller
frappe.ui.form.on("maintenance request", {

    onload(form) {
        console.log(form.doc.workflow_state)
        let fields = ['የጥገናዉ_ዓይነት','በሥራ_ላይ_የዋሉ_ማቴሪያሎች__እና_የጉልበት_ዋጋ_ዝርዝር','ፋካሊቲ']
        
        switch(form.doc.workflow_state) {

            
            case "Requested":

                console.log('in requested work flow state')

                //form.toggle_display(['የጥገናዉ_ዓይነት','በሥራ_ላይ_የዋሉ_ማቴሪያሎች__እና_የጉልበት_ዋጋ_ዝርዝር','ፋካሊቲ'],false)
                
                setReadOnly(fields,form)

                return
                
            case "maintenance started":
                
                console.log(frappe.user_roles)

                let isMechanic = frappe.user_roles.includes('mechanic')
                
                console.log(isMechanic)

                if(isMechanic) {

                    let fields = ['በሥራ_ላይ_የዋሉ_ማቴሪያሎች__እና_የጉልበት_ዋጋ_ዝርዝር']

                    setWrite(fields,form)

                }
                
                return

            case "maintenance ended":
                
                setReadOnly(fields,form)

                return
                
            default:

               let field =  'በሥራ_ላይ_የዋሉ_ማቴሪያሎች__እና_የጉልበት_ዋጋ_ዝርዝር'

                form.set_df_property(field,'read_only',1)


        }
        
        if(form.doc.workflow_state =="maintenance started"){

            //frappe.user_roles.includes('head mechanic')


        }

        if(form.doc.workflow_state == "maintenance ended") {

            form.toggle_display(['የጥገናዉ_ዓይነት','በሥራ_ላይ_የዋሉ_ማቴሪያሎች__እና_የጉልበት_ዋጋ_ዝርዝር','ፋካሊቲ'],false)

        }


    },

})

