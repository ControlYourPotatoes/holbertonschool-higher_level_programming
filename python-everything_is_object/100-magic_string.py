def magic_string():
    """Function to create a magic string"""
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return "Holberton" + ", Holberton" * (magic_string.count - 1)
