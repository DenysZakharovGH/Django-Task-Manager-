#!D:\Education\Django\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'SimpleReg==0.3.1','console_scripts','simplereg_resample'
__requires__ = 'SimpleReg==0.3.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('SimpleReg==0.3.1', 'console_scripts', 'simplereg_resample')()
    )
