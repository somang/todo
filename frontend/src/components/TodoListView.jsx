
import React from 'react';
import Todo from './Todo'


export default function TodoListView(props) {

    return (
        <div>
            <ul>
                {props.todoList.map((todo, i) => <Todo todo={todo} key={i} />)}
            </ul>
        </div>
    )
}