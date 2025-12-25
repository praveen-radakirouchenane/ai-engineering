document.getElementById('addButton').addEventListener('click', function() {
    const input = document.getElementById('todoInput');
    const newTodo = input.value;
    if (newTodo) {
        const li = document.createElement('li');
        li.textContent = newTodo;
        document.getElementById('todoList').appendChild(li);
        input.value = '';
    }
});
