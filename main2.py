# import json
# import requests
#
# CONFIG_DIR = 'configs/'
# DB_HOST = "node3.eventstore:2113"
# AUTHEN = ('admin', 'changeit')
#
# def createStream(payLoad, stream, version):
#     data = open(payLoad)
#     res = requests.post(
#         url ='https://%s/streams/%s' %(DB_HOST, stream),
#         headers={
#             "Content-Type": "application/vnd.eventstore.events+json",
#             "ES-CurrentVersion": version
#         },
#         data=data,
#         verify=False,
#         auth=AUTHEN
#     )
#     return res
#
# def sendEvents(payLoad, stream, version):
#     data = open(payLoad)
#     res = requests.post(
#         url = 'https://%s/streams/%s' %(DB_HOST, stream),
#         headers={
#             "Content-Type": "application/vnd.eventstore.events+json",
#             "ES-ExpectedVersion": version
#         },
#         data=data,
#         verify=False,
#         auth=AUTHEN
#     )
#     return res
#
# def readStreasm(stream):
#     res = requests.get(
#         url = 'https://%s/streams/%s' %(DB_HOST, stream),
#         headers = {
#             'Accept': 'application/vnd.eventstore.atom+json',
#         },
#         verify=False,
#         auth=AUTHEN
#     )
#     return res
#
#
# def readEvent(stream):
#     res = requests.get(
#         url = 'https://%s/streams/%s/0' %(DB_HOST, stream),
#         headers = {
#             'Accept': 'application/json',
#         },
#         verify=False,
#         auth=AUTHEN
#     )
#     return res
#
#
# def deleteStream(stream):
#     res = requests.delete(
#         url = 'https://%s/streams/%s' %(DB_HOST, stream),
#         headers={
#             'ES-HardDelete': 'true',
#         },
#         verify=False,
#     )
#     return res
#
# def main():
#     stream = "order"
#     # res = createStream("event.json", stream, "0")
#     # print(res.status_code)
#
#     # res = sendEvents("event.json", stream, "2")
#     # print(res.status_code)
#     # print(res.reason)
#
#     # res = readEvent(stream)
#     # print(res.status_code)
#     # with open("out.json", "w") as f:
#     #     json.dump(res.json(), f)
#
#     # res = readStreasm(stream)
#     # print(res.status_code)
#     # with open("out.json", "w") as f:
#     #     json.dump(res.json(), f)
#
#     # response = deleteStream(stream)
#     # print(response.status_code)
#
# main()