import json

class EVENT_TYPE():
    ACCOUNTCREATED = "AccountCreatedEvent"
    WITHDRAWED = "FundsWithDrawedEvent"
    DESPOITED = "FundsDepoitedEvent"

class AccountCreatedEvent():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def PayLoad(self, eventId):
        body = [
            {
                "eventId": eventId,
                "eventType": EVENT_TYPE.ACCOUNTCREATED,
                "data": {
                    "id": self.id,
                    "name": self.name,
                }
            }
        ]
        return json.dumps(body)

class FundsDepoitedEvent():
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount
        self.type = EVENT_TYPE.DESPOITED

    def PayLoad(self, eventId):
        body = [
            {
                "eventId": eventId,
                "eventType": EVENT_TYPE.DESPOITED,
                "data": {
                    "id": self.id,
                    "amount": self.amount,
                }
            }
        ]
        return json.dumps(body)

class FundsWithDrawedEvent():
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount
        self.type = EVENT_TYPE.WITHDRAWED

    def PayLoad(self, eventId):
        body = [
            {
                "eventId": eventId,
                "eventType": EVENT_TYPE.WITHDRAWED,
                "data": {
                    "id": self.id,
                    "amount": self.amount,
                }
            }
        ]
        return json.dumps(body)