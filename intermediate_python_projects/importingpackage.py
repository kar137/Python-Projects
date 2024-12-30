from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Province", "District", "City"]
table.add_rows([
    ["Koshi", "Sunsari", "Itahari"],
    ["Bagmati", "Kathmandu", "Kathmandu"],
])
table.align = "l"
print(table)