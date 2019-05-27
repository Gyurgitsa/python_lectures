
import operator

from prettytable import PrettyTable

table = PrettyTable(["animal", "ferocity"])

table.add_row(["wolverine", 100])
table.add_row(["grizzly", 87])
table.add_row(["cat", -1])
table.add_row(["dolphin", 63])

print(table.get_string(sort_key=operator.itemgetter(1,0), sortby="animal"))

# print(table)
