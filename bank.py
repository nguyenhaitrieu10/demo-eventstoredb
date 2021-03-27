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
        if event["eventType"] == EVENT_TYPE.ACCOUNTCREATED:
            self.id = event["data"]["id"]
            self.name = event["data"]["name"]
            self.balance = 0
        elif event["eventType"] == EVENT_TYPE.DESPOITED:
            transaction = Transaction(id=event["data"]["id"], amount=event["data"]["amount"])
            self.transactions.append(transaction)
            self.balance += event["data"]["amount"]
        elif event["eventType"] == EVENT_TYPE.WITHDRAWED:
            transaction = Transaction(id=event["data"]["id"], amount=event["data"]["amount"])
            self.transactions.append(transaction)
            self.balance -= event["data"]["amount"]








