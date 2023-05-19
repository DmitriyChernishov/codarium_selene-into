class X:

    def __init__(self, selector=""):
        self.by = selector

    @staticmethod
    def all():
        return X("//*")

    def child(self, xpath):
        self.xpath += f"/{xpath}"
        return self

    def build(self):
        return self.xpath