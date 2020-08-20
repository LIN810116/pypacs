import pypx
import json


def verify_connectivity(server_ip, server_port):
    """

    :param server_port: String
    :return: String
    """
    pacs_settings = {
        'executable': '/usr/bin/echoscu',
         'serverIP': str(server_ip),
         'serverPort': str(server_port)
    }
    output = pypx.echo(pacs_settings)
    print(output)
    return output['status']


def get_metadata(server_ip, server_port, aec, query_settings):
    """
    get metadata beased on query settings
    :param server_ip: Strings
    :param server_port: Strings
    :param aec: Strings
    :param query_settings: JSON
    :return:
    """
    pacs_settings = {
        'executable': '/usr/bin/findscu',
        'serverIP': str(server_ip),
        'serverPort': str(server_port),
        'aec': aec
    }

    output_settings = {
        'printReport': 'json',
        'colorize': 'dark'
    }

    opt = {**pacs_settings, **query_settings, **output_settings}
    output = pypx.find(opt)
    print(output['report']['json'])
    return output['report']['json']


def save_metadata(metadata, path):
    with open(path, "w") as write_file:
        json.dump(metadata, write_file)

def move_files(server_ip, server_port, aec, aet, study_instance_uid, series_instance_uid):
    pacs_settings = {
        'executable': '/usr/bin/movescu',
        'serverIP': '130.216.209.202',
        'serverPort': '8106',
        'aec': 'ACME_STORE',
        'aet': 'ACM1'
    }

    query_settings = {
        'StudyInstanceUID': study_instance_uid,
        'SeriesInstanceUID': series_instance_uid
    }
    opt = {**pacs_settings, **query_settings}
    output = pypx.move(opt)
    print(output)


if __name__ == '__main__':
    # TODO: choose a pacs system you want to interact with.

    # dcm4chee (old pacs) on bioeng100
    conf_path = "../resources/conf_dcm4chee_bioeng100.json"

    # orthanc on bn363773 (130.216.209.202). needs to log in to bn363773 first.
    # TODO. note that this one is not working at the moment.
    #  perhaps can try pyorthanc package instead of pypx,
    #  or need to modify orthanc's configuration.
    # conf_path = "../resources/conf_orthanc_bn363773.json"

    # dcmtk node on eresearch
    # conf_path = "../resources/conf_dcmtk_bn363773.json"

    with open(conf_path) as config_file:
        cfg = json.load(config_file)
    server_ip = cfg['server_ip']
    server_port = cfg['server_port']
    aec = cfg['aec']
    aet = cfg['aet']

    # check connectivity
    status = verify_connectivity(server_ip, server_port)
    print("Connectivity status: ", status)

    # query & get metadata
    query_settings = {
        'PatientID': 'VL00001'
    }
    metadata = get_metadata(server_ip, server_port, aec, query_settings)
    save_metadata(metadata, "metadata.json")


    # retrieve data and send to another pacs/AE title which has been added to the pacs of your choose
    # The pacs you want to communicate needs to be configured appropriately.
    # move_files(server_ip, server_port, aec, aet,
    #            study_instance_uid='1.3.12.2.1107.5.2.19.45016.30000013082820014020500000011',
    #            series_instance_uid='1.3.12.2.1107.5.2.19.45016.2013082914471598331448277.0.0.0')