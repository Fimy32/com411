#Simple Tuple

def likelihood():
    likelihoods = (50, 38, 27, 99 , 4)
    return likelihoods
def run_task1():
    print("Minimum likelihood of failing:", str(min((likelihood()))) + "%")


if __name__ == "__main__":
    run_task1()

#Returning Tuples in functions

def likelihood_min_max():
    return min(likelihood()), max(likelihood())

def run_task2():
    print("Minimum likelihood of falling:", str(likelihood_min_max()[0]) + "%\n" + "Maximum likelihood of falling:", str(likelihood_min_max()[1]) + "%")


if __name__ == "__main__":
    run_task2()