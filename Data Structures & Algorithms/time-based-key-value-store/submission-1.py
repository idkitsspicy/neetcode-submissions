class TimeMap:

    def __init__(self):
        self.d={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #self.d[(key,timestamp)]=value
        if key not in self.d:
            self.d[key]=[]
        self.d[key].append((timestamp,value))

        return None
        

    def get(self, key: str, timestamp: int) -> str:
        #brute force
        '''best=0
        best_val=""
        for (k,t) in self.d:
            if k==key and t==timestamp:
                return self.d[(k,t)]
            elif k==key and t<timestamp:
                if best<t:
                    best=t
                    best_val=self.d[(k,t)]

            else:
                return ""
        return best_val'''
        #optimized looking for best thru binary search
        #we store key:(t,val),... in set
        if key not in self.d:
            return ""
        rec=self.d[key]
        l=0
        r=len(rec)-1
        best=-1
        while l<=r:
            mid=(l+r)//2
            if rec[mid][0]==timestamp:
                return rec[mid][1]
            elif rec[mid][0]>timestamp:
                r=mid-1
            else:
                l=mid+1
                best=mid
        if best==-1:
            return ""

        return rec[best][1]


        

        

        
