# Checks if a password is strong enough
# Done

import re


def detect_password_strength(password):
    if not re.compile('.{8,}', re.DOTALL).search(password):
        return "Password requires at least 8 characters!"
    elif not re.compile('.*[A-Z].*', re.DOTALL).search(password):
        return "Password requires at least one uppercase character!"
    elif not re.compile('.*[a-z].*', re.DOTALL).search(password):
        return "Password requires at least one lowercase character!"
    elif not re.compile('.*[\d].*', re.DOTALL).search(password):
        return "Password requires at least 1 digit!"
    return "Password looks good!"


print(detect_password_strength('AbiaoaJHFGfhb821'))  # "Password looks good!"
print(detect_password_strength('Pass300'))  # "Password requires at least 8 characters!"
print(detect_password_strength('password77'))  # "Password requires at least one uppercase character!"
print(detect_password_strength('CHAMEL30N'))  # "Password requires at least one lowercase character!"
print(detect_password_strength('PaSsWoRdd'))  # "Password requires at least 1 digit!"
