"""
Link: https://app.codesignal.com/interview-practice/task/gX7NXPBrYThXZuanm/description
"""


def removeKFromList(l, k):
    c = l
    while c:
        if c.next and c.next.value == k:
            c.next = c.next.next
        else:
            c = c.next
    return l.next if l and l.value == k else l


lista = [1, 2, 3, 4, 5, 6, 7, 7]
numero = 7

print(removeKFromList(lista, numero))

