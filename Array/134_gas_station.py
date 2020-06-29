class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # we define an array rest, rest[i] = gas[i] - cost[i]
        # consider we begin with the station k and check whether every sum(rest[k: (k+j)%n] is positive, 
        # if we find a certain j for which sum(rest[k: (k+j)%n] is negative, then k is not a possible start.
        # however, we don't need to continue to check k+1, we only need to begin with (k+j)%n + 1,
        # this is because, since we reach (k+j)%n, for any p < j, sum(rest[k: (k+p)%n] is positive, 
        # but sum(rest[k: (k+j)%n] is negative, it means sum(rest[(k+p+1)%n : (k+j)%n] must be negatiive
        
        # another problem is, for example, we have station 1,2,3,4,5,6,7 and we find 2 cannot reach 3, we then begin with 3 and find 
        # 4 cannot reach 5,then we try 5 as the start and find 5 can reach 7, then we only need to check if sum(1:7) is non negative,
        # you may wonder that, though sum(1:7) is non negative, what if sum(5:2) is negative? this is impossible,
        # because for every subset which is not available like (3:4), their sum is negative, sum(5:4)=sum(1:7) is positive means that
        # for every p<7, sum(5:(5+p)%n) is positive.
        
        rest = [gas[i]-cost[i] for i in range(len(gas))]
        tank = 0
        start = 0
        run = 0 
        for i in range(len(gas)):
            tank += rest[i]
            run += rest[i]
            if run < 0:
                start = i+1
                run = 0

        # there are two situations where there is no solution
        # first tank < 0, start<len(gas) means start can reach end but cannot reach start - 1
        # second start=len(gas) means none of them can reach end, but the second situaion will also has tank<0
        # because since start = len(gas), it must tries end as its beginning, but fails, which means rest[end] < 0
        # since it tries end, we must have sum(1:end-1) < 0, then sum(1:end) = tank < 0

        if tank < 0:
            return -1 
        else:
            return start
