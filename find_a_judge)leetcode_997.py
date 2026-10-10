class Solution:
      def findJudge(self, n: int, trust: list[list[int]]) -> int:

            if len(trust) < 1:
                  if n ==1 : return 1
                  else: return -1

            d = defaultdict(list)
            e = defaultdict(list)
            judge = None

            for u,v in trust:
                  d[v].append(u)
                  e[u].append(v)
            
            # if len(d) == 1: return list(d.keys())[0]

            for key, value in d.items(): 
                  if len(value) == n-1:
                        if len(e[key]) >= 1: 
                              continue
                        judge = key

            return judge if judge is not None else -1

      def findJudge_onemore(self, n: int, trust: list[list[int]]) -> int:
            d= defaultdict(int)

            for u,v in trust: 
                  d[u] -= 1
                  d[v] += 1


            for key, value in d.items():
                  if value == n-1: 
                        return key
            
            return -1 if n > 1 else 1