f=open("5.txt","w")
seq=["First Line\n","Second Line\n","Third Line\n","Fourth Line\n"]
f.writelines(seq)
f.close()
f=open("5.txt","r")
line=f.readlines()
print("Line:",line)
f.close()
