def contain_class(value):
    return f'contains(concat(" ", normalize-space(@class), " "), " {value} ")'