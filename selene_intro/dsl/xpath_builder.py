class X:

    def __init__(self, xpath=""):
        self.xpath = xpath

    @staticmethod
    def all():
        return X("//*")

    def descendant(self, tag=''):
        self.xpath += f"//*{tag}"
        return self

    def by(self, selector):
        self.xpath += f"[{selector}]"
        return self

    def by_not(self, selector):
        self.xpath += f"[not({selector})]"
        return self

    def child(self, value):
        self.xpath += f"/{value}"
        return self

    def build(self):
        return self.xpath