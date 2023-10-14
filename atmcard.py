class AtmCard():
    def __init__(self, cardNum, pin, fname, balance):
        self.cardNum = cardNum
        self.pin     = pin
        self.fname = fname
        self.balance = balance

    #defining getter methods
    def get_cardNum(self):
        return self.cardNum
    def get_pin(self):
        return self.pin
    def get_fname(self):
        return self.fname
    def get_balance(self):
        return self.balance
    
    #defining setter methods
    def set_cardNum(self, newval):
        self.cardNum = newval
    def set_pin(self, newval):
        self.pin = newval
    def set_fname(self, newval):
        self.fname = newval
    def set_balance(self, newval):
        self.balance = newval
    