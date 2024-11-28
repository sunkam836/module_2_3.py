my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
agent = 0
while agent < len(my_list) :
    print(my_list[agent])
    agent += 1
    if my_list[agent] <= - 1:
        break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/