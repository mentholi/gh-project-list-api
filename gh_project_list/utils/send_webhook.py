import dramatiq
import json
import requests
from webhooks.models import Webhook


@dramatiq.actor
def send_webhook(url, payload):
    """
    Send a webhook to given url
    """
    response = requests.post(url, json=payload, headers={
        "Content-Type": "application/json"
    })
    print("Received {status} from url {url}".format(
        status=response.status_code,
        url=url
    ))

@dramatiq.actor
def send_webhooks(instance_id):
    """
    Serializes created project entry and schedules
    tasks to send webhooks for each configured url
    """
    from projects.models import Project  # noqa
    from projects.serializers import ProjectSerializer  # noqa

    project = Project.objects.get(id=instance_id)
    payload = ProjectSerializer(instance=project).data
    webhooks = Webhook.objects.all()
    for webhook in webhooks:
        send_webhook.send(webhook.url, json.dumps(payload))

