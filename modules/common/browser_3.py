# modules/common/browser_3.py

class Browser3:
    def __init__(self, name="DefaultBrowser"):
        self.name = name

    def get_info(self):
        return f"Browser3: {self.name}"

    def is_secure(self):
        return True
