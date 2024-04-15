

sourcecode = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
s1=""
s2=""
s3=""
s4=""
s5=""
t4=""
for i in range(len(sourcecode)):
    s1=sourcecode[i]
    for j in range(len(sourcecode)):
        s2=sourcecode[j]
        for k in range(len(sourcecode)):
            s3=sourcecode[k]
            for l  in range(len(sourcecode)):
                s4=sourcecode[l]
                for m in range(len(sourcecode)):
                    s5=sourcecode[m]
                    for n in range(len(sourcecode)):
                        s6=sourcecode[n]
                        t4=s1+s2+s3+s4+s5+s6
                        if(s1==s2==s3==s4==s5==s6):
                            print(t4)
