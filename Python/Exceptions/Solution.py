# Enter your code here. Read input from STDIN. Print output to STDOUT
ipn=[];
while True:
    try:
        ipn.append(input());
    except EOFError:
        break;
ntc=int(ipn[0]);
tc=[];
for j in range(1,len(ipn)):
    tc.append(ipn[j].split(' '));
for i in range(ntc):
    try:
        print(int(int(tc[i][0])//int(tc[i][1])));
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero');
    except ValueError:
        if tc[i][0].isdigit() == False:
            ec=tc[i][0];
        elif tc[i][1].isdigit() == False:
            ec=tc[i][1];
        print('Error Code: invalid literal for int() with base 10: \'',ec,'\'',sep='');
