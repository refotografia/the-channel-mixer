import combine
import numpy as np
from PIL import Image
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QFileDialog
import sys

class MixerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Mixer App')

        # Labels and LineEdits for input and output paths
        self.inputR_label = QLabel('Source for Red Channel:')
        self.inputR_lineedit = QLineEdit()
        self.inputR_button = QPushButton('Browse')
        self.inputR_button.clicked.connect(self.browseinput)

        self.inputG_label = QLabel('Source for Green Channel:')
        self.inputG_lineedit = QLineEdit()
        self.inputG_button = QPushButton('Browse')
        self.inputG_button.clicked.connect(self.browseinput)

        self.inputB_label = QLabel('Source for Blue Channel:')
        self.inputB_lineedit = QLineEdit()
        self.inputB_button = QPushButton('Browse')
        self.inputB_button.clicked.connect(self.browseinput)

        self.output_label = QLabel('Output Path:')
        self.output_lineedit = QLineEdit()
        self.output_button = QPushButton('Browse')
        self.output_button.clicked.connect(self.browseoutput)

        self.output_name_label = QLabel('Output Name:')
        self.output_name_lineedit = QLineEdit()

        # Button to apply mixer
        self.apply_button = QPushButton('Apply Mixer')
        self.apply_button.clicked.connect(self.applymixer)

        # Layout setup
        vbox = QVBoxLayout()
        vbox.addWidget(self.inputR_label)
        hboxR_input = QHBoxLayout()
        hboxR_input.addWidget(self.inputR_lineedit)
        hboxR_input.addWidget(self.inputR_button)
        vbox.addLayout(hboxR_input)

        vbox.addWidget(self.inputG_label)
        hboxG_input = QHBoxLayout()
        hboxG_input.addWidget(self.inputG_lineedit)
        hboxG_input.addWidget(self.inputG_button)
        vbox.addLayout(hboxG_input)

        vbox.addWidget(self.inputB_label)
        hboxB_input = QHBoxLayout()
        hboxB_input.addWidget(self.inputB_lineedit)
        hboxB_input.addWidget(self.inputB_button)
        vbox.addLayout(hboxB_input)

        vbox.addWidget(self.output_label)
        hbox_output = QHBoxLayout()
        hbox_output.addWidget(self.output_lineedit)
        hbox_output.addWidget(self.output_button)
        vbox.addLayout(hbox_output)

        vbox.addWidget(self.output_name_label)
        vbox.addWidget(self.output_name_lineedit)

        vbox.addWidget(self.apply_button)

        self.setLayout(vbox)
        self.show()

    def browseinput(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select Image")
        if filename:
            self.input_lineedit.setText(filename)

    def browseoutput(self):
        foldername = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if foldername:
            self.output_lineedit.setText(foldername)

    def applymixer(self):
        inputR_path = self.inputR_lineedit.text()
        inputG_path = self.inputG_lineedit.text()
        inputB_path = self.inputB_lineedit.text()
        inputR = np.asarray(inputR_path)
        inputG = np.asarray(inputG_path)
        inputB = np.asarray(inputB_path)
        output_path = self.output_lineedit.text() + "/" + self.output_name_lineedit.text() + ".jpg"
        combined_image = combine.combine_image_channels(image1=inputR, image2=inputG, image3=inputB)
        new_image = Image.fromarray(combined_image)  # Convert NumPy array to PIL image
        new_image.save(output_path)  # Save as JPEG


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MixerApp()
    sys.exit(app.exec_())