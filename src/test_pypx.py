import pypx
import json

def test_pxecho():
    # py-echo: a wrapper of echoscu
    # can be used to verify DICOM connectivity
    pacs_settings = {
        'executable': '/usr/bin/echoscu',
        'serverIP': '130.216.209.202',
        'serverPort': '8106'
    }

    output = pypx.echo(pacs_settings)
    print(output)


def test_pxfind():
    pacs_settings = {
        'executable': '/usr/bin/echoscu',
        'aec': 'ACME_STORE',
        'serverIP': '130.216.209.202',
        'serverPort': '8106'
    }

    query_settings = {
        'PatientID': 'VL00035'
    }

    output_settings = {
        'printReport': 'json',
        'colorize': 'dark'
    }

    opt = {**pacs_settings, **query_settings, **output_settings}
    output = pypx.find(opt)
    print(output['report']['json'])

    with open("metadata.json", "w") as write_file:
        json.dump(output['report']['json'], write_file)


def test_pxmove():
    pacs_settings = {
        'executable': '/usr/bin/movescu',
        'aec': 'ACME_STORE',
        'aet': 'ACM1',
        'serverIP': '130.216.209.202',
        'serverPort': '8106'
    }

    query_settings = {
        'StudyInstanceUID': '1.3.12.2.1107.5.2.19.45016.30000013082820014020500000011',
        'SeriesInstanceUID': '1.3.12.2.1107.5.2.19.45016.2013082914471598331448277.0.0.0'
    }
    opt = {**pacs_settings, **query_settings}
    output = pypx.move(opt)
    print(output)


if __name__ == '__main__':
    # test_pxecho()
    test_pxfind()
    # test_pxmove()
