from bottle import request, response
from icecream import ic
import re

##############################
def disable_cache():
    response.add_header("Cache-Control", "no-cache, no-store, must-revalidate")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)   

##############################
USER_NAME_MIN = 2
USER_NAME_MAX = 20
USER_NAME_REGEX = "^.{2,20}$"

def validate_user_name():
    try:
        error = f"user_name {USER_NAME_MIN} to {USER_NAME_MAX} characters"
        user_name = request.forms.get("user_name", "")
        user_name = user_name.strip()
        if not re.match(USER_NAME_REGEX, user_name): raise Exception(400, error)
        return user_name
    except Exception as ex:
        ic(ex)
        raise Exception(500, ex)


##############################
USER_LAST_NAME_MIN = 2
USER_LAST_NAME_MAX = 20
USER_LAST_NAME_REGEX = "^.{2,20}$"

def validate_user_last_name():
    try:
        error = f"user_last_name {USER_LAST_NAME_MIN} to {USER_LAST_NAME_MAX} characters"
        user_last_name = request.forms.get("user_last_name", "")
        user_last_name = user_last_name.strip()
        if not re.match(USER_LAST_NAME_REGEX, user_last_name): raise Exception(400, error)
        return user_last_name
    except Exception as ex:
        ic(ex)
        raise Exception(500, ex)    