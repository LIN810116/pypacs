import json

import pypacs

if __name__ == '__main__':
    # TODO: choose a PACS system you want to interact with.
    # make sure the pacs is running before executing the script

    # PACS 1: dcm4chee (old pacs) on bioeng100
    conf_path = "../resources/conf_dcm4chee_bioeng100.json"

    # PACS 2: orthanc on bn363773 (130.216.209.202).
    # Note that this one is not working at the moment.
    # perhaps can try pyorthanc package instead of pypx,
    # or need to modify orthanc's configuration.
    # conf_path = "../resources/conf_orthanc_bn363773.json"

    with open(conf_path) as config_file:
        cfg = json.load(config_file)
    server_ip = cfg.get('server_ip')
    server_port = cfg.get('server_port')

    # check connectivity
    status = pypacs.verify_connectivity(server_ip, server_port)
    print("Connectivity status: ", status)

    print("DONE")