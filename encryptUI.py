
def CeaserCipher(): # needs fixing,issue is replacing encryptrd messages as well
    info = message.get()
    alp1 = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(info)):
        info = info[0:i]+info[i].replace(info[i],alp1[(alp1.find(info[i])+3)%26])+info[i+1:len(info)]
    msg.config(text=info)

def Modified_Ceaser_Cipher(): 
    info = message.get()
    key = int(enc_key.get())
    alp1 = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(info)):
        info = info[0:i]+info[i].replace(info[i],alp1[(alp1.find(info[i])+key)%26])+info[i+1:len(info)]
    msg.config(text=info)

def RailFence():
    main_list = []
    mssg = message.get()
    key = int(enc_key.get())
    n = len(mssg)
    for i in range(key): # creating an empty matrix to fill the letters
        li = []
        for j in range(n):
            li.append(0)
        main_list.append(li)
    i = 0
    flag = True
    for j in range(n): # for creating a pattern like this : 0 1 2 1 0 1 2 1 0 ...
        main_list[i][j] = mssg[j]
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
    msg.config(text=new_msg)

def Columner():
    mssg = message.get()
    key = enc_key.get()
    a=[]
    for i in range(0,len(mssg),len(key)):
        a.append(mssg[i:i+3])
    encrypted_msg=""
    for i in range(len(key)):
        for j in range(int(len(mssg)/len(key))):
            encrypted_msg +=a[j][key.find(str(i+1))]
    msg.config(text=encrypted_msg)


def poly_alphabetic():
    info = message.get()
    keyword = enc_key.get()
    if len(info)<len(keyword):
        return 
    alph = "abcdefghijklmnopqrstuvwxyz"
    key = ""

    # Key generator
    for i in range(len(info)):
        key=key+keyword[i%len(keyword)]
    x = []
    for i in range(26):
        x.append(alph[i:26]+alph[0:i])
    mssg=""
    for i in range(len(info)):
        mssg = mssg + x[alph.find(info[i])][alph.find(key[i])]
    msg.config(text=mssg)


def mono_alphabetic():
    mssg = message.get()
    mono_alp=enc_key.get()
    main_alp="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(mssg)):
        mssg = mssg[0:i] + mssg[i].replace(mssg[i],mono_alp[main_alp.find(mssg[i])]) + mssg[i+1:len(mssg)]
    msg.config(text=mssg)
import tkinter as tk
 
def encrypt():
    num1 = message.get()
    k = int(enc_key.get())
    result = CeaserCipher(num1,k)
    msg.config(text=result)
 
 
# create the main window
root = tk.Tk()
root.title("Parth Patwari 2030")
 
# create the widgets
text_label = tk.Label(root, text="Enter text :",font=30)
message = tk.Entry(root)
key_label = tk.Label(root, text="Key :",font=30)
enc_key = tk.Entry(root)
#buttons
cc_button = tk.Button(root, text="Ceacer Chiper", command=CeaserCipher)
mcc_button = tk.Button(root, text = "M. Ceacar Chiper", command=Modified_Ceaser_Cipher)
rail_button = tk.Button(root, text = "Rail Fence",command=RailFence)
column_button = tk.Button(root, text = "Columnar",command=Columner)
monoalpha_button = tk.Button(root, text = "Mono Alphabetic",command=mono_alphabetic)
polyalpha_button = tk.Button(root,text = "Poly-alphabetic",command=poly_alphabetic)

result_label = tk.Label(root, text="Result:",font=30)
msg = tk.Label(root,text="",font=20)

# layout the widgets
root.geometry("270x400")
text_label.grid(row=0, column=0, sticky="e")
message.grid(row=0, column=1)
key_label.grid(row=1,column=0)
enc_key.grid(row=1,column=1)

#button location
cc_button.grid(row=2, column=0)#,columnspan=2, pady=10)
mcc_button.grid(row = 3, column=0)
rail_button.grid(row = 4, column=0)
column_button.grid(row = 5, column=0)
monoalpha_button.grid(row=6,column = 0)
polyalpha_button.grid(row=7,column=0)

result_label.grid(row=9, column=0)# columnspan=2)
msg.grid(row=9,column=1)
 
# run the main loop
root.mainloop()
