import heapq

def kth_larget(arr, k):
  arr = [-elem for elem inarr]
  heapq.heapify(arr)
  for i in range (k-1):
    heapq.heappop(arr)
  return -heapq.heappop(arr)
