import json
import requests

DB_HOST = "node3.eventstore:2113"
AUTHEN = ('admin', 'changeit')

def sendEvents(data, stream):
    res = requests.post(
        url='https://%s/streams/%s' % (DB_HOST, stream),
        headers={
            "Content-Type": "application/vnd.eventstore.events+json",
        },
        data=data,
        verify=False,
        auth=AUTHEN
    )
    return res

def readAllEvents(stream):
    res = requests.get(
        url = 'https://%s/streams/%s/0/forward/999' %(DB_HOST, stream),
        headers = {
            'Accept': 'application/vnd.eventstore.atom+json',
        },
        verify=False,
        auth=AUTHEN
    )
    return res

def readStreasm(stream):
    res = requests.get(
        url = 'https://%s/streams/%s' %(DB_HOST, stream),
        headers = {
            'Accept': 'application/vnd.eventstore.atom+json',
        },
        verify=False,
        auth=AUTHEN
    )
    return res


def readEvent(stream):
    res = requests.get(
        url = 'https://%s/streams/%s/0' %(DB_HOST, stream),
        headers = {
            'Accept': 'application/json',
        },
        verify=False,
        auth=AUTHEN
    )
    return res


def deleteStream(stream):
    res = requests.delete(
        url = 'https://%s/streams/%s' %(DB_HOST, stream),
        headers={
            'ES-HardDelete': 'true',
        },
        verify=False,
    )
    return res

def demo():
    stream = "order"
    # res = createStream("event.json", stream, "0")
    # print(res.status_code)

    # res = sendEvents("event.json", stream, "2")
    # print(res.status_code)
    # print(res.reason)

    # res = readEvent(stream)
    # print(res.status_code)
    # with open("out.json", "w") as f:
    #     json.dump(res.json(), f)

    # res = readStreasm(stream)
    # print(res.status_code)
    # with open("out.json", "w") as f:
    #     json.dump(res.json(), f)

    # response = deleteStream(stream)
    # print(response.status_code)

