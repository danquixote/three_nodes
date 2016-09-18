# three_nodes

I. instructions:

  1. apt-get install python-pip or yum install python-pip
  2. pip install -r requirements.txt
  3. Local-mode:
  
    a) start three instances of the server, the recommended way being:
    ~~~~ 
    chmod +x three_nodes.py
    ./three_nodes.py 127.0.0.1 8081 &
    ./three_nodes.py 127.0.0.2 8082 &
    ./three_nodes.py 127.0.0.3 8083 & 
    ~~~~
    b) you can then use "curl" to request from any of the three "nodes", for examlpe:
    ~~~~ 
    curl http://127.0.0.3:8083/ 
    ~~~~

  4. to run on separate servers, update the ".py" script global varialbe "SERVERS" with the correct addresses and IPs, prior to proceeding to step 3, then, running the python script on each separate physical box or VM.


II. Q & A:

  1. 

