// Copyright (c) 2025, Yooltech and contributors
// For license information, please see license.txt

frappe.ui.form.on("Tijaabo", {
	refresh(frm) {
        if(frm.doc.__unsaved == 1){
            frm.add_custom_button(__('Fill'),function(){
                frappe.call({
                    method: "tijaabo.tijaabo.doctype.tijaabo.tijaabo.fill",
                    callback(r){
                        if(r.message){
                            res = r.message;
                            console.log(res);
                            for(key in res){
                                frm.set_value(key,res[key]);
                            }
                            frm.save();
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

    },
});
