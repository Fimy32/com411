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



# def display_chars(path,count):
#     with open(path, "r") as file:
#         print(file.read(int(count)))
#
# def display_line(path):
#     with open(path, "r") as file:
#         print(file.readline())
#
# def display_text(path):
#     with open(path, "r") as file:
#         print(file.read())
#
# def run_task2():
#     display_chars("library.txt", "10")
#     display_line("library.txt")
#     display_text("library.txt")
#
# if __name__ == "__main__":
#     run_task2()

# def search(path):
#     print("Searching...")
#     with open(path) as file:
#         for line in file:
#             print("Looked in", line)
#     print("\n...Done!")
#
# def run_task3():
#     search("library.txt")
#
# run_task3()

def search_books(path):
    print("Searching...")
    sections = ""
    books = "Books:\n"
    with open(path) as file:
        for line in file:
            if line.startswith("Section: "):
                sections = sections + line + "\n"
            else:
                books = books + line + "\n"
    print("Done!")
    print(sections, "\n\n" + books)
    return sections + books

def save(path,data):
    print("Saving...")
    with open(path,"w") as file:
        file.write(data)
    print("Done!")

def run_task4():
    save("section-books.txt", str(search_books("books.txt")))

run_task4()


