import inspect

class test_cls:
    def test_func(self):
        fun_name = inspect.stack()[1][3]
        print(fun_name)
    def use_func(self):
        self.test_func()

c = test_cls()
c.use_func()
