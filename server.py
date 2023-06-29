import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

def exposed_search(self, data):
    return [item for item in self.value if item == data]

def exposed_sort(self, data):
  DBLength = len(DBList)
  for i in range(DBLength):
      swapped = False
      for j in range(0, DBLength-i-1):
          if DBList[j] > DBList[j+1]:
              DBList[j], DBList[j+1] = DBList[j+1], DBList[j]
              swapped = True
      if (swapped == False):
          break

def exposed_remove(self, data):
    self.value = [item for item in self.value if item != data]
    return self.value

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

