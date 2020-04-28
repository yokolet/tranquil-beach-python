from collections import defaultdict
import heapq

class ListNode:
    def __init__(self, v):
        self.v = v
        self.prev = self.next = None

class FirstUniqueSlow:
    def __init__(self, nums: 'List[int]'):
        tmp = defaultdict(list)
        for i in range(len(nums)):
            tmp[nums[i]].append(i)
        arr = []
        self.seen = set()
        for k, a in tmp.items():
            self.seen.add(k)
            if len(a) == 1:
                heapq.heappush(arr, (a[0], k))
        self.head = ListNode(None)
        self.v_to_node = {}
        self.tail = self.head
        while arr:
            _, v = heapq.heappop(arr)
            node = ListNode(v)
            self.v_to_node[v] = node
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        print('class creates')

    def showFirstUnique(self) -> int:
        if self.head.next == None:
            return -1
        else:
            return self.head.next.v

    def add(self, value: int) -> None:
        if value not in self.seen:
            self.seen.add(value)
            node = ListNode(value)
            self.v_to_node[value] = node
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        elif value in self.v_to_node:
            node = self.v_to_node[value]
            del self.v_to_node[value]
            node.prev.next = node.next
            if self.tail == node:
                self.tail = node.prev
            else:
                node.next.prev = node.prev
