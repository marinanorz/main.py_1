def count_integer(numbers, integer):
    count = 0
    for i in numbers:
        if i == integer:
            count += 1
    if count == 0:
        return 42
    return count


print(count_integer([1, 1, 2, 3, 3, 4], 3))


def list_func(numbers, integer):
    new_list = numbers.copy()
    for index, value in enumerate(numbers):
        if value == integer:
            numbers[index] = 6
            print(numbers.reverse())
            print(new_list)
            return numbers
    else:
        return []


print(list_func([2, 5, 7, 8], 8))


def compare_lists(list1, list2):
    return [i for i in list1 if i in list2]


print(compare_lists([1, 2, 3, 4, 5], [5, 4, 7, 8, 9]))


def remove_duplicates(lst):
    res = []
    [res.append(x) for x in lst if x not in res]
    return print(res)


remove_duplicates([1, 2, 3, 3, 3, 4, 5, 4, 5])


def dict_func(dictionary):
    print("You have a", dictionary["Type"], "from", dictionary["Brand"], "that costs", dictionary["Price"])
    dictionary["OS"] = "Linux"
    print(dictionary)
    #habe das leider überhaupt nicht verstanden


dict_func({"Type": "Notebook", "Brand": "Dell", "Price": 2000})
