import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QGroupBox, QGridLayout, QMessageBox, QComboBox

import combine


class MixerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.inputG_lineedit = QLineEdit()
        self.inputG_label = QLabel('Source for Green Channel:')
        self.inputR_button = QPushButton('Browse')
        self.inputR_lineedit = QLineEdit()
        self.inputR_label = QLabel('Source for Red Channel:')
        self.finishGroup = QGroupBox('Save')
        self.startGroup = QGroupBox('File selection')
        self.apply_button = QPushButton('Apply Mixer')
        self.format_compression = QComboBox()
        self.output_name_lineedit = QLineEdit()
        self.output_name_label = QLabel('Output Name:')
        self.output_button = QPushButton('Browse')
        self.inputG_button = QPushButton('Browse')
        self.output_label = QLabel('Output Path:')
        self.inputB_button = QPushButton('Browse')
        self.inputB_lineedit = QLineEdit()
        self.inputB_label = QLabel('Source for Blue Channel:')
        self.output_lineedit = QLineEdit()
        self.fc_format = ".jpg"
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('The Channel Mixer')
        self.setFixedSize(1000, 700)

        # Labels and LineEdits for input and output paths
        self.inputR_lineedit.setStyleSheet("QLineEdit{background: orangered;}")
        self.inputR_button.clicked.connect(self.browse_r_input)
        self.inputG_lineedit.setStyleSheet("QLineEdit{background: lime;}")
        self.inputG_button.clicked.connect(self.browse_g_input)
        self.inputB_lineedit.setStyleSheet("QLineEdit{background: royalblue;}")
        self.inputB_button.clicked.connect(self.browse_b_input)
        self.output_button.clicked.connect(self.browseoutput)
        self.format_compression.setFixedWidth(300)
        self.format_compression.addItem("Jpeg")
        self.format_compression.addItem("Tiff")
        self.format_compression.activated[str].connect(self.onselected)

        # Button to apply mixer
        self.apply_button.setFixedWidth(350)
        self.apply_button.clicked.connect(self.applymixer)

        # Start Layout setup
        start_layout = QGridLayout()
        start_layout.addWidget(self.inputR_label, 0, 0)
        start_layout.addWidget(self.inputR_lineedit, 0, 1)
        start_layout.addWidget(self.inputR_button, 0, 2)
        start_layout.addWidget(self.inputG_label, 1, 0)
        start_layout.addWidget(self.inputG_lineedit, 1, 1)
        start_layout.addWidget(self.inputG_button, 1, 2)
        start_layout.addWidget(self.inputB_label, 2, 0)
        start_layout.addWidget(self.inputB_lineedit, 2, 1)
        start_layout.addWidget(self.inputB_button, 2, 2)
        self.startGroup.setLayout(start_layout)

        # finish layout setup
        finish_layout = QGridLayout()
        finish_layout.addWidget(self.output_label, 0, 0)
        finish_layout.addWidget(self.output_lineedit, 0, 1)
        finish_layout.addWidget(self.output_button, 0, 2)
        finish_layout.addWidget(self.output_name_label, 1, 0)
        finish_layout.addWidget(self.output_name_lineedit, 1, 1)
        finish_layout.addWidget(self.format_compression, 2, 1)
        finish_layout.addWidget(self.apply_button, 3, 2)
        self.finishGroup.setLayout(finish_layout)

        # final layout
        grid = QGridLayout()
        grid.addWidget(self.startGroup, 0, 0)
        grid.addWidget(self.finishGroup, 1, 0)
        self.setLayout(grid)
        self.show()

    def browse_r_input(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select Image")
        if filename:
            self.inputR_lineedit.setText(filename)

    def browse_g_input(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select Image")
        if filename:
            self.inputG_lineedit.setText(filename)

    def browse_b_input(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select Image")
        if filename:
            self.inputB_lineedit.setText(filename)

    def browseoutput(self):
        foldername = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if foldername:
            self.output_lineedit.setText(foldername)

    def onselected(self, textval):
        # here we can create presets for the app
        # these options have to be also in the mode_combo
        if textval == "Jpeg":
            self.fc_format = ".jpg"
        if textval == "Tiff":
            self.fc_format = ".tif"

    def show_success_message(self, output_path):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setFixedSize(300, 300)
        msg.setText("File saved successfully")
        msg.setInformativeText(f"The file was saved as {output_path}")
        msg.setWindowTitle("Success")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.move(self.geometry().center() - msg.rect().center())
        msg.exec_()

    def applymixer(self):
        input_r_path = self.inputR_lineedit.text()
        input_g_path = self.inputG_lineedit.text()
        input_b_path = self.inputB_lineedit.text()
        output_path = self.output_lineedit.text() + "/" + self.output_name_lineedit.text()
        out = combine.combine_image_channels(
            red=input_r_path,
            green=input_g_path,
            blue=input_b_path
        )
        out.save(f"{output_path}{self.fc_format}")  # Save as defined by ComboBox
        self.show_success_message(output_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MixerApp()
    sys.exit(app.exec_())
