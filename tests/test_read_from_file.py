from app.io.input import read_from_file

def test_read_existing_file():
    file_path = 'file_with_data.txt'
    expected_text = 'I\'m stayin\' at my parents\' house\nAnd the road not taken looks real good now'
    assert read_from_file(file_path) == expected_text

def test_read_nonexistent_file():
    file_path = 'data/nonexistent_file.txt'
    assert read_from_file(file_path) is None

def test_read_empty_file():
    file_path = 'empty_file.txt'
    assert read_from_file(file_path) == ''

def test_read_file_error():
    file_path = 'file_with_data.txt'
    expected_text = 'Im stayin\' at my parents\' house\nAnd the road not taken looks real good now'
    assert read_from_file(file_path) == expected_text
