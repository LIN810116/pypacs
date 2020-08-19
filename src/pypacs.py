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
    pacs_settings = {
        'executable': '/usr/bin/echoscu',
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
    # TODO: choose a pacs system you want to interact with

    # dcm4chee (old pacs) on bioeng100
    server_ip = 'bioeng100.bioeng.auckland.ac.nz'
    server_port = '11112'
    aec = 'DCM4CHEE'
    aet = 'TEST'

    # orthanc on bn363773 (130.216.209.202). needs to log in to bn363773 first.
    # server_ip = '130.216.209.202'
    # server_port = '4242'
    # aec = 'ORTHANC'

    # dcmtk node on eresearch
    # server_ip = '130.216.209.202'
    # server_port = '8110'
    # aec = 'TEST'
    # aet = 'ACM1'

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