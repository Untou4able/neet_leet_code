import heapq


from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyCount = {}
        for i in nums:
            frequencyCount[i] = frequencyCount.get(i, 0) + 1
            
        print(frequencyCount)
        heap = list((f, n) for n, f in frequencyCount.items())
        heapq.heapify(heap)
        return [i[1] for i in heapq.nlargest(k, heap)]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        frequencyCount = {}
        for i in nums:
            frequencyCount[i] = frequencyCount.get(i, 0) + 1
         
        bucket = [[] for _ in range(len(nums)+1)]
        for n in frequencyCount:
            bucket[frequencyCount[n]].append(n)
        print(bucket)

        res = []
        for i in range(len(nums)-1, -1, -1):
            if not bucket[i] ==  []:
                for n in bucket[i]:
                    res.append(n)
                    if len(res) == k:
                        return res


s = Solution()
print(s.topKFrequent2([3,0,1,0], 1))
