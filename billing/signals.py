from django.dispatch import Signal

transaction_started = Signal()

transaction_was_successful = Signal(providing_args=["type", "response"])
transaction_was_unsuccessful = Signal(providing_args=["type", "response"])

amazon_fps_payment_signal = Signal(providing_args=["request", "integration"])
