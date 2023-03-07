def merge(list1, list2):
    # i = j = 0
    # merged_list = []
    #
    # while i < len(list1) and j < len(list2):
    #     if list1[i] < list2[j]:
    #         merged_list.append(list1[i])
    #         i += 1
    #     else:
    #         merged_list.append(list2[j])
    #         j += 1
    #
    # if i < len(list1):
    #     merged_list += list1[i:]
    # elif j < len(list2):
    #     merged_list += list2[j:]

    return sorted(list1 + list2)


def merge_sort(my_list, count):
    if len(my_list) < 2: return my_list

    mid = len(my_list) // 2

    list1 = merge_sort(my_list[:mid], count)
    list2 = merge_sort(my_list[mid:], count)

    if count < len(my_list):
        return list1 + list2

    return merge(list1, list2)


def print_list(my_list):
    for m in my_list:
        print(m, end=" ")


N = int(input())
chicken_rates = list(map(int, input().split()))
print_list(merge_sort(chicken_rates, N//int(input()))) # K명당 정렬해야 하는 배열의 크기
