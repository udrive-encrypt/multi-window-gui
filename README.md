# multi-window-gui

GUI to encrypt USB drive
An easy-to-use gui for encryption of USB drives using Python (PyQt5) for GUI and LUKS for encryption. Users will be provided a list of connected USB drives and will have to select the one to be encrypted. Further they will have to add password. In case, the drive is already encrypted, users will be able to add new passwords (max 8) or delete passwords.

Prerequisites
Any system having Linux based operating system can use this application.

Installing
Installing PyQt5

    pip3 install PyQt5
    If the above command does not run successfully, you can make a directory and create virtual environment.

        mkdir demo
        cd demo
        python -m venv v1
        source v1/bin/activate
        pip3 install PyQt5 


Built With
PyQt5 - Python binding of the cross-platform GUI toolkit Qt. It is implemented as a Python plug-in.
PyCharm - Integrated Development Environment, specially used for Python.

Authors

    Akshata Jadhav
    Gajanan More
    Anuja Kulkarni
    Amruta Salunkhe


License
This project is licensed under the GNU General Public License - see the LICENSE file for details
