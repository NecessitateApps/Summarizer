#!C:\Users\Bisher\Desktop\Projects\Summarizer\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'urlextract==0.8.3','console_scripts','urlextract'
__requires__ = 'urlextract==0.8.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('urlextract==0.8.3', 'console_scripts', 'urlextract')()
    )
