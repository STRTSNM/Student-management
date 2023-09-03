import csv

req_name_list = []  # Will be edited according to usage
name_list = []  # Contains all names

# Adding all names to name_list
with open('list.csv', 'r') as k:
    kc = csv.reader(k)
    for row in kc:
        if row:  # Check if the row is not empty
            name_list.append(row[0])

print("Name list: ", name_list)

#'def' is assigned to any of class,route or bus stop if it is not to be used. This is for future use.

def get_by_class(classs='def', route='def', bus_stop='def'):
    global req_name_list

    temp_name_list = []
    with open('list.csv', 'r') as f:
        fc = csv.reader(f)
        i = 0

        for row in fc:
            if row:  # Check if the row is not empty
                # Check all three criteria: classs, route, and bus_stop
                if (
                    (classs == 'def' or classs == row[1]) and
                    (route == 'def' or route == row[2]) and
                    (bus_stop == 'def' or bus_stop == row[3])
                ):
                    temp_name_list.append(i)
                i += 1

    req_name_list = [name_list[ind] for ind in temp_name_list]


# Example usage with all criteria specified
get_by_class("xii", 'def', 'vels hotel')
print(req_name_list)
