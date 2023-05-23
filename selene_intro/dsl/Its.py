class Its:
    def __init__(self, xpath=''):
        self.xpath = xpath

    def have_id(self, id):
        self.xpath += f'@id="{id}"'
        return f'@id="{id}"'

    def with_class(self, class_name):
        self.xpath += f'contains(@class, "{class_name}")'
        return f'contains(@class, "{class_name}")'

    """
    def without_class(self, class_name):
        self.xpath += f'not(contains(@class, "{class_name}"))'
        return f'not(contains(@class, "{class_name}"))'
    """

    def by_not(self, condition):
        return f'not({condition})'

    def with_text(self, text):
        self.xpath += f'[.//text()="{text}"]'
        return f'.//text()="{text}"'