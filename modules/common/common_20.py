# modules/common/common_20.py

def get_list_element(lst, index):
    if not isinstance(lst, list):
        raise TypeError("lst must be a list")
    if not isinstance(index, int):
        raise TypeError("index must be an integer")
    if index < 0 or index >= len(lst):
        raise IndexError("index out of range")
    return lst[index]
