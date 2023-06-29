import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print (conn.root.exposed_value())
  conn.root.exposed_append(5)       # Call an exposed operation,
  conn.root.exposed_append(6)
  conn.root.exposed_append(12)
  conn.root.exposed_append(8)
  conn.root.exposed_append(2)
  print (conn.root.exposed_value())   # Print the result
  print (conn.root.exposed_remove(2))
  print (conn.root.exposed_search(2))
  conn.root.exposed_sort()
  print (conn.root.exposed_value()) 
