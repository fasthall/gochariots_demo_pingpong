import sys
import grpc
import pingpong_pb2
import pingpong_pb2_grpc

sys.path.append('./gochariots-python-lib')
import gochariots_client

def client(message):
    channel = grpc.insecure_channel('localhost:50051')
    stub = pingpong_pb2_grpc.PingPongStub(channel)
    rpcPing = pingpong_pb2.RPCPing()
    rpcPing.message = message

    seed = 123
    cli = gochariots_client.RPCClient('169.231.235.50:9000')
    record1 = gochariots_client.Record(seed)
    record1.add('first', 'event')
    record1.add('message', message)
    cli.post(record1)

    result = stub.call(rpcPing)
    print(result)

if __name__ == '__main__':
    client(sys.argv[1])