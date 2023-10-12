def Ceaser_Cipher(info): 
    alp1 = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(info)):
        info = info[0:i]+info[i].replace(info[i],alp1[(alp1.find(info[i])+3)%26])+info[i+1:len(info)]
    return info



def Modified_Ceaser_Cipher(info,key): 
    alp1 = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(info)):
        info = info[0:i]+info[i].replace(info[i],alp1[(alp1.find(info[i])+key)%26])+info[i+1:len(info)]
    return info

def RailFence(msg,key):
    main_list = []
    n = len(msg)
    for i in range(key): # creating an empty matrix to fill the letters
        li = []
        for j in range(n):
            li.append(0)
        main_list.append(li)
    i = 0
    flag = True
    for j in range(n): # for creating a pattern like this : 0 1 2 1 0 1 2 1 0 ...
        main_list[i][j] = msg[j]
        if flag:
            i+=1
        else:
            i-=1
        if i == key-1 or i == 0:
            flag = not flag
    new_msg = ""
    for i in range(key):
        for j in range(n):
            if type(main_list[i][j]) == type(str()):
                new_msg += main_list[i][j]
    return new_msg

def Columner(msg,key):
    a=[]
    for i in range(0,len(msg),len(key)):
        a.append(msg[i:i+3])
    encrypted_msg=""
    for i in range(len(key)):
        for j in range(int(len(msg)/len(key))):
            encrypted_msg +=a[j][key.find(str(i+1))]
    return encrypted_msg


def poly_alphabetic(message,keyword):
    if len(message)<len(keyword):
        return 
    alph = "abcdefghijklmnopqrstuvwxyz"
    key = ""
    for i in range(len(message)):
        key=key+keyword[i%len(keyword)]
    x = []
    for i in range(26):
        x.append(alph[i:26]+alph[0:i])
    msg=""
    for i in range(len(message)):
        msg = msg + x[alph.find(message[i])][alph.find(key[i])]
    return msg


def mono_alphabetic(msg):
    mono_alp="qwertyuioplkjhgfdsazxcvbnm"
    main_alp="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(msg)):
        msg = msg[0:i] + msg[i].replace(msg[i],mono_alp[main_alp.find(msg[i])]) + msg[i+1:len(msg)]
    return msg

msg = mono_alphabetic("secretmessage")
print("Encrypted Message :",msg)
