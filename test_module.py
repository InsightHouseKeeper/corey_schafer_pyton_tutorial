
print('Imported test_module.py')

test = 'Test String'

def find_index(iter_obj, target):
    '''Return index of the obj'''
    for i, value in enumerate(iter_obj):
        if value == target:
            return i

    return -1