// Copyright (c) 2025, Yooltech and contributors
// For license information, please see license.txt

frappe.ui.form.on("Tijaabo", {
	refresh(frm) {
        frappe.meta.get_docfield("Fee", "month", frm.doc.name).options = ["Jaunary", "Febauray", "March"];
        
        if (frm.meta.is_submittable ) {

            if(frm.doc.docstatus == 0 ){
                frm.add_custom_button(__('Submit'),function(){
                    frappe.call({
                        method: "tijaabo.tijaabo.doctype.tijaabo.tijaabo.submit",
                        args: {
                            doctype : "Tijaabo",
                            name: frm.doc.magac,
                        },
                        callback(r){
                            if(r.message){
                                console.log(r.message)
                                frappe.set_route("Form", "Tijaabo", r.message); // 🔁 Redirect to new form
                           
                            } 
                        } })
                })
            } 
            else if(frm.doc.docstatus == 1){
                frm.add_custom_button(__('Cancel'),function(){
                    frappe.call({
                        method: "tijaabo.tijaabo.doctype.tijaabo.tijaabo.cancel",
                        args: {
                            doctype : "Tijaabo",
                            name: frm.doc.magac,
                        },
                        callback(r){
                            if(r.message){
                                console.log(r.message)
                                frappe.set_route("Form", "Tijaabo", r.message); // 🔁 Redirect to new form
                           
                            } 
                        } })
                })
            }
            else if(frm.doc.docstatus == 2){
                frm.add_custom_button(__("Amend"),function(){
                    frappe.call({
                        method: "tijaabo.tijaabo.doctype.tijaabo.tijaabo.amend",
                        args: {
                            doctype : "Tijaabo",
                            name: frm.doc.magac,
                        },
                        callback(r){
                            if(r.message){
                                console.log(r.message)
                                frappe.set_route("Form", "Tijaabo", r.message); // 🔁 Redirect to new form
                           
                            } 
                        }
                    })
                });
            }
        }
        if(frm.doc.__unsaved == 1){
            frm.add_custom_button(__('Fill'),function(){
                frappe.call({
                    method: "tijaabo.tijaabo.doctype.tijaabo.tijaabo.fill",
                    callback(r){
                        if(r.message){
                            res = r.message;
                            frappe.set_route("Form", "Tijaabo", res); // 🔁 Redirect to new form
                           
                        } 
                    }
                })
            })
        }
        else{
            frm.add_custom_button(__('Update'),function(){
                frappe.call({
                    method: "tijaabo.tijaabo.doctype.tijaabo.tijaabo.update",
                    args: {
                        doctype : "Tijaabo",
                        name: frm.doc.magac,
                    },
                    callback(r){
                        if(r.message){
                            console.log(r.message)
                            frappe.set_route("Form", "Tijaabo", r.message); // 🔁 Redirect to new form
                       
                        } 
                    } })
            })
        }

        frm.add_custom_button(__('Read Data'),function(){
            frappe.call({
                method: "tijaabo.tijaabo.doctype.tijaabo.tijaabo.read_data",
                args: {
                    doctype : "Tijaabo",
                    name: frm.doc.magac,
                },
                callback(r){
                    if(r.message){
                        res = r.message;
                        for(xog in res){
                            console.log(xog, res[xog])
                        }
                   
                    } 
                } })
        }
        )   

    },
});
