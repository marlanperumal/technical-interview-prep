import heapq


def kth_largest_simple(l: list[int], k: int) -> int:
    s = sorted(l)
    print(s)
    return s[-k]


def kth_largest_heap(l: list[int], k: int) -> int:
    heap: list[int] = []

    for i in l:
        if len(heap) < k:
            heapq.heappush(heap, i)
        else:
            heapq.heappushpop(heap, i)

    return heap[0]


def partition(arr: list[int], left: int, right: int) -> int:
    p = arr[left]
    i = left

    for j in range(left, right):
        if arr[j] >= p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i


def kth_largest_quickselect(
    l: list[int], k: int, left: int | None = None, right: int | None = None
) -> int:
    if left is None:
        left = 0
    if right is None:
        right = len(l) - 1

    i = partition(l, left, right)

    if i == k - 1:
        return l[i]

    if i > k - 1:
        return kth_largest_quickselect(l, k, left, i - 1)

    else:
        return kth_largest_quickselect(l, k - i + left - 1, i + 1, right)


if __name__ == "__main__":
    l: list[int] = [3, 4, 2, 4, 6, 3, 6, 3, 2, 5, 8, 2, 5]
    k = 4
    print(kth_largest_simple(l, k))
    print(kth_largest_heap(l, k))
    print(kth_largest_quickselect(l, k))
    print(l)
