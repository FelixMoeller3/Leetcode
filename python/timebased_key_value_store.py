class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value,timestamp))
        else:
            self.map[key] = [(value,timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        l = 0
        r = len(self.map[key]) -1
        while l < r:
            middle = (l+r)//2
            if l == middle:
                l = l+1 if self.map[key][middle+1][1] <= timestamp else l
                break
            if timestamp < self.map[key][middle][1]:
                r = middle-1
            else:
                l = middle
        if timestamp < self.map[key][l][1]:
            return ""
        return self.map[key][l][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# ["TimeMap","set","set","get","get","get","get","get"]
# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

if __name__ == "__main__":
    obj = TimeMap()
    obj.set("love","high",10)
    obj.set("love","low",20)
    obj.get("love",5)
    obj.get("love",10)
    obj.get("love",15)
    obj.get("love",20)
    obj.get("love",25)
