# Copyright (c) 2025, Yooltech and contributors
# For license information, please see license.txt

import frappe,random
from frappe.model.document import Document

class Tijaabo(Document):
	pass
@frappe.whitelist()
def is_submittable(doctype):
	meta = frappe.get_meta(doctype)
	if meta.is_submittable():
		return True
	else:
		return False
@frappe.whitelist()
def fill():
	doc = frappe.new_doc("Tijaabo")
	doc.magac = "Liban"
	doc.age = 25
	doc.append("waalid",{
		"magac": "Ali",
		"tel_phone": 617653631
	})
	doc.save()
	return doc.name
	
@frappe.whitelist()
def update(doctype, name):
	name1 = "Liban"
	name2 = "Ali"
	new_nameka = name2 if name ==name1 else name1
	new_name = frappe.rename_doc(doctype,name,new_nameka, force=True)
	doc = frappe.get_doc(doctype, new_name)
	age = random.randint(15, 30)

	doc.age = age
	magac = None
	for waalid in doc.waalid:
		magac = waalid.magac
		if waalid.magac == new_name:
			new_nameka = name1 if name ==name1 else name2
			waalid.magac = new_nameka
			waalid.tel_phone = "617653631"
			status = True
			break
	print() 
	if not magac:
		doc.append("waalid",{
			"magac": new_nameka,
			"tel_phone": "617653631"
		})

	doc.save()
	return doc.name

	doc.save()

		
	return new_name
@frappe.whitelist()
def submit(doctype, name):
	doc = frappe.get_doc(doctype, name)
	if doc.docstatus == 0:
		doc.submit()
	else:
		doc.docstatus = 0
		doc.save()
	return doc.name
@frappe.whitelist()
def cancel(doctype, name):
	doc = frappe.get_doc(doctype, name)
	if doc.docstatus == 1:
		doc.cancel()
	return doc.name
@frappe.whitelist()
def amend(doctype, name):
    doc = frappe.get_doc(doctype, name)
    if doc.docstatus == 2:  # Cancelled
        new_doc = frappe.copy_doc(doc)
        new_doc.amended_from = doc.name
        new_doc.docstatus = 0  # Draft
        new_doc.insert()
        return new_doc.name
    else:
        frappe.throw("Document is not cancelled and cannot be amended.")

	
@frappe.whitelist()
def read_data(doctype, name):
	doc = frappe.get_doc(doctype, name)
	data = {
		"magac": doc.magac,
		"age": doc.age,
		"waalid": []
	}
	for waalid in doc.waalid:
		print("__"*10,"\n",waalid.magac, waalid.tel_phone,"\n","__"*10)
		data["waalid"].append({
			"magac": waalid.magac,
			"tel_phone": waalid.tel_phone
		})
	return data