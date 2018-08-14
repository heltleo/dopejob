from celery import shared_task

@shared_task
def debug():
	print("testing celery...")
