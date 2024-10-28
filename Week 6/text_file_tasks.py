## Task 1

# def cwd():
#     import os
#     path = os.getcwd()
#     print(f"the current working directory is:\n{path}")
#     for file in os.listdir(path):
#         print("The directory contains the following files:\n",file)
#
# def run():
#     print("processing...")
#     cwd()
#
# run()

## Task 2

# def display_chars(file_path,no_chars):
#     with open(file_path) as f:
#         print(f.read(no_chars),"\n")
#
# def display_lines(file_path):
#     with open(file_path) as f:
#         print(f.readline())
#
# def display_text (file_path):
#     with open(file_path) as f:
#         print(f.read())
#
# def run_task2 ():
#     display_chars("library.txt", 5)
#     display_lines("library.txt")
#     display_text("library.txt")
#
# if __name__ == '__main__':
#     run_task2()
#

## Task 3

# def search(file_name):
#     print("Searching...")
#     with open(file_name) as f:
#         for line in f:
#             print("looked in",line.strip())
#         print("...Done")
#
# def run_task3():
#     search("library.txt")
# run_task3()

## Task 4

def searched_books(file_name):
    print("searching...")
    sections = ""
    books = "Books:\n"
    with open(file_name) as books_file:
        print(books_file.read(7))
        for line in books_file:
            if books_file.read(7) == "Section":
                sections += f"{line}\n"
        print(sections)




searched_books("books.txt")