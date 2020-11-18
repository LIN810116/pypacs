pypacs
======

Install the dependencies
------------------------
::

    # install system packages
    sudo apt-get update
    sudo apt-get install -y dcmtk

    # install python packages
    pip install --upgrade pip
    pip install -r requirements.txt

Usage
-----
See the *pypacs/scripts* folder for usage examples.
Note that you might need to connect to UOA network
and make sure the PACS system you want to interact with is running
before executing the scripts.
To start DCM4CHEE on bioeng100, see `Starting DCM4CHEE on bioeng100`_.

Main functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- ``verify_connectivity``: verify dicom node/AE connectivity. see *pypacs/scripts/check_connectivity.py* for usage example.
- ``get_metadata``: get metadata. see *pypacs/scripts/query_and_save.py* for usage example.
- ``move_files``: send copies of dicom files to another PACS. see *pypacs/scripts/copy_and_send.py* for usage example.

Starting DCM4CHEE on bioeng100
------------------------------
1. Log into bioeng100. ``ssh breast@bioeng100``
2. Stat DCM4CHEE. ``sh /home/breast/pacs/bin/run.sh``
3. The DCM4CHEE web interface will then be accessible via URL http://bioeng100.bioeng.auckland.ac.nz:8080/dcm4chee-web/
