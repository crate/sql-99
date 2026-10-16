from crate.theme.rtd.conf.sql_99 import *

html_baseurl = "https://sql-99.readthedocs.io/"

# This book is not versioned. Keep in step with the "URL versioning scheme"
# setting on Read the Docs, which must be "Single version without
# translations" - nothing enforces that the two agree.
version = ""
sitemap_url_scheme = "{link}"

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
