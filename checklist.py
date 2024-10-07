print ("Hello World")
checklist = list()
def my_fun_function(say_this):
    print(say_this)

my_fun_function('Hello World')

checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)

def create(item):
    checklist.append('Blue')

checklist[0]

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    item = checklist[index]
    return item

# READ
def read(index):
    return checklist[index]

checklist = ['Blue', 'Orange']
checklist[1] = 'Cats'
print (checklist)

# UPDATE
def update(index, item):
    checklist[index] = item

checklist = ['Blue', 'Cats']
checklist.pop(1)
print(checklist)

# DESTROY
def destroy(index):
    checklist.pop(index)

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))

    list_all_items()


for list_item in checklist:
    #Do something

    def list_all_items():
        for list_item in checklist:
            print(list_item)
def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1

def mark_completed(index):
    if 0 <= index < len(checklist):
        checklist[index] = "√ " + checklist[index]
    else:
        print("Wrong")

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input    
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

 



