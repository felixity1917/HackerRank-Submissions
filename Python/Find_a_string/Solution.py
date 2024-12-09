def count_substring(st, sb):
    cc=0
    ms=''
    for i in range(len(sb)):
        j=sb[i]
        ms+=j
    for i in range(len(st)):
        ts=''
        for j in range(len(sb)):
            try:
                k=st[i+j]
                ts+=k
            except IndexError:
                break
        if ts == ms:
            cc+=1
    return cc
