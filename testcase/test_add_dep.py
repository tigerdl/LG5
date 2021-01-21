from page.home_page import HomePage


class TestAddDep:

    def setup_class(self):
        self.main = HomePage()

    def test_add_department(self):
        result = self.main.goto_contacts().goto_add_department().add_department("部门q").get_dep_list()
        assert "部门q" in result

    def test_add_dep_fail(self):
        pass

