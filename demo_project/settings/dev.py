"""
    Development Django settings for dockerdemo-django project
    =========================================================

    This files imports the `base` settings and can add or modify previously defined settings to
    alter the configuration of the application for development purposes.

    For more information on this file, see https://docs.djangoproject.com/en/dev/topics/settings/
    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/dev/ref/settings/
"""

from .base import *  # noqa


# DEBUG CONFIGURATION
# ------------------------------------------------------------------------------

DEBUG = True
