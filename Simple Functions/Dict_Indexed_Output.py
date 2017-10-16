# If you feed a slice to a dict you can then return the corresponding value but returning a dict within the function.

def get_status(is_busy):
    status = "busy" if is_busy else "available"
    return {"status" : status}

# test:

Test.assert_equals(get_status(True)["status"], "busy")
Test.assert_equals(get_status(False)["status"], "available")

# alt ways to do it:

def get_status(is_busy): return {'status': ("busy" if is_busy else "available")}

def get_status(is_busy):
    return {"status": "busy"} if is_busy else {"status": "available"}
    
def get_status(is_busy):
    return dict(status = "busy" if is_busy else "available")
    
# or:

def get_status(is_busy):
    msg = {}
    msg['status'] = "available"
    if is_busy:
        msg['status'] = "busy"
    return msg
    
# voila
