from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskNums = {}
        taskToPrio = {}
        for elem in tasks:
            if elem not in taskNums:
                taskNums[elem] = 0
                taskToPrio[elem] = 0
            taskNums[elem] += 1

        
        prios = [0] * len(taskToPrio)
        prios.remove()
        heapq.heapify(prios)
        time = 0
        while taskNums:
            time += 1
            if prios[0] > 0:
                for i in range(len(prios)):
                    prios[i] -= 1
                for elem in taskToPrio:
                    taskToPrio[elem] -= 1
                continue
            heapq.heappop(prios)
            task = "Z"
            freq = -1
            for elem in taskNums:
                if taskNums[elem] > freq and taskToPrio[elem] == 0:
                    task = elem
                    freq = taskNums[elem]
            for i in range(len(prios)):
                    prios[i] = prios[i] - 1 if prios[i] > 0 else prios[i]
            for elem in taskToPrio:
                taskToPrio[elem] = taskToPrio[elem]-1 if taskToPrio[elem]>0 else taskToPrio[elem]
            if freq == 1:
                taskNums.pop(task)
                taskToPrio.pop(task)
            else:
                taskToPrio[task] = n
                taskNums[task] -= 1
                heapq.heappush(prios,n)
        return time

if __name__ == "__main__":
    tasks = ["A","A","A","B","B","B"]
    n = 2
    sol = Solution()
    print(sol.leastInterval(tasks,n))