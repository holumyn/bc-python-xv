def odd_numbers(low, high):
    if(low < high):
        even_num = [x for x in range(low,high) if x%2 == 1]
        print(even_num)
    else:
        print("Low is bigger than high")

odd_numbers(1,100)
