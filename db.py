def set_address(file_name):
    with open(file_name) as fn:
        var = {line.strip().split(' ')[0]:line.strip().split(' ')[2] for line in fn}
    login = var['login']
    password = var['password']
    db = ['name']
    host = ['host']
    return f"postgresql://{login}:{password}@{host}/{dbname}"
