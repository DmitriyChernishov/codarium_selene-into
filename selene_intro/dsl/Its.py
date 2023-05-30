def id(value):
    return f'@id="{value}"'


def css_class(value):
    return f'contains(@class, "{value}")'


def text(value):
    return f'.//text()="{value}"'


def by_not(condition):
    return f'not({condition})'