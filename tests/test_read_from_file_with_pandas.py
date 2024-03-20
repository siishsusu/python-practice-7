from app.io.input import read_from_file_with_pandas

def test_read_existing_file():
    file_path = 'file_with_data_csv.csv'
    expected_text = (
        "        COUNTRY      POP      AREA       GDP       CONT     IND_DAY\n"
        "CHN       China  1398.72   9596.96  12234.78       Asia         NaN\n"
        "IND       India  1351.16   3287.26   2575.67       Asia  1947-08-15\n"
        "USA          US   329.74   9833.52  19485.39  N.America  1776-07-04\n"
        "IDN   Indonesia   268.07   1910.93   1015.54       Asia  1945-08-17\n"
        "BRA      Brazil   210.32   8515.77   2055.51  S.America  1822-09-07\n"
        "PAK    Pakistan   205.71    881.91    302.14       Asia  1947-08-14\n"
        "NGA     Nigeria   200.96    923.77    375.77     Africa  1960-10-01\n"
        "BGD  Bangladesh   167.09    147.57    245.63       Asia  1971-03-26\n"
        "MEX      Mexico   126.58   1964.38   1158.23  N.America  1810-09-16\n"
        "JPN       Japan   126.22    377.97   4872.42       Asia         NaN\n"
        "DEU     Germany    83.02    357.11   3693.20     Europe         NaN\n"
        "FRA      France    67.02    640.68   2582.49     Europe  1789-07-14\n"
        "GBR          UK    66.44    242.50   2631.23     Europe         NaN\n"
        "ITA       Italy    60.36    301.34   1943.84     Europe         NaN\n"
        "ARG   Argentina    44.94   2780.40    637.49  S.America  1816-07-09\n"
        "DZA     Algeria    43.38   2381.74    167.56     Africa  1962-07-05\n"
        "CAN      Canada    37.59   9984.67   1647.12  N.America  1867-07-01\n"
        "AUS   Australia    25.47   7692.02   1408.68    Oceania         NaN\n"
        "KAZ  Kazakhstan    18.53   2724.90    159.41       Asia  1991-12-16"
    )
    assert read_from_file_with_pandas(file_path) == expected_text

def test_read_nonexistent_file():
    file_path = 'data/nonexistent_file.txt'
    assert read_from_file_with_pandas(file_path) is None

def test_read_empty_file():
    file_path = 'empty_file.txt'
    assert read_from_file_with_pandas(file_path) is None

def test_read_file_error():
    file_path = 'file_with_data_csv.csv'
    expected_text = (
        "        COUNTRY      AREA       GDP       CONT     IND_DAY\n"
        "CHN       China  1398.72   9596.96  12234.78       Asia         NaN\n"
        "IND       India  1351.16   3287.26   2575.67       Asia  1947-08-15\n"
        "USA          US   329.74   9833.52  19485.39  N.America  1776-07-04\n"
        "IDN   Indonesia   268.07   1910.93   1015.54       Asia  1945-08-17\n"
        "BRA      Brazil   210.32   8515.77   2055.51  S.America  1822-09-07\n"
        "PAK    Pakistan   205.71    881.91    302.14       Asia  1947-08-14\n"
        "NGA     Nigeria   200.96    923.77    375.77     Africa  1960-10-01\n"
        "BGD  Bangladesh   167.09    147.57    245.63       Asia  1971-03-26\n"
        "MEX      Mexico   126.58   1964.38   1158.23  N.America  1810-09-16\n"
        "JPN       Japan   126.22    377.97   4872.42       Asia         NaN\n"
        "DEU     Germany    83.02    357.11   3693.20     Europe         NaN\n"
        "FRA      France    67.02    640.68   2582.49     Europe  1789-07-14\n"
        "GBR          UK    66.44    242.50   2631.23     Europe         NaN\n"
        "ITA       Italy    60.36    301.34   1943.84     Europe         NaN\n"
        "ARG   Argentina    44.94   2780.40    637.49  S.America  1816-07-09\n"
        "DZA     Algeria    43.38   2381.74    167.56     Africa  1962-07-05\n"
        "CAN      Canada    37.59   9984.67   1647.12  N.America  1867-07-01\n"
        "AUS   Australia    25.47   7692.02   1408.68    Oceania         NaN\n"
        "KAZ  Kazakhstan    18.53   2724.90    159.41       Asia  1991-12-16"
    )
    assert read_from_file_with_pandas(file_path) == expected_text
