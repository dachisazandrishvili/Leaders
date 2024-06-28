#card info
#GE71TB7277545061100086 TBC
#GE61BG0000000586743691 საქართველოს ბანკი:


#ვქმნით ფუნქციას ექაუნტის შესაქმნელად


info = []
tbs = []
geo = []
mainInfo = []
password = []

#writing the function of controls
def control():
  m = input("what do you whant to do? ")
  if m == "createAccount":
    createAccount()
  elif m == "transferMoney":
    transferMoney()
  elif m == "deleteAccount":
    deleteAccount()
  elif m == "deposite":
    deposite()
  elif m == "updateUserInfo":
    updateUaerInfo()
  elif m == "deleteAccount":
    deleteAccount()
  else:
    print("we dont have that command: ")

#writing the function of money transfer
def transferMoney():
  k = input("do you have an account? ")
  if k == "yes":
    k = input("enter password: ")
    if len(password) > 0 and password[0] == k:
      j = input("enter card number, whom do you whant to transfer money? ")
      if j in tbs == True or j in geo == True:
        print("you cant transfer to your own bank account :)))")
      else:
        for i in j:
          if len(j) == 22 or len(j) == 23:
            if i == "T" or i == "B" or i == "B" or i == "G":
              h = int(input("hoe much money do you whant to transfer? "))
              if h > info[-1]:
                print("you dont have that much")
              else:
                count = info[-1]
                count -= h
                info.remove(info[-1])
                info.insert(-1,count)
              print(info)

          else:
            print("inviled card number")
    else:
      print("inviled password")
      u = input("do you whant to create an account? ")
      if u == "yes":
        createAccount()
        j = input("enter card number, whom do you whant to transfer money? ")
        if j in tbs == True or j in geo == True:
          print("you cant transfer to your own bank account :)))")
        else:
          for i in j:
            if len(j) == 22 or len(j) == 23:
              if i == "T" or i == "B" or i == "B" or i == "G":
                h = int(input("hoe much money do you whant to transfer? "))
                if h > info[-1]:
                  print("you dont have that much")
                else:
                  count = info[-1]
                  count -= h
                  info.remove(info[-1])
                  info.insert(-1,count)
                print(info)
                break
            else:
              print("inviled card number")

      


    
#writing the function of delating account
def deleteAccount(): 
  m = input("are you shure,you whant to delate an account? ")
  if m == "yes":
    k = input("do you have an account? ")
    if k == "yes":
      b = input("enter password: ")
      if password[0] != b or len(password) == 0:
        print("as i see, you have alrady lost your account :))) ")
        w = input("do you whant to create new one? ")
        if w == "yes":
          createAccount()

#writing the function of a deposit
def deposite():
  q = input("do you have an account? ")
  if q == "yes":
    p = input("enter password: ")
    if password[0] == p:
      d = int(input("how nuch do you whant to make a deposit? "))
      count = info[-1]
      count += d
      info.remove(info[-1])
      info.insert(-1,count)
    else:
      print("inviled password: ")
      j = input("do you whant to create account? ")
      if j == "yes":
        createAccount()
        d = int(input("how nuch do you whant to make a deposit? "))
        count = info[-1]
        count += d
        info.remove(info[-1])
        info.insert(-1,count)
    print(info)

  elif q == "no":
    createAccount()
    d = int(input("how nuch do you whant to make a deposit? "))
    count = info[-1]
    count += d
    info.remove(info[-1])
    info.insert(-1,count)

#writing the function of an update
def update():
  b = input("what information do you whant to update? ")
  if b == "userName":
    newName2 = input("enter your name: ")
    newSurnam2 = input("enter your surname: ")
    newUsername2 = newName2 + " " + newSurnam2
    info.remove(info[0])
    info.insert(0,newUsername2)
  elif b == "bankNumber":
    newBankNum= input("enter your new bankNum: ")
    info.remove(info[1])
    info.insert(1,newBankNum)
  else:
    print("we don't understand, what do you whant to change")
  print(info)

#wriring function of an adding money
def putMoney():
  count = 0
  a = int(input("how much money do you whabt to put on your banck account? "))
  count += a
  info.append(count)
#writing function of a account creator
def createAccount():
  name = input("whats your name: ")
  surname = input("enter your surname: ")
  bnc = input("enter your card info: ")
  a = name+ " " + surname
  info.append(a)
  pasd = input("set your password: ")
  conf = input("confirm your password: ")
  if pasd == conf:
    password.append(conf)
  else:
    print("inviled password: ")
  for i in bnc:
    if len(bnc) == 22 or len(bnc) == 23:
      if i == "T" or i == "B":
        tbs.append(bnc)
      elif i == "B" or i == "G":
        geo.append(bnc)
    else:
      print("inviled card number")
  if(len(tbs) > len(geo)):
    info.append(tbs[0])
  else:
    info.append(geo[0])
  putMoney()
  print(info)
    

def updateUaerInfo():
  quest = input("do you have an account? ")
  if quest == "yes":
    ps = input("enter password: ")
    if ps == password:
      update()
    else:
      print("inviled password")
      k = input("do you whant to create account? ")
      if k == "yes":
        createAccount()
        update()
  elif quest == "no" or quest == "No":
    createAccount()
    update()





    





control()