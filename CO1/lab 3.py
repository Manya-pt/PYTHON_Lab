sen=input("Enter any Sentence:")
name=sen.split()
print(name)
for i in name:
    print(f"{i} occurs {name.count(i)} times..")
