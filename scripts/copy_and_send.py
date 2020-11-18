import json
from src.pypacs import move_files

if __name__ == '__main__':
    # TODO. get the config file of the pacs you want to access
    conf_path = "../resources/conf_dcm4chee_bioeng100.json"

    with open(conf_path) as config_file:
        cfg = json.load(config_file)
    server_ip = cfg['server_ip']
    server_port = cfg['server_port']
    aec = cfg['aec']
    aet = cfg['aet']

    # Retrieve data from the pacs of your choose (sender) and send to another pacs (receiver).
    # The receiver pacs needs to be configured appropriately in the sender pacs in the AE management page/configuration file.
    # Also. make sure both the sender and receiver are running before sending files.
    # TODO. write your query here.
    # Currently, you have to provide StudyInstanceUID and SeriesInstanceUID.
    # Future improvement: allow user to send data from patient, study, series or image level.
    query_settings = {
        'StudyInstanceUID': '1.3.12.2.1107.5.2.30.25138.30000006060820152293700000008',
        'SeriesInstanceUID': '1.3.12.2.1107.5.2.30.25138.30000006060820125681200002569'
    }

    move_files(server_ip=server_ip, server_port=server_port, aec=aec, aet=aet, query_settings=query_settings)

    print("DONE")

