#!C:\Users\ht_3234\PycharmProjects\Twint\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'elasticsearch-helper==0.1.2','console_scripts','es_stream'
__requires__ = 'elasticsearch-helper==0.1.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('elasticsearch-helper==0.1.2', 'console_scripts', 'es_stream')()
    )
