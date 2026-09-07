from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Age", "City"]
table.add_row(["Alice", 25, "Delhi"])
table.add_row(["Bob", 30, "Mumbai"])

table.align = "c"
print(table)
