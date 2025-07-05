class MyHashMap:
    def __init__(self):
        self.length = 10**6 + 1
        self.map = [-1] * self.length

    def get_index(self, key: int) -> int:
        index = hash(key) % self.length
        return index

    def put(self, key: int, value: int) -> None:
        index = self.get_index(key)
        self.map[index] = value

    def get(self, key: int) -> int:
        index = self.get_index(key)
        value = self.map[index]
        return value

    def remove(self, key: int) -> None:
        index = self.get_index(key)
        self.map[index] = -1
