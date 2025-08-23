#!/usr/bin/env python
"""
Script to create sample data for the EdTech platform
Run this after setting up the database and models
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edtech.settings')
django.setup()

from courses.models import Course, Lecture

def create_sample_data():
    """Create sample courses and lectures"""
    
    # Clear existing data
    Course.objects.all().delete()
    Lecture.objects.all().delete()
    
    print("Creating sample courses and lectures...")
    
    # Course 1: DSA - Advanced DSA from Basic (Python)
    dsa_course = Course.objects.create(
        title="DSA - Advanced DSA from Basic (Python)",
        description="Master Data Structures and Algorithms from fundamentals to advanced concepts. Learn problem-solving techniques, time complexity analysis, and implement solutions in Python. Perfect for coding interviews and competitive programming.",
        thumbnail="https://images.unsplash.com/photo-1517077304055-6e89abbf09b0?w=400&h=300&fit=crop"
    )
    
    # Lectures for DSA course
    dsa_lectures = [
        {
            "title": "Introduction to Data Structures",
            "youtube_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "questions": [
                {"title": "Array Basics", "platform": "LeetCode", "url": "https://leetcode.com/problems/two-sum/"},
                {"title": "String Manipulation", "platform": "GeeksforGeeks", "url": "https://practice.geeksforgeeks.org/problems/reverse-a-string/1"}
            ],
            "code": """# Introduction to Arrays in Python
def find_max(arr):
    if not arr:
        return None
    
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    
    return max_val

# Example usage
numbers = [3, 7, 2, 9, 1, 5]
result = find_max(numbers)
print(f"Maximum value: {result}")  # Output: Maximum value: 9""",
            "description": """# Introduction to Data Structures

Welcome to the first lecture of our **Data Structures and Algorithms** course! In this session, we'll explore the fundamental building blocks of computer science.

## What You'll Learn

- **Arrays and Lists**: Understanding sequential data storage
- **Basic Operations**: Insertion, deletion, and searching
- **Time Complexity**: Analyzing algorithm efficiency
- **Problem-Solving**: Applying data structures to real problems

## Key Concepts

### 1. Arrays
Arrays are the most basic data structure that stores elements in contiguous memory locations.

**Characteristics:**
- Fixed size (in most languages)
- Random access (O(1) time complexity)
- Sequential storage

### 2. Basic Operations

| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| Access    | O(1)           | Get element at index |
| Search    | O(n)           | Find element by value |
| Insert    | O(n)           | Add element at position |
| Delete    | O(n)           | Remove element |

### 3. Common Use Cases

- **Storing collections of data**
- **Implementing other data structures**
- **Matrix operations**
- **Buffer management**

## Practice Problems

1. **Two Sum**: Find two numbers that add up to a target
2. **Maximum Subarray**: Find the largest sum of contiguous elements
3. **Array Rotation**: Rotate array by k positions

> **Pro Tip**: Always consider edge cases when working with arrays - empty arrays, single elements, and boundary conditions.

## Next Steps

After this lecture, you'll be ready to:
- Implement array-based algorithms
- Understand time and space complexity
- Move on to more complex data structures

---

*Remember: Practice is key to mastering data structures!*""",
            "order": 1
        },
        {
            "title": "Linked Lists Implementation",
            "youtube_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "questions": [
                {"title": "Reverse Linked List", "platform": "LeetCode", "url": "https://leetcode.com/problems/reverse-linked-list/"},
                {"title": "Detect Cycle", "platform": "HackerRank", "url": "https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle"}
            ],
            "code": """# Linked List Node Class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Reverse Linked List Function
def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev

# Example usage
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Reverse the linked list
reversed_head = reverse_linked_list(head)

# Print reversed list
current = reversed_head
while current:
    print(current.val, end=" -> " if current.next else "")
    current = current.next
# Output: 5 -> 4 -> 3 -> 2 -> 1""",
            "description": """# Linked Lists Implementation

Building on our array knowledge, let's dive into **Linked Lists** - a dynamic data structure that grows and shrinks as needed.

## What Are Linked Lists?

A linked list is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence.

```
Node Structure:
┌─────────┬─────────┐
│  Data   │  Next   │
│ (Value) │ (Pointer)│
└─────────┴─────────┘
```

## Types of Linked Lists

### 1. Singly Linked List
- Each node has data and a pointer to the next node
- Last node points to `null`

### 2. Doubly Linked List
- Each node has data and pointers to both next and previous nodes
- Better for reverse traversal

### 3. Circular Linked List
- Last node points back to the first node
- Useful for round-robin scheduling

## Common Operations

| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| Insert at Head | O(1) | Add new node at beginning |
| Insert at Tail | O(n) | Add new node at end |
| Delete | O(n) | Remove node by value |
| Search | O(n) | Find node by value |

## Advantages vs Disadvantages

**Advantages:**
- Dynamic size
- Efficient insertion/deletion at beginning
- No wasted memory

**Disadvantages:**
- No random access
- Extra memory for pointers
- Cache unfriendly

## Implementation Tips

1. **Always handle edge cases**:
   - Empty list
   - Single node
   - First/last node operations

2. **Use dummy nodes** for easier head operations

3. **Keep track of tail** for O(1) append operations

## Common Interview Questions

- Reverse a linked list
- Detect cycle in linked list
- Find middle element
- Merge two sorted lists
- Remove duplicates

> **Note**: Linked lists are fundamental to understanding more complex data structures like trees and graphs.

---

*Practice these concepts with the provided code examples!*""",
            "order": 2
        },
        {
            "title": "Binary Trees and Traversals",
            "youtube_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "questions": [
                {"title": "Maximum Depth", "platform": "LeetCode", "url": "https://leetcode.com/problems/maximum-depth-of-binary-tree/"},
                {"title": "Level Order Traversal", "platform": "GeeksforGeeks", "url": "https://practice.geeksforgeeks.org/problems/level-order-traversal/1"}
            ],
            "code": """# Binary Tree Node Class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Inorder Traversal (Left -> Root -> Right)
def inorder_traversal(root):
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return result

# Preorder Traversal (Root -> Left -> Right)
def preorder_traversal(root):
    result = []
    
    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
    
    preorder(root)
    return result

# Postorder Traversal (Left -> Right -> Root)
def postorder_traversal(root):
    result = []
    
    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
    
    postorder(root)
    return result

# Example usage
# Create a binary tree:
#       1
#      / \\
#     2   3
#    / \\
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder:", inorder_traversal(root))    # [4, 2, 5, 1, 3]
print("Preorder:", preorder_traversal(root))  # [1, 2, 4, 5, 3]
print("Postorder:", postorder_traversal(root)) # [4, 5, 2, 3, 1]""",
            "description": "Explore binary trees and their various traversal methods. Understand inorder, preorder, and postorder traversals with practical implementations.",
            "order": 3
        }
    ]
    
    for lecture_data in dsa_lectures:
        Lecture.objects.create(course=dsa_course, **lecture_data)
    
    # Course 2: AI and ML - Machine Learning Course
    ml_course = Course.objects.create(
        title="AI and ML - Machine Learning Course",
        description="Dive into the world of Artificial Intelligence and Machine Learning. Learn fundamental concepts, algorithms, and practical implementations using Python libraries like scikit-learn, TensorFlow, and PyTorch.",
        thumbnail="https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400&h=300&fit=crop"
    )
    
    # Lectures for ML course
    ml_lectures = [
        {
            "title": "Introduction to Machine Learning",
            "youtube_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "questions": [
                {"title": "Linear Regression Basics", "platform": "Kaggle", "url": "https://www.kaggle.com/learn/intro-to-machine-learning"},
                {"title": "Data Preprocessing", "platform": "Coursera", "url": "https://www.coursera.org/learn/machine-learning"}
            ],
            "code": """# Introduction to Machine Learning with Python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate sample data
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 2 * X + 1 + np.random.randn(100, 1) * 0.5

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model coefficients: {model.coef_[0][0]:.2f}")
print(f"Model intercept: {model.intercept_[0]:.2f}")
print(f"Mean Squared Error: {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# Visualize results
import matplotlib.pyplot as plt
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression: Actual vs Predicted')
plt.legend()
plt.show()""",
            "description": "Get started with machine learning fundamentals. Learn about supervised vs unsupervised learning, data preprocessing, and your first ML model implementation.",
            "order": 1
        },
        {
            "title": "Classification Algorithms",
            "youtube_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "questions": [
                {"title": "Logistic Regression", "platform": "LeetCode", "url": "https://leetcode.com/problems/"},
                {"title": "Decision Trees", "platform": "GeeksforGeeks", "url": "https://practice.geeksforgeeks.org/"}
            ],
            "code": """# Classification Algorithms in Machine Learning
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Generate sample classification data
X, y = make_classification(
    n_samples=1000, n_features=20, n_informative=15,
    n_redundant=5, random_state=42
)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Logistic Regression
lr_model = LogisticRegression(random_state=42, max_iter=1000)
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)
lr_accuracy = accuracy_score(y_test, lr_pred)

# Decision Tree
dt_model = DecisionTreeClassifier(random_state=42, max_depth=5)
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_pred)

print("Logistic Regression Accuracy:", lr_accuracy)
print("Decision Tree Accuracy:", dt_accuracy)

# Compare models
print("\\nLogistic Regression Classification Report:")
print(classification_report(y_test, lr_pred))

print("\\nDecision Tree Classification Report:")
print(classification_report(y_test, dt_pred))

# Feature importance for Decision Tree
feature_importance = dt_model.feature_importances_
print("\\nTop 5 Most Important Features:")
top_features = np.argsort(feature_importance)[-5:]
for i, feature_idx in enumerate(reversed(top_features)):
    print(f"{i+1}. Feature {feature_idx}: {feature_importance[feature_idx]:.4f}")""",
            "description": "Explore classification algorithms including logistic regression and decision trees. Learn how to evaluate model performance and interpret results.",
            "order": 2
        }
    ]
    
    for lecture_data in ml_lectures:
        Lecture.objects.create(course=ml_course, **lecture_data)
    
    # Course 3: Full Stack Development Course
    fullstack_course = Course.objects.create(
        title="Full Stack Development Course",
        description="Build complete web applications from frontend to backend. Learn modern web technologies including React, Node.js, databases, and deployment strategies. Create real-world projects and deploy them to production.",
        thumbnail="https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=400&h=300&fit=crop"
    )
    
    # Lectures for Full Stack course
    fullstack_lectures = [
        {
            "title": "React Fundamentals",
            "youtube_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "questions": [
                {"title": "Component Lifecycle", "platform": "React Docs", "url": "https://react.dev/"},
                {"title": "State Management", "platform": "Redux", "url": "https://redux.js.org/"}
            ],
            "code": """// React Component Example
import React, { useState, useEffect } from 'react';

const TodoApp = () => {
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [filter, setFilter] = useState('all');

  useEffect(() => {
    // Load todos from localStorage on component mount
    const savedTodos = localStorage.getItem('todos');
    if (savedTodos) {
      setTodos(JSON.parse(savedTodos));
    }
  }, []);

  useEffect(() => {
    // Save todos to localStorage whenever todos change
    localStorage.setItem('todos', JSON.stringify(todos));
  }, [todos]);

  const addTodo = (e) => {
    e.preventDefault();
    if (inputValue.trim()) {
      const newTodo = {
        id: Date.now(),
        text: inputValue.trim(),
        completed: false,
        createdAt: new Date().toISOString()
      };
      setTodos([...todos, newTodo]);
      setInputValue('');
    }
  };

  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  const filteredTodos = todos.filter(todo => {
    if (filter === 'active') return !todo.completed;
    if (filter === 'completed') return todo.completed;
    return true;
  });

  return (
    <div className="max-w-md mx-auto mt-8 p-6 bg-white rounded-lg shadow-lg">
      <h1 className="text-2xl font-bold text-gray-800 mb-6">Todo App</h1>
      
      <form onSubmit={addTodo} className="mb-6">
        <div className="flex gap-2">
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Add a new todo..."
            className="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            type="submit"
            className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
          >
            Add
          </button>
        </div>
      </form>

      <div className="mb-4">
        <div className="flex gap-2">
          {['all', 'active', 'completed'].map(filterType => (
            <button
              key={filterType}
              onClick={() => setFilter(filterType)}
              className={`px-3 py-1 rounded-lg text-sm capitalize transition-colors ${
                filter === filterType
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
              }`}
            >
              {filterType}
            </button>
          ))}
        </div>
      </div>

      <ul className="space-y-2">
        {filteredTodos.map(todo => (
          <li
            key={todo.id}
            className="flex items-center gap-3 p-3 bg-gray-50 rounded-lg"
          >
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => toggleTodo(todo.id)}
              className="w-4 h-4 text-blue-600 rounded focus:ring-blue-500"
            />
            <span
              className={`flex-1 ${
                todo.completed ? 'line-through text-gray-500' : 'text-gray-800'
              }`}
            >
              {todo.text}
            </span>
            <button
              onClick={() => deleteTodo(todo.id)}
              className="text-red-500 hover:text-red-700 transition-colors"
            >
              ×
            </button>
          </li>
        ))}
      </ul>

      {filteredTodos.length === 0 && (
        <p className="text-center text-gray-500 mt-4">
          No todos found. {filter !== 'all' && 'Try changing the filter.'}
        </p>
      )}
    </div>
  );
};

export default TodoApp;""",
            "description": "Learn React fundamentals including components, state management, hooks, and modern React patterns. Build interactive user interfaces with best practices.",
            "order": 1
        },
        {
            "title": "Backend API Development",
            "youtube_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "questions": [
                {"title": "REST API Design", "platform": "MDN", "url": "https://developer.mozilla.org/en-US/docs/Glossary/REST"},
                {"title": "Authentication", "platform": "JWT", "url": "https://jwt.io/"}
            ],
            "code": """# FastAPI Backend Example
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import jwt
from datetime import datetime, timedelta
import uvicorn

app = FastAPI(title="Todo API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

security = HTTPBearer()

# Pydantic models
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class User(BaseModel):
    username: str
    email: str

class UserCreate(User):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# In-memory storage (replace with database in production)
todos_db = []
users_db = []
current_user_id = 1

# Helper functions
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user_id
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Authentication endpoints
@app.post("/auth/register", response_model=Token)
async def register(user: UserCreate):
    # Check if user already exists
    if any(u["username"] == user.username for u in users_db):
        raise HTTPException(status_code=400, detail="Username already registered")
    
    if any(u["email"] == user.email for u in users_db):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # In production, hash the password
    new_user = {
        "id": current_user_id,
        "username": user.username,
        "email": user.email,
        "password": user.password  # Hash this in production!
    }
    users_db.append(new_user)
    
    global current_user_id
    current_user_id += 1
    
    # Create access token
    access_token = create_access_token(data={"sub": new_user["id"]})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/auth/login", response_model=Token)
async def login(username: str, password: str):
    user = next((u for u in users_db if u["username"] == username and u["password"] == password), None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user["id"]})
    return {"access_token": access_token, "token_type": "bearer"}

# Todo endpoints
@app.get("/todos", response_model=List[Todo])
async def get_todos(user_id: int = Depends(verify_token)):
    user_todos = [todo for todo in todos_db if todo["user_id"] == user_id]
    return user_todos

@app.post("/todos", response_model=Todo)
async def create_todo(todo: TodoCreate, user_id: int = Depends(verify_token)):
    new_todo = {
        "id": len(todos_db) + 1,
        "user_id": user_id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    todos_db.append(new_todo)
    return new_todo

@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo_update: TodoCreate, user_id: int = Depends(verify_token)):
    todo = next((t for t in todos_db if t["id"] == todo_id and t["user_id"] == user_id), None)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo.update({
        "title": todo_update.title,
        "description": todo_update.description,
        "completed": todo_update.completed,
        "updated_at": datetime.utcnow()
    })
    return todo

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, user_id: int = Depends(verify_token)):
    todo = next((t for t in todos_db if t["id"] == todo_id and t["user_id"] == user_id), None)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todos_db.remove(todo)
    return {"message": "Todo deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)""",
            "description": "Build robust backend APIs using FastAPI. Learn about authentication, database design, and API best practices for production applications.",
            "order": 2
        }
    ]
    
    for lecture_data in fullstack_lectures:
        Lecture.objects.create(course=fullstack_course, **lecture_data)
    
    print(f"✅ Created {Course.objects.count()} courses")
    print(f"✅ Created {Lecture.objects.count()} lectures")
    print("\nSample data created successfully!")
    print("\nYou can now:")
    print("1. Run the Django server: python manage.py runserver")
    print("2. Start the React frontend: npm run dev")
    print("3. Visit http://localhost:3000 to see your EdTech platform!")

if __name__ == "__main__":
    create_sample_data() 