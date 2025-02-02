from vjyscan.cores import http_session
from vjyscan.modules.fingerprints.joomla import version_parser
from vjyscan.resources import joomla
from vjyscan.cores.version_cmp import *
import json

db_path = joomla.__path__[0] + "core.jdb" if joomla.__path__[0].endswith("/") else joomla.__path__[0] + "/core.jdb"


session = http_session.VJScan(verbose=False, ua="Mozilla/5.0", cookie="", proxy="")

target_url = "https://ktht.nuce.edu.vn/"

session.print_verbose(f"Checking {target_url}")
version = version_parser.check_xml(session, target_url)

for line in open(db_path):
    vuln_info = json.loads(line)
    if joomla_cmp("3.3.22", vuln_info["version"]):
        session.print_vulnerable(f"{vuln_info['CVE']} {vuln_info['name']}")
