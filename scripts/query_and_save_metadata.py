import json
from src.pypacs import get_metadata, create_custom_report, save_metadata

if __name__ == '__main__':
    # TODO: get the config file of the pacs you want to access
    conf_path = "../resources/conf_dcm4chee_bioeng100.json"

    with open(conf_path) as config_file:
        cfg = json.load(config_file)
    server_ip = cfg['server_ip']
    server_port = cfg['server_port']
    aec = cfg['aec']

    # TODO. write your query here
    query_settings = {
        'PatientID': 'VL*'
    }

    # get metadata
    metadata = get_metadata(server_ip, server_port, aec, query_settings)
    report = create_custom_report(metadata)
    print(report)
    # save custom report
    save_metadata(report, "../out/custom_report.json")
    # save metadata in the default format
    # save_metadata(metadata, "../out/metadata.json")
    # save_metadata(metadata['report']['json'], "../out/report.json")

    print("DONE")