from app.io.input import input_text_from_console, read_from_file, read_from_file_with_pandas
from app.io.output import output_text_to_console, write_to_file, write_to_file_with_pandas


def main():
    text_from_console = input_text_from_console()

    file_path = "data/test1.csv"
    text_from_file = read_from_file(file_path)
    text_from_file_using_pandas = read_from_file_with_pandas(file_path)

    print("--------------------------------------------------------------------------------")
    output_text_to_console(text_from_console)
    print("--------------------------------------------------------------------------------")
    output_text_to_console(text_from_file)
    print("--------------------------------------------------------------------------------")
    output_text_to_console(text_from_file_using_pandas)

    file_output_path = "data/python_output_1.txt"
    write_to_file(file_output_path, text_from_console)
    file_output_path = "data/python_output_2.txt"
    write_to_file(file_output_path, text_from_file)
    file_output_path = "data/python_output_3.txt"
    write_to_file(file_output_path, text_from_file_using_pandas)

    file_output_path = "data/pandas_output_1.txt"
    write_to_file_with_pandas(file_output_path, text_from_console)
    file_output_path = "data/pandas_output_2.txt"
    write_to_file_with_pandas(file_output_path, text_from_file)
    file_output_path = "data/pandas_output_3.txt"
    write_to_file_with_pandas(file_output_path, text_from_file_using_pandas)


if __name__ == '__main__':
    main()