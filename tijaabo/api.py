import frappe,json
from frappe.auth import LoginManager

session_expiry_time = ""

@frappe.whitelist()
def check_token(token):
    state = False
    try:
        state = frappe.session.sid == token and frappe.utils.get_datetime(session_expiry_time) > frappe.utils.now_datetime()
    except:
        return "Please try to Login"
    if state:
        return True
    else:
        return "Token expired or invalid session"


@frappe.whitelist()
def get_data(token):
    check = check_token(token)
    if check == True:
        return "Hello world"
    return check


@frappe.whitelist(allow_guest=True)
def login(usr=None, pwd=None):
    """Authenticate user and set session expiry."""
    global session_expiry_time
    login_manager = LoginManager()
    login_manager.authenticate(usr, pwd)
    login_manager.post_login()

    user_doc = frappe.get_doc("User", usr)
    roles = [d.role for d in user_doc.get("roles")]

    # Set session expiration time (configurable)
    session_expiry = 600
    session_expiry_time = frappe.utils.add_to_date(frappe.utils.now(), seconds=session_expiry)

    return {
        "message": "Login successful",
        "sid": frappe.session.sid,
        "user": usr,
        "roles": roles,
        "session_expiry_time": session_expiry_time
    }



@frappe.whitelist()
def logout():
    """Logout user and clear session."""
    global session_expiry_time
    session_expiry_time = ""
    frappe.local.login_manager.logout()
    return {
        "message": "Logout successful"
}


@frappe.whitelist()
def create_doctype(data):
    data= json.loads(data)
    print("Data received:", data)
    doc = frappe.get_doc(data)
    doc.flags.ignore_permissions = True
    doc.insert()
    doc.save()
    frappe.db.commit()
    return {
        "message": "Document created successfully",
        "name": doc.name
    }
    
  