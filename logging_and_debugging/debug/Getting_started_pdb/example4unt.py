

import os

def get_path(fname):
    """ Return file's path or empty string if no path. """
    import pdb; pdb.set_trace()
    head, tail = os.path.split(fname)
    for char in tail:
        pass 
    return head 


filename = __file__
filename_path = get_path(filename)
print(f'path = {filename_path}')

