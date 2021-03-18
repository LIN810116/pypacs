import json
from pypacs.pypacs import get_metadata, create_custom_report, save_metadata, filter_by_extra_query

if __name__ == '__main__':
    # TODO: get the config file of the pacs you want to access
    conf_path = "../resources/conf_dcm4chee_bioeng100.json"

    with open(conf_path) as config_file:
        cfg = json.load(config_file)
    server_ip = cfg.get('server_ip')
    server_port = cfg.get('server_port')
    aec = cfg.get('aec')

    # TODO. write your query here
    query_settings = {
        'PatientID': 'VL*'
    }
    # query_settings = {
    #     'PatientID': 'VL00001',
    #     'Modality': 'MR'
    # }
    # query_settings = {
    #     'PatientID': 'CL*',
    #     'Modality': 'MR',
    # }

    # get metadata
    metadata = get_metadata(server_ip, server_port, aec, query_settings)

    # # TODO. filter by extra query
    extra_query = [
        # NumberOfSeriesRelatedInstances
        {
            'tag': 'NumberOfSeriesRelatedInstances',
            'operator': '>',
            'value': 100
        }
    ]

    metadata = filter_by_extra_query(metadata, extra_query)

    report = create_custom_report(metadata)
    # print(report)
    # save custom report
    save_metadata(report, "../out/custom_report_test.json")
    # save metadata in the default format
    # save_metadata(metadata, "../out/metadata.json")
    # save_metadata(metadata['report']['json'], "../out/report.json")

    print("DONE")