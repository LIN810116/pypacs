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
See the main function in *src/pypacs.py* for a complete usage example.
Note that you might need to connect to UOA network before running the script.

* Verify dicom node/AE connectivity: use the **verify_connectivity** function in *src/pypacs.py*.
* Get metadata: use the **get_metadata** function in *src/pypacs.py*.
* Send copies of dicom files to another pacs: use the **move_files** function in *src/pypacs.py*.

