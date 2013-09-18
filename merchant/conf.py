import os

from importlib import import_module

from merchant.exceptions import GatewayNotConfigured


settings_module = os.getenv("MERCHANT_SETTINGS")
if not settings_module:
    raise GatewayNotConfigured
try:
    module = import_module(settings_module)
    settings = module.MERCHANT_SETTINGS
    signal_handlers = module.SIGNAL_HANDLERS
except AttributeError:
    raise GatewayNotConfigured
