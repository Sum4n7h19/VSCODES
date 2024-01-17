# write a program to convert decimal degree into degree,minutes,seconds

dd = float(input("Enter decimal degree: "))
degree = dd // 1
temp = (dd % 1) * 60
minutes = temp // 1
seconds = (temp % 1) * 60
print(f'D:: {int(degree)} ,M:: {int(minutes)}, S:: {seconds}')