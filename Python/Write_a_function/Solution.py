def is_leap(year):
    leap = False
    L=True
    NL=False
    # Write your logic here
    if 1900<=year<=100000:
        if year%4==0:
            if year%100==0:
                if year%400==0:leap=L
                else:leap=NL
            else:leap=L
        else:leap=NL
    return leap

