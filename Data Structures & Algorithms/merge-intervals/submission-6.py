class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort(key=lambda x:x[0])
        start=intervals[0][0]
        endd=intervals[0][1]
        if len(intervals)==1:
            return [intervals[0]]
        else:
            for i in range(1,len(intervals)):
                if intervals[i][0]<=endd:
                    #overlapped
                    endd=max(endd,intervals[i][1])
                else:
                    res.append([start,endd])
                    start=intervals[i][0]
                    endd=intervals[i][1]
            res.append([start,endd])
            unique_list = [list(x) for x in set(tuple(x) for x in res)]
            return unique_list



