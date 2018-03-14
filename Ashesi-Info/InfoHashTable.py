class HashTable:
    #Initialize a hash table with size 2001 and a load factor of 0.6
    def __init__(self):
        self.size = 2001
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.items = 0
        self.loadFactor = 0.6

    #Method to put data into hashtable
    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))
      

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
        self.items += 1
        self.reSize()
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
            self.items += 1
            self.reSize()
          else:
            self.data[nextslot] = data 

    #Method to resize hashtable so that it does not exceed the load factor
    def reSize(self):
        if (self.items/self.size) > self.loadFactor:
            self.size = self.items/self.loadFactor
            
    #Method to generate a hash function for storing the key
    def hashfunction(self,key,size):
        Sum = 0
        if key is str:
            for pos in range(len(key)):
               Sum += (ord(key[pos])*pos)


        return Sum%size

    # Method to rehash in the case of collisions
    def rehash(self,oldhash,size):
        return (oldhash+3)%size


    # Method to get data from hashtable
    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    # Special method to use python's get functionality
    def __getitem__(self,key):
        return self.get(key)

    # Special method to use python's set functionality
    def __setitem__(self,key,data):
        self.put(key,data)







