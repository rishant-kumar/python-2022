# 28/03/2022 work P4
names = ['Patrick', "David"]

def adding_names(names):
    repeat = True
    while repeat:
        add_name = input("What name would you like to add? ").title()
        names.append(add_name)
        print(", ".join(names))
        repeat_error = True
        while repeat_error:
            add_more_names = input("Would you like to add more names? yes/no: ").strip().lower()
            if add_more_names == 'yes':
                repeat = True
                repeat_error = False
            elif add_more_names == 'no':
                repeat = False
                repeat_error = False
            else:
                print("Enter 'yes' or 'no'")
                repeat_error = True
    return names

def removing_names(names):
    repeat = True
    while repeat:
        remove_name = input("What name would you like to remove? ").title()
        names.remove(remove_name)
        print(", ".join(names))
        repeat_error = True
        while repeat_error:
            remove_more_names = input("Would you like to remove more names? yes/no: ").strip().lower()
            if remove_more_names == 'yes':
                repeat = True
                repeat_error = False
            elif remove_more_names == 'no':
                repeat = False
                repeat_error = False
            else:
                print("Enter 'yes' or 'no'")
                repeat_error = True
    return names

# prints current list (will print patrick and david)
print("Current names in list are: ")
if len(names) == 0:
    print("No names in current list")
else:
    print(", ".join(names))

# add names to list
start_adding_names = input("Would you like to add names to list? yes/no: ").strip().lower()
if start_adding_names == 'yes':
    adding_names(names)
elif start_adding_names == 'no':
    pass
else:
    print("Enter 'yes' or 'no'")

# remove names from list    
start_removing_names = input("Would you like to remove names to list? yes/no: ").strip().lower()
if start_removing_names == 'yes':
    removing_names(names)
elif start_removing_names == 'no':
    pass
else:
    print("Enter 'yes' or 'no'")

# prints final list
if len(names) == 0:
    print("No names in final list!")
else:
    for name in names:
        print("We have {} in list" .format(name))
# Copyright - Rishant
