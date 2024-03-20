from app.io.input import input_text_from_console, read_from_file, read_from_file_with_pandas
from app.io.output import output_text_to_console, write_to_file, write_to_file_with_pandas


def main():
    print("Step 1: Reading and outputting data from console")
    text_from_console = input_text_from_console()
    print("Text from console:", text_from_console)

    print("\nStep 2: Reading and outputting data from file using built-in Python capabilities to console")
    file_path = "data/test1.csv"
    text_from_file = read_from_file(file_path)
    print("Text from file (built-in Python):\n", text_from_file)

    print("\nStep 3: Reading and outputting data from file using pandas to console")
    text_from_file_using_pandas = read_from_file_with_pandas(file_path)
    print("Text from file (pandas):\n", text_from_file_using_pandas)

    print("\nStep 4: Writing data to files using built-in Python capabilities")
    file_output_path = "data/python_output_1.txt"
    write_to_file(file_output_path, text_from_console)
    print("Data written to:", file_output_path)

    file_output_path = "data/python_output_2.txt"
    write_to_file(file_output_path, text_from_file)
    print("Data written to:", file_output_path)

    file_output_path = "data/python_output_3.txt"
    write_to_file(file_output_path, text_from_file_using_pandas)
    print("Data written to:", file_output_path)

    print("\nStep 5: Writing data to files using pandas")
    file_output_path = "data/pandas_output_1.txt"
    write_to_file_with_pandas(file_output_path, text_from_console)
    print("Data written to:", file_output_path)

    file_output_path = "data/pandas_output_2.txt"
    write_to_file_with_pandas(file_output_path, text_from_file)
    print("Data written to:", file_output_path)

    file_output_path = "data/pandas_output_3.txt"
    write_to_file_with_pandas(file_output_path, text_from_file_using_pandas)
    print("Data written to:", file_output_path)


if __name__ == '__main__':
    main()
