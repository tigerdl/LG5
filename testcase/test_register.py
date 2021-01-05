from page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_register().register()

    def teardown(self):
        self.main._driver.quit()