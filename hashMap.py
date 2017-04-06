class KeyValue:
    def __init__(self,key,value):
        self.key=key
        self.value=value
    def __str__(self):
        return self.key+":"+str(self.value)
class HashTable:
    SIZE=10
    def __init__(self):
        self.list=[]
        while len(self.list)<=self.SIZE:
            self.list.append([])
    
    def getValue(self,key):
        h = self.hash (key)
        bucket = self.list[h]
        for kv in bucket:
            if kv.key==key:
                return kv.value
     
    def getIndex(self,key):
        h = self.hash (key)
        bucket = self.list[h]
        for index,kv in enumerate(bucket):
            if kv.key==key:
                return index       

    def putValue(self,key,value):
        h = self.hash(key)
        index=self.getIndex(key)
        

        if index!=None:
            self.list[h].pop(index)

        self.list[h].append(KeyValue(key,value))
        
    def hash(self,key):
        i=0
        total=0
        while i<len(key):
            total = total+ord(key[i])
            i=i+1
        return total % self.SIZE

import unittest

class HashMapUnitTest(unittest.TestCase):
    
    def test_hashMap(self):
        hashTable=HashTable()
        
        hashTable.putValue("input1","value1")
        
        self.assertEqual("value1",hashTable.getValue("input1"))

    def test_hashMapNull(self):
        hashTable=HashTable()
        
        
        self.assertEqual(None,hashTable.getValue("input2"))
        
        
    def test_hashMapUpdate(self):
        hashTable=HashTable()
        hashTable.putValue("input1","value1")

        
        hashTable.putValue("input1","value2")
        
        self.assertEqual("value2",hashTable.getValue("input1"))

if __name__ == '__main__':
    unittest.main()