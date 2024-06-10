def inequality_solver(a, b, c, x_range):
    answer = []
    for x in x_range:
        if a * x + b < c:
            answer.append(x)
    return answer if answer else "No Solution"

a = float(input("A:"))
b = float(input("B:"))
c = float(input("C:"))
range_required = input("Are you fine with the range being (0, 20)? y/n:")

def use_range():
    x_range = []
    if range_required == "y":
        x_range_str = input("Enter a range in the format (n, n):")
        return eval(x_range_str)
    else:
        x_range = (0, 20)

x_range = use_range()

answer = inequality_solver(a, b, c, x_range)
print(answer)
