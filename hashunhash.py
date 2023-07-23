import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

from cryptography.fernet import Fernet

class EncryptionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

        layout = QVBoxLayout()

        self.original_data_label = QLabel("Enter the data to encrypt:")
        layout.addWidget(self.original_data_label)

        self.original_data_input = QLineEdit()
        layout.addWidget(self.original_data_input)

        self.encrypt_button = QPushButton("Encrypt")
        self.encrypt_button.clicked.connect(self.encrypt_data)
        layout.addWidget(self.encrypt_button)

        self.encrypted_data_label = QLabel("Encrypted Data:")
        layout.addWidget(self.encrypted_data_label)

        self.encrypted_data_output = QLabel()
        layout.addWidget(self.encrypted_data_output)

        self.decrypt_button = QPushButton("Decrypt")
        self.decrypt_button.clicked.connect(self.decrypt_data)
        layout.addWidget(self.decrypt_button)

        self.decrypted_data_label = QLabel("Decrypted Data:")
        layout.addWidget(self.decrypted_data_label)

        self.decrypted_data_output = QLabel()
        layout.addWidget(self.decrypted_data_output)

        self.setLayout(layout)
        self.setWindowTitle("Encryption App")

    def encrypt_data(self):
        original_data = self.original_data_input.text()
        data_bytes = original_data.encode()
        encrypted_data = self.cipher_suite.encrypt(data_bytes)
        self.encrypted_data_output.setText(encrypted_data.decode())

    def decrypt_data(self):
        encrypted_data = self.encrypted_data_output.text().encode()
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        self.decrypted_data_output.setText(decrypted_data.decode())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EncryptionApp()
    window.show()
    sys.exit(app.exec_())
