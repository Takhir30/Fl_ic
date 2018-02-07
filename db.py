def set_address(file_name):
    with open(file_name) as fn:
        var = {line.strip().split(' ')[0]:line.strip().split(' ')[2] for line in fn}
    login = var['login']
    password = var['password']
    dbname = var['dbname']
    host = var['host']
    return f"postgresql://{login}:{password}@{host}/{dbname}"
