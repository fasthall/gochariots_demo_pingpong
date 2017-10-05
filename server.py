from concurrent import futures
import time
import grpc
import pingpong_pb2
import pingpong_pb2_grpc

class PingPongServicer(pingpong_pb2_grpc.PingPongServicer):
    def __init__(self):
        pass
    
    def call(self, request, context):
        message = request.message
        return pingpong_pb2.RPCPong(message = 'hello, ' + message)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pingpong_pb2_grpc.add_PingPongServicer_to_server(PingPongServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()