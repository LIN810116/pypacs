"""
Retrieve data from the pacs of your choose (sender) and send to another pacs (receiver).
The receiver pacs needs to be configured properly in the sender pacs on the AE management page/configuration file.

Also. make sure both the sender and receiver nodes are running before sending files.
Below are the steps to set up a receiver node using storescp:
    Prerequisites: you need have dcmtk package installed:
        - sudo apt-get update
        - sudo apt-get install -y dcmtk
    1. Create a folder
    2. Open a terminal from the folder
    3. Run:
        sudo storescp -v <portNumber> -tos 3 -dhl -ss dcm -tn
"""

import json
from src.pypacs import move_files

if __name__ == '__main__':
    # TODO. get the config file of the pacs you want to access
    conf_path = "../resources/conf_dcm4chee_bioeng100.json"

    with open(conf_path) as config_file:
        cfg = json.load(config_file)
    server_ip = cfg.get('server_ip')
    server_port = cfg.get('server_port')
    aec = cfg.get('aec')
    aet = cfg.get('aet')

    # Currently, you have to provide StudyInstanceUID and SeriesInstanceUID.
    # Future improvement: allow user to send data from patient, study, series or image levels.
    # TODO. write your query here.
    query_settings = {
        'StudyInstanceUID': '1.3.12.2.1107.5.2.30.25138.30000006060122155281200000007',
        'SeriesInstanceUID': '1.3.12.2.1107.5.2.30.25138.30000006060120104693700002235'
    }

    move_files(server_ip=server_ip, server_port=server_port, aec=aec, aet=aet, query_settings=query_settings)

    print("DONE")

