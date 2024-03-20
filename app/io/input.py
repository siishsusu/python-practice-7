import pandas as pd


def input_text_from_console():
    """
    Function for inputting text from the console.

    Returns:
        str: The text inputted from the console.
    """
    return input("Enter text: ")


def read_from_file(file_path):
    """
    Function for reading text from a file using built-in Python capabilities.

    Args:
        file_path (str): The path to the file to read the text from.

    Returns:
        str: The text read from the file.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as error:
        print(f"An error occurred while reading the file '{file_path}': {error}")


def read_from_file_with_pandas(file_path):
    """
    Function for reading text from a file using the pandas library.

    Args:
        file_path (str): The path to the file to read the text from.

    Returns:
        str: The text read from the file.
    """
    try:
        file_data = pd.read_csv(file_path)
        text = file_data.to_string(index=False, header=True)
        return text
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as error:
        print(f"An error occurred while reading the file '{file_path}': {error}")