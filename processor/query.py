import csv
import json

def query(condition):
    if "==" not in condition:
         return json.dumps({"msg": "Invalid Query: == not in query"})
    column_indices = {"C1": 0, "C2": 1, "C3": 2}
    column, _, value = condition.partition("==")
    column, value = column.strip(), value.strip().strip("'").strip('"')
    if column not in column_indices:
        return json.dumps({"msg": "Invalid Query: Invalid Column Name. Please use C1, C2, C3."})
    column_index = column_indices[column]
    matching_rows = [] 
    with open("data.csv", mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[column_index] == value:
                matching_rows.append(row)
    return json.dumps({"result": matching_rows})

#def main():
#    result = query("C1 == 'China'")
#    print("Query Result:", result)
#
#if __name__ == "__main__":
#        main()