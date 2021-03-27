import json
import requests
from bank import BankAccount
from event import AccountCreatedEvent, FundsDepoitedEvent, FundsWithDrawedEvent
import eventstoredb
import uuid

def streamId(id):
    return "BankAccount-" + str(id)

def main():
    # aggregateId = "6d397bd4-f095-405e-b3bb-75ff3d7a763b"
    aggregateId = str(uuid.uuid4())
    eventsToRun = []
    eventsToRun.append(AccountCreatedEvent(aggregateId, "Vincent"))
    eventsToRun.append(FundsDepoitedEvent(aggregateId, 150))
    eventsToRun.append(FundsDepoitedEvent(aggregateId, 100))
    eventsToRun.append(FundsWithDrawedEvent(aggregateId, 60))
    eventsToRun.append(FundsWithDrawedEvent(aggregateId, 94))
    eventsToRun.append(FundsDepoitedEvent(aggregateId, 4))

    stream = streamId(aggregateId)
    for event in eventsToRun:
        eventId = str(uuid.uuid4())
        print(eventId)
        data = event.PayLoad(eventId)
        res = eventstoredb.sendEvents(data, stream)
        print(res.status_code)

    # Read all events from BankAccount stream
    res = eventstoredb.readAllEvents(stream)
    print(res.status_code)
    results = res.json()
    print(results)
    with open("output.json", "w") as f:
        json.dump(results, f)

    # Aggregate all transactions
    bankAccount = BankAccount()


main()
