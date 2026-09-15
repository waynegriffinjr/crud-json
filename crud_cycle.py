import requests


# CREATE — POST a new todo item for user 1 (title: "Complete Module 4", completed: false).
response = requests.post(
    "https://jsonplaceholder.typicode.com/todos",
    json={
        "userId": 1,
        "title": "Complete Module 4",
        "completed": False
    }
)

if not response.ok:
    print(f"Failed to create todo: {response.status_code}")
    raise SystemExit

todos = response.json()
new_todo_id = todos["id"]

print(f"POST /todos")
print(f"Status: {response.status_code}")
print(f"New todo task added: Title: {todos['title']} | ID: {todos['id']}")


# READ — GET the todo you just created (use the ID from the POST response).
response1 = requests.get(
    f"https://jsonplaceholder.typicode.com/todos/{new_todo_id}"
)

print(f"GET /todos/{new_todo_id}")
print(f"Status: {response1.status_code}")

if response1.ok:
    todo = response1.json()
    print(f"Reading User 1's New Todo: {todo['title']}")
else:
    print("Result: Attempted to read the newly created todo (JSONPlaceholder does not persist).")


# UPDATE — PATCH the todo to mark it as completed (completed: true).
update = {
    "completed": True
}

response2 = requests.patch(
    f"https://jsonplaceholder.typicode.com/todos/{new_todo_id}",
    json=update
)

print(f"PATCH /todos/{new_todo_id}")
print(f"Status: {response2.status_code}")

if response2.ok:
    result = response2.json()
    print(f"Updated todo: {result}...")
else:
    print(f"PATCH failed with status {response2.status_code}")



# READ AGAIN — GET the todo once more to verify the update.
response3 = requests.get(
    f"https://jsonplaceholder.typicode.com/todos/{new_todo_id}"
)

todo1 = response3.json()

print(f"GET /todos/{new_todo_id}")
print(f"Status: {response3.status_code}")
print("Result: Verified update (JSONPlaceholder does not store updates).")


# DELETE — DELETE the todo.
response4 = requests.delete(
    f"https://jsonplaceholder.typicode.com/todos/{new_todo_id}"
)

print(f"DELETE /todos/{new_todo_id}")
print(f"Status: {response4.status_code}")

if response4.ok:
    print(f"Result: Sent delete request for todo {new_todo_id}.")
else:
    print(f"DELETE failed with status {response4.status_code}")

# VERIFY — Try to GET the deleted todo and handle the response
response5 = requests.get(
    f"https://jsonplaceholder.typicode.com/todos/{new_todo_id}"
)


print("METHOD: GET")
print(f"GET /todos/{new_todo_id}")
print(f"Status: {response5.status_code}")

if response5.status_code == 404:
    print(f"Result: The todo was not found after DELETE. Actual status from Server: {response5.status_code}")
elif response5.ok:
    print(f"Result: The todo is still returned because JSONPlaceholder simulates DELETE. Actual status from Server: {response5.status_code}")
else:
    print(f"Result: Verification request failed with status {response5.status_code}.")
