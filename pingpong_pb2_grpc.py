# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import pingpong_pb2 as pingpong__pb2


class PingPongStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.call = channel.unary_unary(
        '/PingPong/call',
        request_serializer=pingpong__pb2.RPCPing.SerializeToString,
        response_deserializer=pingpong__pb2.RPCPong.FromString,
        )


class PingPongServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def call(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PingPongServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'call': grpc.unary_unary_rpc_method_handler(
          servicer.call,
          request_deserializer=pingpong__pb2.RPCPing.FromString,
          response_serializer=pingpong__pb2.RPCPong.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'PingPong', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))