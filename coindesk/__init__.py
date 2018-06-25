
import os
import codecs
import grpc

from coindesk import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc

os.environ.setdefault("GRPC_SSL_CIPHER_SUITES", "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256")

def stub():
    creds = grpc.ssl_channel_credentials(open(settings.CERT_PATH).read())
    channel = grpc.secure_channel(settings.LND_RPCHOST, creds)
    print(channel)
    stub = lnrpc.LightningStub(channel)
    print(stub)
    return stub


def macaroon():
    with open(os.path.expanduser('~/.lnd/admin.macaroon'), 'rb') as f:
        macaroon_bytes = f.read()
        macaroon = codecs.encode(macaroon_bytes, 'hex')
    print(macaroon)
    return macaroon