def check_pwd(pwd):
    has_upper = False
    if(len(pwd) < 8 or len(pwd) > 20):
        return False
    for c in pwd:
        if c.isupper():
            has_upper = True

    return has_upper

