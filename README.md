# Python Calculator

## Description

A simple calculator program made in Python for a PDC project. It performs basic arithmetic operations and compares their execution times.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Sequential execution
- Parallel execution
- Execution time comparison

## How It Works

The program takes two numbers as input and performs all four calculations.

First, the operations are performed sequentially. Then, Python's `multiprocessing` module is used to perform the operations using separate processes.

The execution time of both methods is displayed at the end.

## Run the Program

```bash
python calculator.py