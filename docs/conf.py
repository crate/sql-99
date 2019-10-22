from crate.theme.rtd.conf.sql_99 import *

# crate.theme sets html_favicon to favicon.png which causes a warning because
# it should be a .ico and in addition there is no favicon.png in this project
# so it can't find the file
html_favicon = None

source_suffix = '.rst'

exclude_patterns = ['.*', '*.lint']

master_doc = 'index'

site_url = 'https://crate.io/docs/sql-99/en/latest/'

extensions = ['sphinx_sitemap']

