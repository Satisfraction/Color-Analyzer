# Import necessary modules
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
from PIL import Image, ImageQt
from PyQt5 import QtCore

# Create a class for our ColorAnalyzer widget
class ColorAnalyzer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # Define the user interface
    def initUI(self):
        # Create a label
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("<font color='blue'>Select an image:</font>")
        self.label1.move(20, 20)

        # Create a button
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Open File")
        self.button.move(20, 60)
        self.button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.button.clicked.connect(self.get_file)
        
        # Create a save button
        self.save_button = QtWidgets.QPushButton(self)
        self.save_button.setText('Save Color')
        self.save_button.move(100, 100)
        self.save_button.setStyleSheet('background-color: #4CAF50; color: white;')
        self.save_button.clicked.connect(self.save_color)

        # Create an entry box
        self.entry = QtWidgets.QLineEdit(self)
        self.entry.move(130, 60)

        # Create an analyze button
        self.analyze_button = QtWidgets.QPushButton(self)
        self.analyze_button.setText("Analyze color")
        self.analyze_button.move(20, 100)
        self.analyze_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.analyze_button.clicked.connect(self.get_color)

        # Create a label to display the average color
        self.color_label = QtWidgets.QLabel(self)
        self.color_label.setGeometry(20, 140, 400, 50)
        self.color_label.setStyleSheet("background-color: #E91E63; color: white;")

        # Create a label to display the image
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(20, 200, 360, 360)
        self.label.setStyleSheet("background-color: white;")

        # Set the window size and title
        self.setGeometry(100, 100, 400, 600)
        self.setWindowTitle('Color Analyzer')

        # Set the background color of the window
        self.setStyleSheet("background-color: #F5F5F5;")

        # Show the widget
        self.show()

    # Define a function to get the file path of the selected image
    def get_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image File")
        if file_path:
            self.entry.clear()
            self.entry.insert(file_path)
            self.get_color()

    # Define a function to analyze the color of the selected image
    def get_color(self):
        image_path = self.entry.text()
        color = self.analyze_color(image_path)
        color_hex = '#{0:02x}{1:02x}{2:02x}'.format(*color)
        self.color_label.setText('Average color: ' + color_hex)
        self.show_image(image_path)

    # Define a function to analyze the color of an image
    def analyze_color(self, image_path):
        with Image.open(image_path) as img:
            colors = img.getcolors(img.size[0] * img.size[1])
            average_color = tuple(sum([c[0] * c[1][i] for c in colors for i in range(3)]) // sum([c[0] for c in colors]) for j in range(3))
            return average_color

    # Define a function to display the selected image
    def show_image(self, image_path):
        with Image.open(image_path) as img:
            img.thumbnail((600, 600))
            qimage = ImageQt.ImageQt(img)
            pixmap = QtGui.QPixmap.fromImage(qimage)
            pixmap = pixmap.scaled(self.label.size() * 0.9, QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(pixmap)
            
    def save_color(self):
        color_hex = self.color_label.text().split(': ')[-1]
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Color File', '', 'Text Files (*.txt)')
        if file_path:
            with open(file_path, 'w') as f:
                f.write(color_hex)
            
# If this file is being run directly,
if __name__ == '__main__':
    # Create a new Qt application
    app = QtWidgets.QApplication(sys.argv)

    # Create an instance of the ColorAnalyzer widget
    ex = ColorAnalyzer()

    # Execute the application
    sys.exit(app.exec_())