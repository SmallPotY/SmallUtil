import os


def get_file(file_dir):
    lists = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] not in ['.py', '.pyc']:
                lists.append(os.path.basename(file))
    return lists


files = get_file(r'/home/HR/web/static/tmp')

for file in files:
    os.remove('/home/HR/web/static/tmp/' + file)
