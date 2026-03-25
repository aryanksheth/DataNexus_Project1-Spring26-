import time
import csv

def clean_job_dataset(filename, columns_to_keep, output_file):

    # 1) READ FILE
    with open(filename, newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        lines = list(reader)

    # 2) HEADER
    header = lines[0]

    # 3) FIND INDEXES
    indexes = []
    for i in range(len(header)):
        if header[i] in columns_to_keep:
            indexes.append(i)

    selected_headers = []
    for i in indexes:
        selected_headers.append(header[i])

    cleaned_rows = []

    # 4) PROCESS ROWS
    for row in lines[1:]:
        filtered_row = []
        for i in indexes:
            if i < len(row):
                filtered_row.append(row[i])
            else:
                filtered_row.append("")
        cleaned_rows.append(filtered_row)

    # 5) OUTPUT FILE
    timestamp = str(int(time.time()))
    output_name = output_file + "_" + timestamp + ".csv"

    with open(output_name, "w", newline='', encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(selected_headers)
        writer.writerows(cleaned_rows)

    print("Saved file:", output_name)