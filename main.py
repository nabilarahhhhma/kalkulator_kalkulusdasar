from sympy import symbols, diff, integrate, sympify

x = symbols('x')

def kalkulasi_turunan(fungsi_str):
    fungsi = sympify(fungsi_str)
    turunan = diff(fungsi, x)
    return turunan

def kalkulasi_integral(fungsi_str):
    fungsi = sympify(fungsi_str)
    integral = integrate(fungsi, x)
    return integral

if __name__ == "__main__":
    fungsi_input = input("Masukkan fungsi (misal: x**2 + 3*x + 2): ")
    print("Turunan:", kalkulasi_turunan(fungsi_input))
    print("Integral:", kalkulasi_integral(fungsi_input))
