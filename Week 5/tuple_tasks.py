#Simple Tuple

def likelihood():
    likelihoods = (50, 38, 27, 99 , 4)
    return min(likelihoods)
def run_task1():
    print("Minimum likelihood of failing:", str(likelihood()) + "%")


if __name__ == "__main__":
    run_task1()