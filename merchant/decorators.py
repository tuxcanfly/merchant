from merchant.conf import signal_handlers

def raise_signal(func):
    def inner_func(*args, **kwargs):
        response  = func(*args, **kwargs)
        status = response['status']
        if status in signal_handlers:
            signal_handlers[status](*args, **kwargs)
        return response
    return inner_func
