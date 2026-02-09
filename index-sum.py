def findRestaurant(list1: list[str], list2: list[str]) -> list[str]:
    output = {}

    for i, string in enumerate(list1):
        if string in list2:
            if string not in output.keys():
                output[string] = i + list2.index(string)
            elif i + list2.index(string) < output[string]:
                output[string] = i + list2.index(string)

    value = min([out for out in output.values()])

    return [string for string, index_sum in output.items() if index_sum == value]

# print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
# print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]))
print(findRestaurant(["happy","sad","good"], ["sad","happy","good"]))