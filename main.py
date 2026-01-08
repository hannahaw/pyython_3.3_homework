my_list = [1, 2, 3, 4, 5]

split_index = (len(my_list) + 1) // 2

part1 = my_list[:split_index]
part2 = my_list[split_index:]

print([part1, part2])
