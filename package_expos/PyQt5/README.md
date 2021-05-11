# PyQt5 Tutorial

### About
PyQt5 is a python package developed from the QT C++ framework that allows users to generate interactive GUIs in Python. 

Use cases include any need to develop a point and click application. Examples include but are not limited to receiving text information from a user, developing a controller for an audio interface, or building aesthetically appealing controls for a data visualization tool.

### QT Website
https://www.qt.io

### Package Expo Tutorial Video
https://youtu.be/Pz4vPZIlZhQ

#### About the tutorial
The tutorial first walks through the installation instructions for PyQt5 and then goes through the import process for widgets. The required widgets are imported and then there are 2 example codes. The first is a simple code-along demonstration which outlines the basics of the package. This shows how to build a basic window with a button using the QPushButton widget.
The second example is a bit more involved and shows PyQt5 being used in a more object oriented program approach with objects and classes. Ultimately, this second example will result in a dynamic button that changes the text in the window when clicked.

### Software
Python 3 or higher is required.

### Install the required package with
!pip install PyQt5

### Import widgets from PyQt5
After installing PyQt5 using the pip installer, you will need to import QtWidgets in order to import various widgets that can be used in your GUI. A list of some of the widgets available in PyQt5 followed by their descriptions are outlined below.
    
### Widget Guide
QApplication: a class that manages the GUI application's control flow and main settings
QWidget: the base class of all user interface objects
QPushButton: A simple button
QVBoxLayout: lines up widgets vertically
QMainWindow: procides a main application window
QLabel: generates a non-interactive label
QComboBox: creates a dropdown list box
QCheckbox: creates a check box
QDial: creates a rotateable dial

### Conclusion
I hope this document and tutorial provide you with enough information to start building GUIs in PyQt5.
Thanks!




### Sources
https://build-system.fman.io/pyqt5-tutorial
https://www.youtube.com/watch?v=-2uyzAqefyE&list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj&index=2
https://www.educative.io/edpresso/what-is-pyqt
https://www.mfitzp.com/tutorials/basic-widgets/