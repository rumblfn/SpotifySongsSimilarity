import json


def save_json(data, filename):
    with open(f'output/{filename}', 'w') as f:
        json.dump(data, f)
        print(f'{filename} saved.')
