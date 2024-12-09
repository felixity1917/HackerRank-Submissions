if __name__ == '__main__':
    s = input()
    an=ap=di=il=iu=0
    for i in s:
        if i.isalnum():
            an=1
        if i.isalpha():
            ap=1
        if i.isdigit():
            di=1
        if i.islower():
            il=1
        if i.isupper():
            iu=1
    if an==1:
        print(True)
    else:
        print(False)
    if ap==1:
        print(True)
    else:
        print(False)
    if di==1:
        print(True)
    else:
        print(False)
    if il==1:
        print(True)
    else:
        print(False)
    if iu==1:
        print(True)
    else:
        print(False)
    
