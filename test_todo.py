import todo 

def test_add():
    todo_list = todo.TodoList()
    todo_list.add("хлеб")
    assert len(todo_list) == 1


def test_a():
    todo_list = todo.TodoList()
    todo_list.add("хлеб")
    assert todo_list.tasks[0].done == False

def test_b():
    todo_list = todo.TodoList()
    todo_list.add("хлеб")
    todo_list.complete(0)
    assert todo_list.tasks[0].done == False

def test_c():
    todo_list = todo.TodoList()
    assert len(todo_list) == 1

