import grpc
from concurrent import futures
import time

#import _pb2 files
import sessionset_pb2 as pb
import sessionset_pb2_grpc as pb_grpc
from sessionset_pb2 import SMFSessionRequest
from sessionset_pb2 import UPFSessionResponse

import configManager

from collections import OrderedDict
od = {}
idx = 0

class PipelinedServicer(pb_grpc.PipelinedServicer):

	def Add(self, request, contest):
		global od
		global idx
		od[idx] = request
		idx += 1
		print(od)
		print("OD[idx]: ",od[0])
		configManager.writeConfig(od)
		r = UPFSessionResponse()
		r.subscriber_id = request.subscriber_id
		return r



def main():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	pb_grpc.add_PipelinedServicer_to_server(PipelinedServicer(), server)
	print("starting server, listening on port 50051")
	server.add_insecure_port('[::]:50051')
	server.start()
	try:
		while True:
			time.sleep(86400)
	except KeyboardInterrupt:
		server.stop(0)

if __name__ == "__main__":
	main()