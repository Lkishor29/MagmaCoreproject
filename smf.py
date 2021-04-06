import grpc
import sessionset_pb2 as pb
import sessionset_pb2_grpc as pb_grpc
from sessionset_pb2 import SMFSessionRequest

import configManager
import dataInput

channel = grpc.insecure_channel('localhost: 50051')
stub = pb_grpc.PipelinedStub(channel)

print("SMF Loading")
res11 = SMFSessionRequest()
res11.subscriber_id = "10.1.1.1"
rep11 = stub.Add(res11)


info1 = []
info1 = dataInput.dataInputHelper()
print(info1)