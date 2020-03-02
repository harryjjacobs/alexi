INFO_FILE = "twitter_info.json"

class Twitter():
    def __init__(self):
        self.load_info()

    def __del__(self):
        self.save_info()

    def load_info(self):
        # read configuration
        self.info = ""

    def save_info(self):
        # write configuration
        info = ""