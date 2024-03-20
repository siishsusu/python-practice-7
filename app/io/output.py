import pandas as pd


def output_text_to_console(text):
    """
    Function to output text to the console.

    This function prompts the user to input text and then prints it to the console.

    Args:
        text (str): The text to be printed to the console.

    Returns:
        None
    """
    print(text)

def write_to_file(file_path, text):
    """
    Function to write text to a file using built-in Python capabilities.

    Args:
        file_path (str): The path to the file to write the text to.
        text (str): The text to be written to the file.

    Returns:
        None
    """
    with open(file_path, 'w') as file:
        return file.write(text)


def write_to_file_with_pandas(file_path, text):
    """
    Function to write text to a file using the pandas library.

    Args:
        file_path (str): The path to the file to write the text to.
        text (str): The text to be written to the file.

    Returns:
        None
    """
    df = pd.DataFrame([text])
    df.to_csv(file_path, index=False, header=False)
