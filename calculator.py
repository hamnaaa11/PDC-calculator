import time
from multiprocessing import Process, Queue


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def parallel_add(a, b, queue):
    queue.put(("Addition", add(a, b)))


def parallel_subtract(a, b, queue):
    queue.put(("Subtraction", subtract(a, b)))


def parallel_multiply(a, b, queue):
    queue.put(("Multiplication", multiply(a, b)))


def parallel_divide(a, b, queue):
    queue.put(("Division", divide(a, b)))


if __name__ == "__main__":

    print("===================================")
    print("        MY PDC CALCULATOR")
    print("===================================")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Sequential execution
    start_time = time.perf_counter()

    addition = add(num1, num2)
    subtraction = subtract(num1, num2)
    multiplication = multiply(num1, num2)
    division = divide(num1, num2)

    end_time = time.perf_counter()

    sequential_time = end_time - start_time

    print("\n========== SEQUENTIAL ==========")
    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Division:", division)
    print("Execution Time:", sequential_time, "seconds")

    # Parallel execution
    queue = Queue()

    start_time = time.perf_counter()

    p1 = Process(target=parallel_add, args=(num1, num2, queue))
    p2 = Process(target=parallel_subtract, args=(num1, num2, queue))
    p3 = Process(target=parallel_multiply, args=(num1, num2, queue))
    p4 = Process(target=parallel_divide, args=(num1, num2, queue))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    end_time = time.perf_counter()

    parallel_time = end_time - start_time

    results = {}

    for i in range(4):
        operation, result = queue.get()
        results[operation] = result

    print("\n========== PARALLEL ==========")
    print("Addition:", results["Addition"])
    print("Subtraction:", results["Subtraction"])
    print("Multiplication:", results["Multiplication"])
    print("Division:", results["Division"])
    print("Execution Time:", parallel_time, "seconds")

    print("\n========== COMPARISON ==========")
    print("Sequential Time:", sequential_time, "seconds")
    print("Parallel Time:", parallel_time, "seconds")