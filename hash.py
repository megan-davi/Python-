class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size  # key
        self.data = [None] * self.size   # value

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
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
          else:
            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

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

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def __len__(self):
        "Returns the number of key-value pairs in the map"
        count = 0
        for i in self.slots:
            if i != None:
                count += 1
        return count

    def __contains__(self, slots):
        "Returns true if a specified value is associated with a key"
        return slots in self.slots

    def __delitem__(self, slots):
        "Deletes data given a key"
        "Not currently working"
        print ("Deleted")
        
        if slots in self.slots:
            slots = None
        else:
            print ("Key provided doesn't exist")
        
                

        

         

H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"

print("Keys:")
print(H.slots)
print()
print("Values:")
print(H.data)

print()
print("Is 1 in the hash table?", 1 in H)
print("Is 55 in the hash table?", 55 in H)
print()
print("Number of key-value pairs is:", len(H))

