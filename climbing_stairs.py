def find_ways(steps_needed):
    if steps_needed <= 1:
        return 1

    first = 1      
    second = 1    

    for i in range(2, steps_needed + 1):
        ways = first + second
        first = second
        second = ways

    return second

def main():

    total_steps = int(input("Enter the number of stairs: "))
    output = find_ways(total_steps)
    print("Total possible ways to climb:", output)

main()