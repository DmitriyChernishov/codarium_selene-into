def contain_class(value):
    return f'//*[contains(concat(" ", normalize-space(@class), " "), " {value} ")]'


def not_contain_class(value):
    return f'[not(contains(concat(" ", normalize-space(@class), " "), " {value} "))]'