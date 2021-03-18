import pydicom

if __name__ == '__main__':
    file_path = '/home/clin864/dicom_node_test/dcmqrscp_node/ACME_STORE/MR_5f322164a1a25e33.dcm'
    ds = pydicom.read_file(file_path)
    print(ds)
    patient_id = ds.PatientID
    print("patient_id: ", patient_id)
    study_instance_uid = ds.StudyInstanceUID
    print("study_instance_uid: ", study_instance_uid)
    study_id = ds.StudyID
    print("study_id: ", study_id)

    """
    PatientID: VL00035
    StudyInstanceUID: 1.3.12.2.1107.5.2.19.45016.30000013082820014020500000011
    """