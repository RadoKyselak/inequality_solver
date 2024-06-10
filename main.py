def inequality_solver(a, b, c, x_range):
    answer = []
    for x in x_range:
        if a * x + b < c:
            answer.append(x)
    return answer if answer else "No Solution"

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
range_required = input("Are you fine with the range being (0, 20)? y/n: ")

def use_range():
    if range_required == "n":
        x_range_str = input("Enter a range in the format (n, n): ")
        start, end = map(int, x_range_str.strip("()").split(","))
        return range(start, end)
    else:
        return range(0, 20)

x_range = use_range()

answer = inequality_solver(a, b, c, x_range)
print(answer)
