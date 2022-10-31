from operator import le
import sys
import heapq

N = int(sys.stdin.readline())

"""
h_list = []
heapq.heappush(h_list, 5)
heapq.heappush(h_list, 10)
heapq.heappush(h_list, 1)
heapq.heappush(h_list, 20)
heapq.heappush(h_list, 15)
heapq.heappop(h_list)
print(h_list)
"""
left_list = []
right_list = []

for _ in range(N):
    n = int(sys.stdin.readline())
    if len(left_list) == len(right_list):
        heapq.heappush(left_list, -n)
    else:
        heapq.heappush(right_list, n)

    if len(right_list) == 0:
        print("answer: ", end="")
        print(-left_list[0])
    else:
        left = -left_list[0]
        right = right_list[0]
        if left <= right:
            print("answer: ", end="")
            print(left)
        else:
            print("answer: ", end="")
            print(right)
            heapq.heappop(left_list)
            heapq.heappop(right_list)
            heapq.heappush(left_list, -right)
            heapq.heappush(right_list, left)
