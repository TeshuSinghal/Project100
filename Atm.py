class Atm(object):
    def __init__(self, atm_card_number, pin_number):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number

    def cashWithdrawl(self):
        print("Cash Withdrawn")

    def balanceEnquiry(self):
        print("Balance is Rs. 1000000")

    def billPayment(self):
        print("Payment successfully done")

    def makeDeposits(self):
        print("Money deposited successfully")

    def requestForChequeBook(self):
        print("Cheque book request placed")
