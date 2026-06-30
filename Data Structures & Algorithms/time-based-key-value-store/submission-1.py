class TimeMap:

    def __init__(self):
        self.values = {}
         
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.values:
            val = self.values[key]
            n = len(val)
            for i in range(n):
                if (val[i][0] > timestamp):
                    val.insert(i,(timestamp,value))
                    break
            if val[n-1][0]<timestamp:
                val.append((timestamp,value))
        else:
            self.values[key] = [(timestamp,value)]
            

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""
        values = self.values[key]
        
        n = len(values)
        if n==1:
            if values[0][0] <= timestamp:
                return values[0][1]
        for i in range(1,n):
            
            if values[i-1][0] == timestamp or (values[i-1][0]<timestamp and values[i][0]>timestamp ) :  
                return values[i-1][1]
        if values[n-1][0]<=timestamp:
            return values[n-1][1]
        return ""
          


        
        
