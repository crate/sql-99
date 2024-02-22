from crate.theme.rtd.conf.sql_99 import *

html_theme_options.update({
    "canonical_url": "https://sql-99.readthedocs.io",
})

# Disable version chooser.
html_context.update({
    "display_version": False,
    "current_version": None,
    "versions": [],
})
