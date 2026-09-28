from crate.theme.rtd.conf.sql_99 import *

# NOTE: `html_baseurl` used to be pinned to https://sql-99.readthedocs.io/ here.
# It now comes from `crate.theme.rtd.conf.sql_99`, which derives it from the
# Read the Docs environment for the docs.cratedb.com migration PoC.

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
