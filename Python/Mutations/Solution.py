def mutate_string(string, position, character):
    sl=[]
    for i in string:
        sl.append(i)
    sl[position]=character
    sn=''.join(sl)
    return sn

