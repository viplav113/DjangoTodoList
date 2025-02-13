# To-Do List API with Django REST Framework

A RESTful API for managing tasks built with Django REST Framework.

![Screenshot 2025-02-13 230918](https://github.com/user-attachments/assets/a02481f3-9816-47d9-bcfe-972780eea469)
 
 *Django REST Framework Interface Example*

## Features

- Create, Read, Update, Delete (CRUD) operations for tasks
- RESTful endpoints with proper HTTP status codes
- Error handling for invalid requests
- JSON-based interaction

## API Endpoints

| Endpoint          | Method | Description                      |
|-------------------|--------|----------------------------------|
| `/tasks/add/`     | POST   | Create new task                  |
| `/tasks/`         | GET    | List all tasks                   |
| `/tasks/<id>/`    | GET    | Get single task                  |
| `/tasks/<id>/`    | PUT    | Update entire task               |
| `/tasks/<id>/`    | DELETE | Remove task                      |

## Installation

1. **Clone repository**
   ```bash
   git clone https://github.com/your-username/todo-api.git
   cd todo-api
   Install requirements
   
2. **Install requirements**
    ```bash
    pip install django djangorestframework
    ```
3. **Run migrations**
    ```bash
    python manage.py migrate
    ```
4. **Start server**
    ```bash
    python manage.py runserver
    ```
API available at: `http://localhost:8000/tasks/`

## Usage

### Create a Task (POST)
curl http://localhost:8000/tasks/add/
```bash
{
    "title": "Buy groceries",
    "completed": false
}
```
### Get All Tasks (GET)
curl http://localhost:8000/tasks/
### Response:
```bash
[
    {
        "id": 1,
        "title": "Buy groceries",
        "completed": false
    }
]
```
### Update a Task (PUT)
curl http://localhost:8000/tasks/1
### Response:
```bash
{
    "title": "Buy groceries id 1 edited",
    "completed": false
}
```

### Response:
```bash
[
    {
        "id": 1,
        "title": "Buy groceries id 1 edited",
        "completed": false
    }
]
```

### Delete a Task (DELETE)

curl -X DELETE http://localhost:8000/tasks/1/

## Screenshots
1. To add task
![Screenshot 2025-02-13 230918](https://github.com/user-attachments/assets/75994dae-3b4f-4840-907d-710e15e294d8)

2. To get task by id
![Screenshot 2025-02-13 231007](https://github.com/user-attachments/assets/7a008671-52cd-4f63-9634-ada23eacab87)

3. To get all tasks
![Screenshot 2025-02-13 233535](https://github.com/user-attachments/assets/06df0d05-5f4b-4565-8d31-3482c995ff45)

4. To delete task
![Screenshot 2025-02-13 233551](https://github.com/user-attachments/assets/2a000bc7-0411-43e2-bed8-c52e1b355bf7)



