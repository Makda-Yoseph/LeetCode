class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        occur = Counter(words)
        lis = []
        w = defaultdict(list)
        for key,v in occur.items():
            w[v].append(key)
        for key,v in w.items():
            w[key].sort()
        for key,v in w.items():
            lis.append([key,v])
        lis.sort(reverse = True)
        
        ans = []
        for i in range(len(lis)):
            n = len(lis[i][1])
            l = 0
            while k and l<n:
                ans.append(lis[i][1][l])
                l+=1
                k-=1
            if k==0:
                break
        return ans
        