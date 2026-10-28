import pytest
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
    with pytest.raises(todo.TodoError):
        todo_list.complete(7)
        

def test_complete():
    todo_list = todo.TodoList()
    todo_list.add("яйца")
    todo_list.complete(0)
    assert todo_list.tasks[0].done == True


def test_save_and_load(tmp_path):
    path = tmp_path / "todo.json"
    todo_list = todo.TodoList()
    todo_list.add("молочко")
    todo_list.add("яйки")
    todo_list.save(path)

    other = todo.TodoList()
    other.load(path)           
    assert len(other) == 2 


def test_missing_loading_file(tmp_path):
    todo_list = todo.TodoList()
    todo_list.load(tmp_path / "todo.json")
    assert len(todo_list) == 0


def test_pending():
    todo_list = todo.TodoList()
    todo_list.add("хлеб")
    todo_list.add("молоко")
    todo_list.complete(0)

    result = list(todo_list.pending())
    assert len(result) == 1
    assert result[0].title == "молоко"