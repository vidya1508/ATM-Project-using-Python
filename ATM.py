def ATM():
    pass
username=['vidya','vamsi','sai','devi']
password=['vidya1','vamsi2','sai3','devi4']
pin=[0000,1111,2222,3333]
balance=[1000,4000,6000,7000] 
print("Enter username:")
a=input()
if(a in username):
    print("Enter password")
    b=input()
    j=username.index(a)
    if(b not in password[j]):
            print("Enter your password Correctly, you have 3 chance(s)")
            b=input()
            j=username.index(a)
            if(b not in password[j]):
              print("Enter your password Correctly, you have 2 chance(s)")
              b=input()
              j=username.index(a)
            elif(b not in password[j]):
                print("Account Blocked")
       
            else:
             print("Enter Your Choice:")
             print("1.Withdrawl")
             print("2.Deposit")
             print("3.Check Balance")
            print("4.Change Password")
            choice=int(input())
            while(1): 
             if choice==1:
               print("withdrawl")
               break
             elif choice==2:
               print("deposit")
               break
             elif choice==3:
              print("check balance")
              break
             elif choice==4:
               print("change password")
               break
             else:
              print("Enter a Valid Choice")
              choice=int(input())

else:
    print("END")
            

    


