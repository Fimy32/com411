import os

# def cwd():
#     path = os.getcwd()
#     print(f"Current Working Directory: {path}")
#     print("The directory contains the following files:")
#     for file in os.listdir(path):
#         print(file)
#
#
# def run():
#     cwd
#
# run()



def display_chars(path,count):
    with open(path, "r") as file:
        print(file.read(int(count)))

def display_line(path):
    with open(path, "r") as file:
        print(file.readline())

def display_text(path):
    with open(path, "r") as file:
        print(file.read())

def run_task2():
    display_chars("library.txt", "10")
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run_task2()