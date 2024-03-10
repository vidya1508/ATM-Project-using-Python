def withdrwal(i):
    print("Enter Your Amount To Withdraw:")
    amount=int(input())
    print("Enter Your PIN:")
    pincode=int(input())
    if(pincode!=pin[i]):
        print("Incorrect PIN")
        print("END")
    else:
      if(amount>balance[i]):
        print("Insufficient Balance")
      else:
        balance[i]=balance[i]-amount
        print("Withdrawl Successful")
        print("Do You Want to Know your Available Balnce? Yes/No")
        q=input()
        if(q=='No'):
          print("Thank You for Banking, Visit Us Again.")
        else:
          print("The Available Balance is",balance[i])
          print("Thank You for Banking, Visit Us Again.")
def deposit(i):
    print("Enter Your Amount:")
    amount=int(input())
    print("Enter Your PIN:")
    pincode=int(input())
    if(pincode!=pin[i]):
        print("Incorrect PIN")
        print("END")
    else:
        balance[i]=balance[i]+amount
        print("Deposit Successful")
        print("Do You Want to know your Available Balance? Yes/No")
        q=input()
        if(q=='No'):
          print("Thank You for Banking, Visit Us Again.")
        else:
          print("The Available Balance is",balance[i])
          print("Thank You for Banking, Visit Us Again.")
def checkbalance(i):
   print("Enter Your PIN")
   pincode=int(input())
   if(pincode!=pin[i]):
        print("Incorrect PIN")
        print("END")
   else:
       print("Your Available Balance:",balance[i])
       print("Thank You for Banking, Visit Us Again.")
def changepassword(i):
    print("Enter Your Current Password:")
    cp=input()
    while(1):
      if(cp!=password[i]):
        print("Enter Your Correct Password:")
        cp=input()
      else:
         print("Enter Your New Password:",end='')
         np=input()
         print("Re-enter Your New Password:",end='')
         np1=input()
         if(np1!=np):
            print("Password Does'nt Match")
         else:
            password[i]=np
            print("Password Changed Successfully")
            print("Thank You for Banking, Visit Us Again.")
            break
def ATM():
    i=username.index(user_name)
    print("Enter Your Password")
    passcode=input()
    flag=0
    if(passcode!=password[i]):
        print("Incorrect Password,Enter Correct password,only 2 chances left")
        passcode=input()
        if(passcode!=password[i]):
            print("Incorrect Password,Enter Correct password,only 1 chance left")
            passcode=input()
            if(passcode!=password[i]):
                print("Account Blocked")
                print("END")
            else:
                flag=1
        else:
            flag=1
    else:
        flag=1
    if(flag==0):
        print("END")
    else:
        print("Enter Your Choice:")
        print("1.Withdrawl")
        print("2.Deposit")
        print("3.Check Balance")
        print("4.Change Password")
        choice=int(input())
        while(1):
          if(choice not in[1,2,3,4]):
            print("Enter a Valid Choice")
            choice=int(input())
          else:
                if choice==1:
                    print("************withdrawl**************")
                    withdrwal(i)
                    break
                elif choice==2:
                    print("************Deposit************")
                    deposit(i)
                    break
                elif choice==3:
                    print("************Check Balance*************")
                    checkbalance(i)
                    break
                elif choice==4:
                    print("************change Password*************")
                    changepassword(i)
                    break    
username=['vidya','vamsi','sai','devi']
password=['vidya1','vamsi2','sai3','devi4']
pin=[0000,1111,2222,3333]
balance=[1000,4000,6000,7000]
print("Enter Your UserName:")
user_name=input()
if(user_name not in username):
    print("END")
else:
    ATM()
