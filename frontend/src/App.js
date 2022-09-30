import React, { useState, useEffect } from 'react';
import './App.css';
import TodoListView from './components/TodoListView';
import axios from 'axios';

function App() {
  const [todoList, setTodoList] = useState([{}])
  const [title, setTitle] = useState('')
  const [desc, setDesc] = useState('')

  useEffect(() => {
    axios.get('http://localhost:8000/all/')
      .then(res => {
        setTodoList(res.data)
      })
  });

  const addTodoHandler = () => {
    axios.post('http://localhost:8000/todo/', { 'title': title, 'description': desc })
      .then(res => console.log(res))
  }

  return (
    <div className="App">
      <h1>Todo List</h1>
      <TodoListView todoList={todoList} setTodoList={setTodoList}/>
        <p>Add todo</p>
        <input onChange={event => setTitle(event.target.value)} placeholder='Title' /> 
        <input onChange={event => setDesc(event.target.value)} placeholder='Description' />
        <button onClick={addTodoHandler}>Add</button>
    </div>
  );
}

export default App;