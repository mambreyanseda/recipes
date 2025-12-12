import csv, json

def open_file_read(filename):
    return open(filename, "r")

def open_file_write(filename):
    return open(filename, "w")

def read_json_file(filename):
    with open_file_read(filename) as file:
        content = file.read()
        if content.strip() == "":
            return {}
        return json.loads(content)

def write_json_file(filename, data):
    with open_file_write(filename) as file:
        json.dump(data, file)

def read_csv_file(filename):
    data_list = []
    with open_file_read(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_list.append(row)
    return data_list

def write_csv_file(filename, data_list, fieldnames):
    with open_file_write(filename) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)

def comma_string_to_list(comma_str):
    if not comma_str or comma_str.strip() == "":
        return []
    comma_str = comma_str.replace('"','').strip()
    result = []
    for x in comma_str.split(","):
        x = x.strip()
        if x.isdigit():
            result.append(x)
    return result

