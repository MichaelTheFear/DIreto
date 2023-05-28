import re

def validate_email(email:str) -> bool:

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

    if(re.search(regex,email)):
        return True
    
    return False

def send_email(content:str,cat:str) -> None:
    pass