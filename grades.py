O = int(input("Enter no. of Subjects with 'O' Grade:"))
S = int(input("Enter no. of Subjects with 'S' Grade:"))
A = int(input("Enter no. of Subjects with 'A' Grade:"))
B = int(input("Enter no. of Subjects with 'B' Grade:"))
C = int(input("Enter no. of Subjects with 'C' Grade:"))
D = int(input("Enter no. of Subjects with 'D' Grade:"))
Labs = int(input("Enter no. of labs:"))
Ol = int(input("Enter no. of labs with 'O' Grade:"))
Sl = int(input("Enter no. of labs with 'S' Grade:"))
Al = int(input("Enter no. of labs with 'A' Grade:"))
Bl = int(input("Enter no. of labs with 'B' Grade:"))
Cl = int(input("Enter no. of labs with 'C' Grade:"))
Dl = int(input("Enter no. of labs with 'D' Grade:"))
Fin_grade = (O*10*3)+(S*9*3)+(A*8*3)+(B*7*3)+(C*6*3)+(D*5*3)+(Ol*10*2)+(Sl*9*2)+(Al*8*2)+(Bl*7*2)+(Cl*6*2)+(Dl*5*2)
if Labs==3:
	print("Your GPA is",Fin_grade/24)
else:
	print("Your GPA is",Fin_grade/22)



