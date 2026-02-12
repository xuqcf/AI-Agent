from functions.get_files_contents import get_file_content


def main():
    # Current directory as working directory
    print("Result for current directory:")
    print(get_file_content(".", "calculator/main.py"))
    print()

    print("Result for 'pkg' directory:")
    print(get_file_content(".", "calculator/pkg/calculator.py"))
    print()

    print("Result for '/bin' directory:")
    print(get_file_content(".", "/bin/cat"))
    print()

    print("Result for '../' directory:")
    print(get_file_content(".", "calculator/pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()