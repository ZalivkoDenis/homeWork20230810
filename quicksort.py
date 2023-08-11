def quicksort(alist: list[any([int, float])], start: int, end: int):
    """Sorts the list from indexes start to end - 1 inclusive."""
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)


def partition(alist: list[any([int, float])], start: int, end: int) -> int:
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and alist[i] <= pivot:
            i += 1
        while i <= j and alist[j] >= pivot:
            j -= 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j