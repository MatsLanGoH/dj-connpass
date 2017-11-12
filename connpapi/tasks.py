from celery.decorators import task
from celery.utils.log import get_task_logger

from .queries import event_proc

logger = get_task_logger(__name__)


@task(name="get_events_data")
def get_events_data_task():
    logger.info("Requesting API data")
    results = event_proc()
    return results
