python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. sessionset.proto

sudo mn -c
sudo python3 miniTopology.py
ryu-manager ryuControl.py

h1 ping h2


//upf -> listening
//smf -> sends ip add to upf
//upf -> calls configManager.py -> configManager.py-> writes in congig.ini


#ryuControl.py -> calls dataInput.py-> dataInput.py calls configManager.py-> reads config.ini and returns a list of ip addresses. -> ryuController checks if the ip address request coming to switch is present in the list or not. If present forwards its, else blocks it.


mininetTopology:
smf - upf:

add the host address in a config file

switch ------------------------- switch
  |                                |
host(192.168.1.1/24)       host(192.168.1.2/24)

