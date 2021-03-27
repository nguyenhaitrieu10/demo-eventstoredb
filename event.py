
class EVENT_TYPE():
    WITHDRAWED = 0
    DESPOITED = 1

class AccountCreatedEvent():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class FundsDepoitedEvent():
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount
        self.type = EVENT_TYPE.DESPOITED

class FundsWithDrawedEvent():
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount
        self.type = EVENT_TYPE.WITHDRAWED
