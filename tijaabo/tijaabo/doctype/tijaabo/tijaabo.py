# Copyright (c) 2025, Yooltech and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Tijaabo(Document):
	pass
@frappe.whitelist()
def fill():
	
	return {
		"magac": "Liban",
		"age": 25,
	}
@frappe.whitelist()
def update(doctype, name):
	name1 = "Liban"
	name2 = "Ali"
	new_name = frappe.rename_doc(doctype,name,name2 if name ==name1 else name1, force=True)

	return new_name
	
	
