calls = 0
def count_calls()  :
    global calls
    calls += 1
def string_info(string):
    count_calls()
    my_tuple = (len(string), string.upper(), string.lower())
    return my_tuple
def is_contains(string, list_to_seach):
    count_calls()

    for i in list_to_seach:
        if ((i.lower()for i in list_to_seach)
                and (i.lower() == string.lower())):

                return True
    else:
                return False

print(string_info('Nosorog'))
print(string_info('Rossomaha'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('Cycle', ['ONE', 'two', 'Third']))
print(calls)
