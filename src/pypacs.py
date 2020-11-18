import os
import pypx
import json
from collections import OrderedDict


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


def get_total_num_of_slices(metadata):
    """

    :param metadata: Dictionary
    :return: Int.
    """
    num_of_slices = 0
    studies = metadata['data']
    for study in studies:
        series = study['series']
        for s in series:
            num_of_slices = num_of_slices + int(s['NumberOfSeriesRelatedInstances']['value'])
    return num_of_slices


def create_custom_report(metadata, fields=None, custom_fields=None):
    """
    create custom report for the metadata

    :param metadata: Dictionary.
    :param fields: Dictionary. fields for different query levels (patient, study or series)
    :param custom_fields: TODO. List. a list of custom fields which do not provided by the metadata directly. might need to calculat or query separately.
    :return:
    """
    # TODO. the fields in the report are customisable providing/modifying the variable "fields"
    if fields is None:
        fields = {
            "patient": ["PatientName", "PatientID", "PatientBirthDate", "PatientAge", "PatientSex"],
            "study": ["StudyInstanceUID", "StudyDate", "ModalitiesInStudy", "StudyDescription"],
            "series": ["SeriesDate", "Modality", "SeriesDescription", "SeriesInstanceUID", "NumberOfSeriesRelatedInstances"]
        }

    report = OrderedDict()

    studies = metadata['data']
    for study in studies:
        # get patient id
        patient_id = study["PatientID"]["value"]
        if not(patient_id in report):
            report[patient_id] = OrderedDict()
            report[patient_id]["study"] = OrderedDict()

        # get study id
        study_id = study["StudyInstanceUID"]["value"]
        if not (patient_id in report[patient_id]["study"]):
            report[patient_id]["study"][study_id] = OrderedDict()

        for key in study:
            # get patient info
            if key in fields["patient"]:
                report[patient_id][key] = study[key]["value"]
            # get study info
            if key in fields["study"]:
                report[patient_id]["study"][study_id][key] = study[key]["value"]

        if "series" in study:
            report[patient_id]["study"][study_id]["series"] = OrderedDict()
            for series in study["series"]:
                # get series id
                series_id = series["SeriesInstanceUID"]["value"]
                if not (series_id in report[patient_id]["study"][study_id]["series"]):
                    report[patient_id]["study"][study_id]["series"][series_id] = OrderedDict()

                for key_in_series in series:
                    # get series info
                    if key_in_series in fields["series"]:
                        report[patient_id]["study"][study_id]["series"][series_id][key_in_series] = series[key_in_series]["value"]

    # reorder
    for patient_id in report:
        report[patient_id].move_to_end("study")

    return report