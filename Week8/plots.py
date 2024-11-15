import matplotlib.pyplot as plt

# #Basic Data Visualisation
# def display_line(xvalues,yvalues):
#     plt.xlabel("X Value")
#     plt.ylabel("Y Value")
#     plt.plot(xvalues, yvalues)
#     plt.show()
#
# def run_task1():
#     display_line([1,2,3,4,5],[1,4,9,16,25])
#
# run_task1()

# #More complex data visulisation
#
# def small():
#     plt.plot([3,3,4,4,3],[3,4,4,3,3],"ro--")
#
#
# def medium():
#     plt.plot([2, 2, 5, 5, 2], [5, 2, 2, 5, 5],"gs--")
#
#
# def large():
#     plt.plot([1, 1, 6, 6, 1], [1, 6, 6, 1, 1],"bp-")
#
# small()
# medium()
# large()
# plt.show()


#User Inputed Data Visualisation

def coordinate():
    return input("Enter an X"),input("Enter an Y")

def path():
    print("Retrieving Path")
    x_values = []
    y_values = []
    for i in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return x_values,y_values

def run_task3():
    values = path()
    plt.plot(values[0],values[1],"ro--")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.show()

run_task3()