class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidMap = defaultdict(list)
        # euclidMap = {}
        ePoints = []
        result = []
        
        for point in points:
            euclid = math.sqrt((point[0] ** 2) + (point[1] ** 2))
            euclidMap[euclid].append(point)
            # euclidMap[euclid] = point
            ePoints.append(euclid)
        
        heapq.heapify(ePoints)
        while k > 0:
            dist = heapq.heappop(ePoints)
            result.append(euclidMap[dist].pop())
            # result.append(euclidMap[heapq.heappop(ePoints)])
            k -= 1

        return result