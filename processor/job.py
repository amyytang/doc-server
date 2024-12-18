import csv

CSV_FILE = "data.csv"
def insert(c1_value, c2_value, c3_value):
    line_exists = False
    with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:
                    continue
                if row[0] == c1_value and row[1] == c2_value and row[2] == c3_value:
                    line_exists = True
                    break
    if not line_exists:                
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([c1_value, c2_value, c3_value])

def delete(c1_value, c2_value=None, c3_value=None):
    rows = []
    if c2_value == None:
        if c3_value == None:
            with open(CSV_FILE, mode='r') as file:
                reader = csv.reader(file)
                rows = [row for row in reader if row[0] != c1_value]
    elif c3_value == None:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            rows = [row for row in reader if not (row[0] == c1_value and row[1] == c2_value)]
    else:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            rows = [row for row in reader if not (row[0] == c1_value and row[1] == c2_value and row[2] == c3_value)]
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def update(c1_value, c2_value, c3_value, column_number, update_value):
    rows = []
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if c2_value == None and c3_value == None and row[0] == c1_value:
                row[column_number] = update_value
            elif c3_value == None and row[0] == c1_value and row[1] == c2_value:
                row[column_number] = update_value
            elif row[0] == c1_value and row[1] == c2_value and row[2] == c3_value:
                row[column_number] = update_value
        rows.append(row)
        file.close()

    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        file.close()

#def main():
#    insert("China", "Best University", "Zhejiang University")
#    insert("UK", "Company", "DeepMind")
#    delete("UK")
#    update("China", "Best University", "Zhejiang University", 2, "Tsinghua University")
#if __name__ == "__main__":
#        main()