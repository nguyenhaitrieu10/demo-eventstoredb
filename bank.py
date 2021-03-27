from event import EVENT_TYPE

class Transaction():
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount

class BankAccount():
    def __init__(self):
        self.id = ""
        self.name = ""
        self.balance = 0
        self.transactions = []

    def apply(self, event):
        transaction = Transaction(id=event.id, amount=event.amount)
        self.transactions.append(transaction)
        if event.type == EVENT_TYPE.ACCOUNTCREATED:
            self.id = event.id
            self.name = event.name
            self.balance = 0
        elif event.type == EVENT_TYPE.DESPOITED:
            self.balance += event.amount
        elif event.type == EVENT_TYPE.WITHDRAWED:
            self.balance -= event.amount








