# Example Celery task
from celery import shared_task

@shared_task
def send_welcome_email(user_id):
    # Implement email sending logic here
    print(f"Send welcome email to user {user_id}")
    return True
