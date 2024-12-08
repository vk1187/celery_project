from celery_config import make_celery

# Create Celery app instance
app = make_celery()

@app.task  # Ensure this decorator is applied to the function
def add(x, y):
    print("tasks.py has been loaded!")  # This will print if tasks.py is loaded

    # Simple add task
    return x + y
