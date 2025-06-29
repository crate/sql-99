from crate.theme.rtd.conf.sql_99 import *

html_baseurl = "https://sql-99.readthedocs.io/"

# Disable version chooser.
html_context.update({
    "display_version": False,
    "current_version": None,
    "versions": [],
})

linkcheck_ignore = [
    r"https://www.mysql.com/",
    r"http://www.hughes.com.au/*",
]
