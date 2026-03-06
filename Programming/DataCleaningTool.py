import time 

def clean_job_dataset(filename, columns_to_keep, output_file):
    
    # 1) READING THE FILE:
    file = open(filename,"r",encoding="utf-8")
    lines = file.readlines()
    file.close()

    # 2) SPLITTING THE HEADER:
    header = lines[0].strip().split(",")

    # 3) FIND INDEXES OF COLUMNS TO KEEP
    indexes = []
    for i in range(len(header)):
        if header[i] in columns_to_keep:
            indexes.append(i)

    selected_headers = []
    for i in indexes:
        selected_headers.append(headers[i])

    cleaned_rows = []
    # 4) PROCESSING THE ROWS
    
    for line in lines[1:]:
        row = line.strip().split(",")

        filtered_row = []
        for i in indexes:
            if i < len(row):
                filtered_row.append(row[i])
            else:
                filtered_row.append("")

        cleaned_rows.append(filtered_row)

    # 5) CREATING OUTPUT FILE BASED ON TIME/DATE: