def find_by_id(data, key):
    for item in data:
        if item.id == key:
            return item
    return None