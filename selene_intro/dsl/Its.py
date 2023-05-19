class Its:
    @staticmethod
    def have_id(self, id):
        self.xpath += f"//*[@id='{id}']"
        return self

    def with_class(self, class_name):
        self.xpath += f"[contains(@class, '{class_name}')]"
        return self

    def with_text(self, text):
        self.xpath += f"[.//text()='{text}']"
        return self