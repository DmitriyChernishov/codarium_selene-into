class Its:
    def __init__(self, xpath=""):
        self.xpath = xpath

    def have_id(self, id):
        self.xpath += f"//*[@id='{id}']"
        return self

    def with_class(self, class_name):
        self.xpath += f"[contains(@class, '{class_name}')]"
        return self #f"[contains(@class, '{class_name}')]"

    def with_text(self, text):
        self.xpath += f"[.//text()='{text}']"
        return self #f"[.//text()='{text}']"