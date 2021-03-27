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

def readStream(stream):
    res = requests.get(
        url = 'https://%s/streams/%s' %(DB_HOST, stream),
        headers = {
            'Accept': 'application/vnd.eventstore.atom+json',
        },
        verify=False,
        auth=AUTHEN
    )
    return res


def readEventAt(stream, position):
    res = requests.get(
        url = 'https://%s/streams/%s/%s' %(DB_HOST, stream, position),
        headers = {
            'Accept': 'application/vnd.eventstore.atom+json',
        },
        verify=False,
        auth=AUTHEN
    )
    return res


def readEventFromTo(stream, fr, to):
    res = requests.get(
        url = 'https://%s/streams/%s/%s/forward/%s' %(DB_HOST, stream, fr, to),
        headers = {
            'Accept': 'application/vnd.eventstore.atom+json',
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

