import string
def swap_case(s):
    ek=' '+string.ascii_letters+string.punctuation+string.digits
    r=''
    for i in s:
        if 65<=ord(i)<=90:
            i=chr(ord(i)+32)
            r+=i
        elif 97<=ord(i)<=122:
            i=chr(ord(i)-32)
            r+=i
        elif i in ek:
            r+=i
    return r


