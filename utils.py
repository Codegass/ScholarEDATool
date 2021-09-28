# Support functions #

def findAllFile(base):
    '''
    generator function
        Usage: for file in findAllFile(path):
                ...
        Walk through all the files in the path, 
        no matter how deep the file is hide. 

        It won't include folder as final result. 
    '''
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname