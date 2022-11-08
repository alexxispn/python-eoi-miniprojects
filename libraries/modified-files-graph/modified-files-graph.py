import datetime
import os

today = datetime.date.today()
seven_days_ago = today - datetime.timedelta(days=7)
GRAPH_CHAR = '\u2589'


def get_modified_files():
    modified_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            file_path = os.path.join(root, file)
            modified_time = os.path.getmtime(file_path)
            modified_date = datetime.date.fromtimestamp(modified_time)
            if modified_date > seven_days_ago:
                modified_files.append(file_path)
    return modified_files


def get_modified_files_by_date():
    modified_files = get_modified_files()
    modified_files_by_date = {}
    for file in modified_files:
        modified_time = os.path.getmtime(file)
        modified_date = datetime.date.fromtimestamp(modified_time)
        if modified_date in modified_files_by_date:
            modified_files_by_date[modified_date] += 1
        else:
            modified_files_by_date[modified_date] = 1
    return modified_files_by_date


def print_graph_modified_files_by_date():
    modified_files_by_date = get_modified_files_by_date()
    for date, count in modified_files_by_date.items():
        print(f'{date} {GRAPH_CHAR * count}')


print_graph_modified_files_by_date()
