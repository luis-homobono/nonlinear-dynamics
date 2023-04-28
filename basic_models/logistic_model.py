# Logistic equation model
# x_n+1 = R * x_n * (1 - x_n)

def logistic_model(n: int, r: float, x: float) -> list:
    """Model logistic with maps time laps

    Args:
        n (int): Generations
        r (float): R value
        x (float): Rate

    Returns:
        list: List with values in iterations
    """
    result = []
    for i in range(n):
        try:
            x_n1 = r * result[-1] * (1 - result[-1])
            result.append(x_n1)
        except:
            x_n1 = r * x * (1 - x)
            result.append(x_n1)

    return result

x = 0.2
r = 2
n = 50

print(logistic_model(n=n, r=r, x=x))