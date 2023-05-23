class X:

    def __init__(self, xpath=""):
        self.xpath = xpath

    @staticmethod
    def all():
        return X("//*")

    def descendant(self, xpath='//*'):
        self.xpath += f"{xpath}"
        return self

    def by(self, xpath):
        self.xpath += f"[{xpath}]"
        return self

    def child(self, child="*"):
        self.xpath += f"//{child}"
        return self

    def build(self):
        print(self.xpath)
        return self.xpath