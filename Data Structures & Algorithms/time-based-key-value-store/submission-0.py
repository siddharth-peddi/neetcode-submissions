class TimeMap:
    def __init__(self):
        self.count = defaultdict(list)
    
    def set(self, key, value, timestamp):
        self.count[key].append([value, timestamp])
    
    def get(self, key, timestamp):
        values = self.count[key]

        left = 0
        right = len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] > timestamp:
                right = mid - 1
            else:
                result = values[mid][0]
                left = mid + 1
        return result