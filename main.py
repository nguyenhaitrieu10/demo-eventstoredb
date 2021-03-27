import json
import requests
from bank import BankAccount, Transaction
from event import AccountCreatedEvent, FundsDepoitedEvent, FundsWithDrawedEvent
import uuid

def streamId(id):
    return "BankAccount-" + str(id)

def main():
    id = str(uuid.uuid4())
    eventsToRun = []
    eventsToRun.append(AccountCreatedEvent(id, "Vincent"))
    eventsToRun.append(FundsDepoitedEvent(id, 150))
    eventsToRun.append(FundsDepoitedEvent(id, 100))
    eventsToRun.append(FundsWithDrawedEvent(id, 60))
    eventsToRun.append(FundsWithDrawedEvent(id, 94))
    eventsToRun.append(FundsDepoitedEvent(id, 4))

    for event in eventsToRun:



main()
