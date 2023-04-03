def test_abc():
    todomvc_testing.given_opened('a', 'b', 'c')
    todomvc_testing.should_be('a', 'b', 'c', )
    todomvc_testing.toggle('a')
    todomvc_testing.toggle('b')
    todomvc_testing.should_be_comleted('c')


class TodoMVC:
    def __init__(self):
        self.todo_list = selene.browser.all('todo-list>li')

    def open(self):
        selene.browser.open('https://todomvc4tasj.herokuapp.com/')
        return self

    def add(self, *todos: str):
        for todo in todos:
            selene.browser.element('new-todo').type(todo).press_enter()
            return self
    def given_opened(self, *todos: str):
        self.open()
        self.add(*todos)
    def should_be(self, *todos: str):
