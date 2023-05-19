def contain_class(self, value):
    return f'contains(concat(" ", normalize-space(@class), " "), " {value} ")'


class XPathBuilder:
    @staticmethod
    def tag(tag_name):
        return XPathBuilder("/*")

    def __init__(self, xpath=""):
        self.xpath = xpath

    def have_id(self, id):
        self.xpath += f"//*[@id='{id}']"
        return self

    def with_class(self, class_name):
        self.xpath += f"[contains(@class, '{class_name}')]"
        return self

    def with_text(self, text):
        self.xpath += f"[.//text()='{text}']"
        return self

    def child(self, xpath):
        self.xpath += f"/{xpath}"
        return self

    def build(self):
        return self.xpath