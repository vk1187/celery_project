import logging
from tasks import add  # Import the add task from tasks.py

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        # Start the Celery task
        logger.info("Starting the Celery task")
        result = add.apply_async((5, 10))  # Call the task with arguments (5, 10)
        
        # Wait for the result with a timeout of 30 seconds
        logger.info(f'Task result: {result.get(timeout=30)}')
    
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
