s=input("Enter a sentence:")
dic={}
lst=s.split()

for i in lst:
    if i[-1]==".":
        i=i[0:len(i)-1]
        lst.append(i)

    elif i in dic:
        dic[i]+=1

    else:
        dic.update({i:1})  

for j in dic:
    print ("Frequency of ", j, end = " ")
    print (":", end = " ")
    print (dic[j], end = " ")
    print ()
