def check_pwd(pwd):
    has_upper = False
    has_lower = False
    if(len(pwd) < 8 or len(pwd) > 20):
        return False
    for c in pwd:
        if c.isupper():
            has_upper = True
        if c.islower():
            has_lower = True


    return has_upper and has_lower

