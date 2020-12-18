class BasicSetting:
    url = ""
    sleep_time = 0

    def set_all(self, url, sleep_time):
        self.url = url
        self.sleep_time = sleep_time
        pass

    def get_all(self):
        all_setting = (self.url, self.sleep_time)
        return all_setting
    pass
