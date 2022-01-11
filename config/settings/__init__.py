from .base import *
import os


if os.environ.get("ENVIRONMENT") == 'Production':
    from .production import *
else:
    from .development import *
