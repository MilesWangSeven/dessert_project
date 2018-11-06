def solution(items):
    rtn = {}
    for i in range(len(items)):
        if items[i]:
            necklace = []
            while items[i] is not None:
                necklace.append(i)
                t = i
                i, items[t] = items[i], None
            length = len(necklace)
            if rtn.get(length):
                rtn[length].append(necklace)
            else:
                rtn[length] = [necklace]
    # print(rtn)
    return max(rtn.keys())


necklace_list = [5, 4, 0, 3, 1, 6, 2]
print(solution(necklace_list))

necklace_list = [1,0, 3, 2]
print(solution(necklace_list))