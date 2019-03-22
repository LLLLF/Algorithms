def max_heapify(heap, size, root):

    left = 2*root + 1
    right = left + 1
    larger = root
    if left < size and heap[left] > heap[larger]:
        larger = left
    if right < size and heap[right] > heap[larger]:
        larger = right
    if larger != root:
        heap[larger], heap[root] = heap[root], heap[larger]

        max_heapify(heap, larger, size)


def build_max_heap(heap):
    size = len(heap)
    for i in range((size - 2)//2, -1, -1):
        max_heapify(heap, size, i)


def heapsort(heap):
    build_max_heap(heap)
    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0)
    return heap





a = [30, 50, 57, 77, 62, 78, 94, 80, 84]

heapsort(a)
print(a)








