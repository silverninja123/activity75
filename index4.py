math=int(input("What is your marks in maths :"))
english=int(input("What is your marks in english :"))
science=int(input("What is your marks in science :"))
average=(math+english+science)/3
if average>=90 and average==100:
    print("A")
elif average>=80 and average<90:
    print("B")
elif average>=70 and average<80:
    print("C")
elif average>=60 and average<70:
    print("D")
elif average>=50 and average<60:
    print("E")
elif average>100:
    print("Invalid input")
else:
    print("You are failed")