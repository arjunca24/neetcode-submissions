class LRUCache:

    def __init__(self, capacity: int):
        self.data = dict()
        self.capacity = capacity 
        self.used = []
        

    def get(self, key: int) -> int:
        val = self.data.get(key,-1)
        if val != -1:

         self.used.remove(key)   
         self.used.append(key)
        return val
        

    def put(self, key: int, value: int) -> None:

        val = self.data.get(key,-1)
        if val == -1:
            if len(self.data) >= self.capacity:
                k = self.used[0]
                self.used.remove(k)
                self.data.pop(k)
        self.data[key] = value    
        if val != -1:           
            self.used.remove(key)
        self.used.append(key)
        
        
