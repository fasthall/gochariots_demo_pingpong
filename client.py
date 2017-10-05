import sys
import grpc
import pingpong_pb2
import pingpong_pb2_grpc

def client(message):
    channel = grpc.insecure_channel('localhost:50051')
    stub = pingpong_pb2_grpc.PingPongStub(channel)
    rpcPing = pingpong_pb2.RPCPing()
    rpcPing.message = message
    result = stub.call(rpcPing)
    print(result)

if __name__ == '__main__':
    client(sys.argv[1])