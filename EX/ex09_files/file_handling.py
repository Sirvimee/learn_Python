"""File handling."""
import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into a string.

    In this exercise, assume that the file exists.

    :param filename: The name of the file to read.
    :return: The contents of the file as a string.
    """
    with open(filename) as f:
        return str(f.read())


def read_file_contents_to_list(filename: str) -> list[str]:
    r"""
    Read file contents into a list of lines.

    In this exercise, assume that the file exists.

    Each line from the file is a separate element in the list,
    and the order of the list matches the order in the file.
    Newline characters ('\n') are removed from each line.

    :param filename: The name of the file to read.
    :return: A list of lines without newline characters.
    """
    with open(filename) as f:
        lines = f.readlines()
        data = [line.strip() for line in lines]
    return data


def read_csv_file(filename: str, delimiter: str = ",") -> list[list[str]]:
    """
    Read CSV file contents into a list of rows.

    Each row is represented as a list of "columns" or fields.

    Example CSV (Comma-separated values) data:
    name,age
    john,12
    mary,14

    Will return as:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Note: The "csv" module should be used.

    :param delimiter: A character used to separate or distinguish elements in a data structure.
    :param filename: The name of the file to read.
    :return: A list of lists, where each inner list represents a row of CSV data.
    """
    with open(filename) as f:
        lines = csv.reader(f, delimiter=delimiter)
        data = [line for line in lines]
        return data


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to a file.

    If the file does not exist, it will be created.
    If the file already exists, its contents will be overwritten.

    :param filename: The name of the file to write to.
    :param contents: The content to write to the file.
    :return: None
    """
    with open(filename, "w") as f:
        f.write(contents)


def write_lines_to_file(filename: str, lines: list[str]) -> None:
    """
    Write lines to a file.

    Each string in the 'lines' list represents a separate line in the file.
    The function ensures that there is no extra newline added at the end of the file,
    unless the last element in the 'lines' list itself ends with a newline.

    :param filename: The name of the file to write to.
    :param lines: A list of strings, each representing a line to write to the file.
    :return: None
    """
    with open(filename, "w") as f:
        if len(lines) == 0:
            return
        elif len(lines) == 1:
            f.write(lines[0])
        else:
            for line in lines[:-1]:
                f.write(line.rstrip('\n') + '\n')


def write_csv_file(filename: str, data: list[list[str]]) -> None:
    """
    Write data into a CSV file.

    The data is a list of lists, where each inner list represents a row,
    and the elements within each inner list represent the columns.

    Example data:
    [["name", "age"], ["john", "11"], ["mary", "15"]]

    Will be written in the .csv file as:
    name,age
    john,11
    mary,15

    Note: The "csv" module should be used.

    :param filename: The name of the file to write to.
    :param data: A list of lists to write to the file, where each list represents a row.
    :return: None
    """
    with open(filename, "w", newline="") as f:
        csv_writer = csv.writer(f, delimiter=",")
        for line in data:
            csv_writer.writerow(line)


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two input CSV files into one output CSV file.

    The dates file contains names and dates separated by a colon, and the towns file contains
    names and towns separated by a colon. Both files have no headers.

    Example format of the dates file:
    john:01.01.2001
    mary:06.03.2016

    Example format of the towns file:
    john:london
    mary:new york

    The merging is performed based on the names found in input files.
    The order of the lines in the output file follows the order in the dates input file.
    Names that are missing in the dates input file will follow the order in the towns input file.
    The order of the fields is: name, town, date.

    The resulting CSV file should have the following format:
    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be represented as "-" in the output file.

    Example:
    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Reuse CSV reading and writing functions.
    Note: When reading CSV files, specify the delimiter (improve existing method).

    :param dates_filename: The name of the CSV file with names and dates (name:date).
    :param towns_filename: The name of the CSV file with names and towns (name:town).
    :param csv_output_filename: The name of the CSV file to write to names, towns, and dates.
    :return: None
    """
    dates = read_csv_file(dates_filename, ":")
    towns = read_csv_file(towns_filename, ":")
    result = [["name", "town", "date"]]
    filename = csv_output_filename

    for date in dates:
        date.insert(1, "-")
        result.append(date)

    for town in towns:
        if town[0] not in [name[0] for name in result]:
            town.insert(2, "-")
            result.append(town)
        else:
            for name in result:
                if name[0] == town[0]:
                    name[1] = town[1]

    write_csv_file(filename, result)


def read_csv_file_into_list_of_dicts(filename: str) -> list[dict[str, str]]:
    """
    Read a CSV file into a list of dictionaries.

    The header line of the CSV file will be used as keys for the dictionaries.
    If there are only headers or no rows in the CSV file, the result is an empty list.
    Each line after the header line will result in a dictionary inside the result list.
    Every line should contain the same number of fields.
    The order of the elements in the list corresponds to the lines in the file
    (the first line becomes the first element, and so on).

    Given a CSV file like this:
    name,age,sex
    John,12,M
    Mary,13,F

    The result will be:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    :param filename: The name of the CSV file to read.
    :return: A list of dictionaries where keys are taken from the header and values are strings.
    """
    result_list = []
    data = read_csv_file(filename)
    header = data[0]

    if len(data) <= 1:
        return result_list

    for row in data[1:]:
        values = row
        entry = {}
        for i in range(len(header)):
            entry[header[i]] = values[i]
        result_list.append(entry)

    return result_list


def write_list_of_dicts_to_csv_file(filename: str, data: list[dict]) -> None:
    """
    Write a list of dictionaries to a CSV file.

    Each dictionary in the 'data' list represents a row in the CSV file,
    with dictionary keys representing the fields of a header.
    Fields missing in certain rows will be empty in these rows.
    The order of rows in the file matches the order of elements in the list.

    Example data:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]

    This data will be written to the CSV file as:
    name,age,town
    john,12,
    mary,,London

    :param filename: The name of the file to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    headers = []
    for row in data:
        for key in row.keys():
            if key not in headers:
                headers.append(key)

    for row in data:
        for header in headers:
            if header not in row.keys():
                row[header] = ""

    result = [headers]
    for row in data:
        result.append([row[key] for key in headers])

    write_csv_file(filename, result)
