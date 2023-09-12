from crate.theme.rtd.conf.sql_99 import *

# Disable version chooser.
html_context.update({
    "display_version": False,
    "current_version": None,
    "versions": [],
})
