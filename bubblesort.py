"""
Информация получена:
https://younglinux.info/algorithm/bubble
"""


def bubblesort(alist: list[any([int, float])]):
    n = len(alist)
    for i in range(n-1):
        for j in range(n-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]