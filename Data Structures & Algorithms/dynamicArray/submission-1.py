class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity

        #if capacity is say 5 initial array is [0 0 0 0 0]

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        #append won't work here because append pushes the element to the end at the back so for example
        #instead of [1 0 0 0 0] for a new pushback it will do [0 0 0 0 0 1] it will increase the capacity and we don't want that 
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size]= n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.arr.extend(self.arr)
        self.capacity = 2 * self.capacity

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
