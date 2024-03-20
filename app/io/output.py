import pandas as pd


def output_text_to_console(text):
    """
    Function for outputting text to the console.

    Args:
        text (str): The text to be outputted to the console.
    """
    print(text)


def write_to_file(file_path, text):
    """
    Function for writing text to a file using built-in Python capabilities.

    Args:
        file_path (str): The path to the file where the text will be written.
        text (str): The text to be written to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"Text has been written to the file: {file_path}")
    except Exception as error:
        print(f"An error occurred while writing to the file '{file_path}': {error}")


def write_to_file_with_pandas(file_path, text):
    """
    Function for writing text to a file using the pandas library.

    Args:
        file_path (str): The path to the file where the text will be written.
        text (str): The text to be written to the file.
    """
    try:
        file_data = pd.DataFrame([text])
        file_data.to_csv(file_path, index=False, header=False)
        print(f"Text has been written to the file using pandas: {file_path}")
    except Exception as error:
        print(f"An error occurred while writing to the file '{file_path}': {error}")
