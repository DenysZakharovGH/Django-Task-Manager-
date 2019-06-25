#!D:\Education\Django\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'NSoL==0.1.12','console_scripts','nsol_run_deconvolution_study'
__requires__ = 'NSoL==0.1.12'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('NSoL==0.1.12', 'console_scripts', 'nsol_run_deconvolution_study')()
    )
