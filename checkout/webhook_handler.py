from django.http import HttpResponse


class stripe_handler:
    """ Handle Stripe webhooks """
    
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ 
        handles a generic / unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200
        )