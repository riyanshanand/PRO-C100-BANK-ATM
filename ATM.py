class ATM(object):
    def __init__(self, CardNumber,PinNumber):
        self.CardNumber=CardNumber
        self.PinNumber=PinNumber

    def checkBalance(self):
        print("Your Current Balance Rs. 10020")

    def WithDrawal(self,amount):
        r=10020-amount
        print("You have Withdrawal Amount "+str(amount))
        print("Your Remaining Amount is"+str(r))        

a = ATM("4820 4582 5894 5559", 5854)
a.checkBalance()
a.WithDrawal(1000)