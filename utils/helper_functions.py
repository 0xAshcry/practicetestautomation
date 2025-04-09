def get_test_data():
    return {
        "username": "student",
        "password": "Password123"
    }
def get_test_data_invalid():
    return {
        "username": "student",
        "password": "wrong_password"
    }
def get_test_data_empty():
    return {
        "username": "",
        "password": ""
    }
def get_test_data_invalid_username():
    return {
        "username": "invalid_user",
        "password": "Password123"
    }
def get_test_data_invalid_password():
    return {
        "username": "student",
        "password": "invalid_password"
    }
def get_test_data_special_characters(): 
    return {
        "username": "@student!",
        "password": "#Password123$"
    }
def get_test_data_long_username():  
    return {
        "username": "a" * 256,
        "password": "Password123"
    }
def get_test_data_long_password():
    return {
        "username": "student",
        "password": "a" * 256
    }
def get_test_data_sql_injection():      
    return {
        "username": "' OR '1'='1",
        "password": "' OR '1'='1"
    }
def get_test_data_xss_attack():     
    return {
        "username": "<script>alert('XSS')</script>",
        "password": "<script>alert('XSS')</script>"
    }
def get_test_data_valid_credentials():
    return {
        "username": "valid_user",
        "password": "valid_password"
    }
def get_test_data_invalid_credentials():
    return {
        "username": "invalid_user",
        "password": "invalid_password"
    }
def get_test_data_empty_username():
    return {
        "username": "",
        "password": "valid_password"
    }
def get_test_data_empty_password():
    return {
        "username": "valid_user",
        "password": ""
    }