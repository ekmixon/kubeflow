"""
Common helper functions for handling k8s objects information
"""
import datetime as dt
import logging
import os
import re

import yaml
from flask import current_app

log = logging.getLogger(__name__)


def get_prefixed_index_html():
    """
    The backend should modify the <base> element of the index.html file to
    align with the configured prefix the backend is listening
    """
    prefix = os.path.join("/", current_app.config["PREFIX"], "")
    static_dir = current_app.config["STATIC_DIR"]

    log.info("Setting the <base> to reflect the prefix: %s", prefix)
    with open(os.path.join(static_dir, "index.html"), "r") as f:
        index_html = f.read()
        return re.sub(
            r"\<base href=\".*\".*\>",
            '<base href="%s">' % prefix,
            index_html,
        )


def load_yaml(f):
    """
    f: file path
    Load a yaml file and convert it to a python dict.
    """
    c = None
    try:
        with open(f, "r") as yaml_file:
            c = yaml_file.read()
    except IOError:
        log.error("Error opening: %s", f)
        return None

    try:
        contents = yaml.safe_load(c)
        return {} if contents is None else contents
    except yaml.YAMLError:
        return None


def load_param_yaml(f, **kwargs):
    """
    f: file path

    Load a yaml file and convert it to a python dict. The yaml might have some
    `{var}` values which the user will have to format. For this we first read
    the yaml file and replace these variables and then convert the generated
    string to a dict via the yaml module.
    """
    c = None
    try:
        with open(f, "r") as yaml_file:
            c = yaml_file.read().format(**kwargs)
    except IOError:
        log.error("Error opening: %s", f)
        return None

    try:
        contents = yaml.safe_load(c)
        return {} if contents is None else contents
    except yaml.YAMLError:
        return None


def get_uptime(then):
    """
    then: datetime instance | string

    Return a string that informs how much time has pasted from the provided
    timestamp.
    """
    if isinstance(then, str):
        then = dt.datetime.strptime(then, "%Y-%m-%dT%H:%M:%SZ")

    now = dt.datetime.now()
    diff = now - then.replace(tzinfo=None)

    days = diff.days
    age = ""
    if days > 0:
        age = f"{str(days)} day" if days == 1 else f"{str(days)} days"
    else:
        hours = int(diff.seconds / 3600)
        if hours > 0:
            age = f"{hours} hour" if hours == 1 else f"{hours} hours"
        else:
            mins = int((diff.seconds % 3600) / 60)

            if mins == 0:
                return "just now"
            age = f"{mins} min" if mins == 1 else f"{mins} mins"
    return f"{age} ago"
