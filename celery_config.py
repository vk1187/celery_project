from celery import Celery

def make_celery():
    """Factory function to create Celery app."""
    app = Celery('my_celery_project', broker='redis://localhost:6379/0')
    app.conf.update(
        result_backend='redis://localhost:6379/1',  # Using Redis as result backend
        result_expires=3600,  # Results expire after 1 hour
        broker_connection_retry_on_startup=True,  # Retry broker connection on startup
    )
    
    # Explicitly import the tasks module to ensure tasks are loaded
    app.config_from_object('celery_config')

    return app

# Initialize and export the Celery app
app = make_celery()

# Import tasks explicitly to ensure Celery knows about them
import tasks
