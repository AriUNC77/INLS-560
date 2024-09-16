# This lesson teaches how to test order for else-elif chains
age = 101

if age < 4:
    print("Admission is $8")
elif age < 18:
    print("Admission is $25")
elif age > 60:
    print("Admission is $35")
elif age > 100:
    print("Admission is $0 and you get a free beer!")


# This will not work here. Put it before age > 60
# elif age > 100
#    print("Admission is $0 and you get a free beer!")
else:
    print("Admission cost is $40")