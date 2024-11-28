def binary_search_iterative(sorted_list: list, target: int) -> int:
    # Empty List
    if len(sorted_list)==0:
        return -1
    # Data Validation
    if not isinstance(target, int):
        return -1
    
    left = 0
    right = len(sorted_list)-1
    
    while left <=right:
        mid = left+(right-left)//2 # restituisce solo la parte intera
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] > target:
            right = mid-1
        elif sorted_list[mid] < target:
            left = mid+1
    return -1


def binary_search_recursive(sorted_list: list, target: int, left: int, right: int) -> int:
   # Empty List
    if len(sorted_list)==0:
        return -1
    # Data Validation
    if not isinstance(target, int):
        return -1

    while left <= right:
        mid = left + (right-left)//2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] > target:
            right = mid -1
            return binary_search_recursive(sorted_list, target, left, right)
        elif sorted_list[mid] < target:
            left = mid +1
            return binary_search_recursive(sorted_list, target, left, right)
    return -1
