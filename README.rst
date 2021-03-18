======
pypacs
======

Prerequisites
=============

Install system packages
-----------------------

::

    sudo apt-get update
    sudo apt-get install -y dcmtk

Install Python dependencies
---------------------------

Installing python dependencies using a virtual environment is recommended.

::

    # create a virtual environment
    python3 -m venv venv/
    # activate the virtual environment
    source venv/bin/activate
    # install the dependencies via pip
    pip install -r requirements.txt

Main functions
==============

- ``verify_connectivity``: verify dicom node/AE connectivity. see *pypacs/scripts/check_connectivity.py* for usage example.
- ``get_metadata``: get metadata. see *pypacs/scripts/query_and_save.py* for usage example.
- ``move_files``: send copies of dicom files to another PACS. see *pypacs/scripts/copy_and_send.py* for usage example.

Usage Examples
==============

See the *examples/* folder for usage examples.

Make sure the PACS system you want to interact with is running before running the examples.
To start DCM4CHEE on bioeng100, see `Starting DCM4CHEE on bioeng100`_.

Note that if you want to download the files from the PACS on bioeng100 to a receiver node (e.g. on local machine),
You need to add the receiver node/pacs to the node list in the PACS on bioeng100. See the header comment in download.py for more details.

Starting DCM4CHEE on bioeng100
------------------------------

1. Connect to UOA network/VPN
2. Log into bioeng100. ``ssh breast@bioeng100``
3. Start DCM4CHEE. ``sh /home/breast/pacs/bin/run.sh``
4. The DCM4CHEE web interface will then be accessible via URL http://bioeng100.bioeng.auckland.ac.nz:8080/dcm4chee-web/
