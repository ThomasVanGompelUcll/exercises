def make_path(parts):
    string = ''
    for part in parts:
        string += part + '/'
    return string[:len(string)-1]

