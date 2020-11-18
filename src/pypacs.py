import os
import pypx
import json


def verify_connectivity(server_ip, server_port):
    """

    :param server_ip. String.
    :param server_port: String.
    :return: String. Connectivity status
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
    :param query_settings: Dictionary
    :return: Dictionary.
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
    metadata = pypx.find(opt)

    return metadata


def save_metadata(metadata, save_path):
    """
    write metadata to file

    :param metadata: Dictionary.
    :param save_path: String. path to file
    :return:
    """
    dir_path = os.path.dirname(save_path)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    with open(save_path, "w") as write_file:
        json.dump(metadata, write_file, indent=4)


def move_files(server_ip, server_port, aec, aet, query_settings):
    pacs_settings = {
        'executable': '/usr/bin/movescu',
        'serverIP': str(server_ip),
        'serverPort': str(server_port),
        'aec': str(aec),
        'aet': str(aet)
    }

    opt = {**pacs_settings, **query_settings}
    output = pypx.move(opt)
    print(output)
