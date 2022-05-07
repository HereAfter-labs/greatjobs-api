# import csv
#
# def check_data(username, password):
#     file = open("data/data.csv")
#     csvreader = csv.reader(file)
#
#     header = next(csvreader)
#
#     rows = []
#     for row in csvreader:
#         rows.append(row)
#     file.close()
#
#     for row in rows:
#         if row[1] == username and row[2] == password:
#             return row[0]
#
#     return 'err'
#
#
