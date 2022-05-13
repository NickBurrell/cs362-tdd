def check_pwd(pwd):
    has_upper  = False
    has_lower  = False
    has_digit  = False
    has_symbol = False
    if(len(pwd) < 8 or len(pwd) > 20):
        return False
    for c in pwd:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        elif c in "~`!@#$%^&*()_+-=":
            has_symbol = True
        else:
            return False

    return has_upper and has_lower and has_digit and has_symbol

