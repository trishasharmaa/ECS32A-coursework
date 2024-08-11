import random



def estimating_pi(seed, iterations_to_run):
    """
    This function estimates pi using random number generator

    Parameters:
    seed (int): random number generator
    iterations_to_run (int): number of iterations to run

    Returns:
    pi (float): estimated vale of pi
    """
    random.seed(int(seed))
    inside_circle = 0

    for _ in range(iterations_to_run):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1

    pi_estimation = 4 * inside_circle / iterations_to_run
    return pi_estimation



if __name__ == "__main__":
    seed = input("Enter the seed for the random number generator: ")
    iterations_to_run = int(input("Enter the number of iterations to run: "))

    pi_value = estimating_pi(seed, iterations_to_run)
    print(f"The value of pi is {pi_value:.2f}.")
