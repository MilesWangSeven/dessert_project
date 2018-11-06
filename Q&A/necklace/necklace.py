def solution(items):
    r_list = []
    for i in range(len(items)):
        if items[i]:
            necklace = []
            while items[i] is not None:
                necklace.append(i)
                t = i
                i, items[t] = items[i], None
            r_list.append(necklace)
    print(r_list)
    return max([len(x) for x in r_list])


necklace_list = [5, 4, 0, 3, 1, 6, 2]
print(solution(necklace_list))
