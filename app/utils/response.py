def success_response(data=None, message="Success"):
    return {
        "status": "success",
        "message": message,
        "data": data
    }

def error_response(message="Something went wrong", data=None):
    return {
        "status": "error",
        "message": message,
        "data": data
    }
