from django.dispatch import Signal

api_response_cached = Signal(providing_args=['view_instance', 'view_method',
                                             'request', 'args', 'kwargs',
                                             'status', 'not_modified'])
