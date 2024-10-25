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


#Nested tuples and lists

def steps():
    return [("step 1",50),("step 2",38),("step 3",27),("step 4",99),("step 5",4)]

def run_task3():
    good_steps = []
    bad_steps = []
    for element in steps():
        if element[1] > 50:
            good_steps.append(element)
        else:
            bad_steps.append(element)
    print("Good steps:", len(good_steps),", Bad steps:", len(bad_steps))

if __name__ == "__main__":
    run_task3()