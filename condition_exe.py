son_of_ceo=False
if son_of_ceo==True:
    print("approved")
else:
    python_grade=int(input("enter your python grade "))
    git_grade=int(input("enter your git grade  "))
    if python_grade >= 85 and git_grade >= 85:
        print("approved")
    elif python_grade >= 90 and 80 <= git_grade <= 85:
        print("approved")
    elif  80 <= git_grade <= 85 and 80 <= python_grade <= 85:
        print("wating list")
    else:
        print("not approved")