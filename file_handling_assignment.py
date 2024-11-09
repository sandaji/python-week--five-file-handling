# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, World!\n")
            file.write("12345\n")
            file.write("Python is fun!\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File Appending
def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("My name is Vincent 1\n")
            file.write("i work wit Tronic Kenya Ltd 2\n")
            file.write("I study at powerLearn academy 3\n")
        print("File appended successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to execute the tasks
def main():
    create_file()
    read_file()
    append_file()
    read_file()

if __name__ == "__main__":
    main()
