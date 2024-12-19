import math
import matplotlib.pyplot as plt

def bisection_method(func, a, b, epsilon):
    if func(a) * func(b) >= 0:
        print("Error: f(a) and f(b) must have opposite signs.")
        return None, []
    
    iteration = 1
    x_values = []

    while (b - a) / 2 > epsilon:
        x = (a + b) / 2
        x_values.append(x)
        print(f"{iteration}-iteration: x = {x:.6f}, a = {a:.6f}, b = {b:.6f}, f(x) = {func(x):.6f}")

        if func(x) * func(a) < 0:
            b = x
        else:
            a = x

        iteration += 1

    print(f"\nRoot: x = {x:.6f}, found in {iteration} iterations.")
    return x, x_values

def false_position_method(func, a, b, epsilon):
    if func(a) * func(b) >= 0:
        print("Error: f(a) and f(b) must have opposite signs.")
        return None, []
    
    iteration = 1
    x_values = []

    while True:
        x = (a * func(b) - b * func(a)) / (func(b) - func(a))
        x_values.append(x)
        print(f"{iteration}-iteration: x = {x:.6f}, a = {a:.6f}, b = {b:.6f}, f(x) = {func(x):.6f}")

        if abs(func(x)) < epsilon or abs(b - a) < epsilon:
            break

        if func(x) * func(a) < 0:
            b = x
        else:
            a = x

        iteration += 1

    print(f"\nRoot: x = {x:.6f}, found in {iteration} iterations.")
    return x, x_values

def plot_results(x_values, method_name):
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(x_values) + 1), x_values, marker='o', label=method_name)
    plt.title(f'Convergence of {method_name}')
    plt.xlabel('Iteration')
    plt.ylabel('x Value')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    print("Root-Finding Methods")
    print("1. Bisection Method")
    print("2. Method of False Position")

    choice = input("Select a method (1 or 2): ")
    if choice not in ['1', '2']:
        print("Invalid choice!")
        return

    equation = input("Enter the function (use 'x' as the variable, e.g., 'x**3 - x - 2'): ")
    func = lambda x: eval(equation)
    
    a = float(input("Enter the lower bound (a): "))
    b = float(input("Enter the upper bound (b): "))
    epsilon = float(input("Enter the tolerance (epsilon): "))

    if choice == '1':
        print("\nBisection Method:")
        root, x_values = bisection_method(func, a, b, epsilon)
        method_name = "Bisection Method"
    else:
        print("\nMethod of False Position:")
        root, x_values = false_position_method(func, a, b, epsilon)
        method_name = "Method of False Position"

    if root is not None:
        plot_results(x_values, method_name)

if __name__ == "__main__":
    main()
