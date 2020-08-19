PACS Overview
=============
PACS stands for Picture Archiving and Communication System.

Some open source pacs projects
------------------------------
* `DCMTK`_
* `dcm4che`_

DCMTK
-----
DCMTK_ stands for Digital Imaging and Communications in Medicine ToolKit, which is a lightweight PACS.
It is a collection of libraries and services following the DICOM standard for medical image communication.

* storescp

  The storescp service implements a Service Class Provider (SCP) for the storing dicom files.
  see storescp_.
  ::

      # Usage
      1. go to the folder which you want to set as a dicom node.
      2. open terminal
      3. sudo storescp -v PortNumber -aet AETitle

* storescu

  The storescu service implements a Service Class User (SCU) for sending dicom files to a service provider (dicom node).
  see storescu_.
  ::

      # Usage
      1. go to the study folder.
      2. open terminal
      3. sudo storescu -v ProviderIP PortNumber -aet AETitle --scan-directories StudyFolder
      # --scan-directories is for sending all the files in a directory (usually a study)
      # for sending a single dicom file, remove --scan-directories and replace StudyFolder with the filename.

* dcmqrscp

  The dcmqrscp service is an Image Central Test Node which provides store, query and retrieve services.
  Unlike storescp which only provide storage service. see dcmqrscp_.

  - Setting up a dcmqrscp service
    ::

        1. create a config file or use the example config file in `/resources/dcmqrscp_conf`
        2. open terminal
        3. sudo dcmqrscp -d -c /pathToConfFile

  - Sending a study to a dcmqrscp storage
    ::

        1. go to the study folder
        2. open terminal
        3. sudo storescu -v IP Port -aec myAEC -aet myAET --scan-directories StudyFolder
        # note: check your config file for the names of aec & aet

dcm4che
-------
dcm4che_ is a collection of services which provide image archiving and management.

* dcm4chee-web3

.. _DCMTK: https://support.dcmtk.org/docs/index.html
.. _storescp: https://support.dcmtk.org/docs/storescp.html
.. _storescu: https://support.dcmtk.org/docs/storescu.html
.. _dcmqrscp: https://support.dcmtk.org/docs/dcmqrscp.html
.. _dcm4che: https://www.dcm4che.org/
