def write(f_path, string):
    f = open(f_path, 'w')
    f.write(string)
    f.close()


def read(f_path):
    f = open(f_path, "r")
    text = f.read()
    f.close()
    return text
