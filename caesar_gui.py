# !\Users\jason\Desktop\ceasar_cipher\caesar_gui.py
import tkinter as tk
from tkinter import ttk


# Create the main window for the caeser cipher
class caesarCipherGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Caesar Cipher")
        self.root.geometry("300x600")
        
        # Initialize the tabs
        tab_control = ttk.Notebook(self.root)
        
        # Create both tabs for encrypt and decrypt
        encrypt_tab = ttk.Frame(tab_control)
        decrypt_tab = ttk.Frame(tab_control)
        
        # Create the clickable tabs
        tab_control.add(encrypt_tab, text="encrypt message")
        tab_control.add(decrypt_tab, text="decrypt message")
        
        # Place tab bar at the top of the screen
        tab_control.pack(fill="both", expand=1)
        
        # Create frame for encryption key
        self.encryptkey = ttk.Frame(encrypt_tab)
        self.encryptkey.pack()
        
        # Create frame for encryption message
        self.encryptmessage = ttk.Frame(encrypt_tab)
        self.encryptmessage.pack()
        
        # Widgets inside encrypt key frame
        self.enkey_label = ttk.Label(self.encryptkey,
                                   text="Enter the encryption key: ")
        self.enkey_label.pack(side="left")
        
        self.enkey_entry = ttk.Entry(self.encryptkey, width="5")
        self.enkey_entry.pack(side="left")
        
        # Widgets inside encrypt message frame
        self.enmessage_label = ttk.Label(self.encryptmessage, text="Enter the message you wish to encrypt:")
        self.enmessage_label.pack()
        
        enS = tk.Scrollbar(self.encryptmessage)
        enT = tk.Text(self.encryptmessage, height=8, width=50)
        enS.pack(side="right", fill="y")
        enT.pack(side="left", fill="y")
        enS.config(command=enT.yview)
        enT.config(yscrollcommand=enS.set)

        # Create button for encrypting message
        self.encrypt_button = tk.Button(encrypt_tab, text="encrypt message", command = self.encryption)
        self.encrypt_button.pack()
        
        # Create frame for the returned encrypted message
        self.enmessage = ttk.Frame(encrypt_tab)
        self.enmessage.pack()

        self.encrypted_answer = tk.StringVar()  # Dynamic label for the encrypted answer

        self.dyn_enanswer_label = ttk.Label(self.enmessage, textvariable=self.encrypted_answer)
        self.dyn_enanswer_label.pack()

        # Widgets that will be placed on decryption tab
        # Create frame for decryption key
        self.decryptkey = ttk.Frame(decrypt_tab)
        self.decryptkey.pack()
        
        # Create frame for decryption message
        self.decryptmessage = ttk.Frame(decrypt_tab)
        self.decryptmessage.pack()
        
        # Widgets for decrypt key
        self.dekey_label = ttk.Label(self.decryptkey,
                                   text="Enter the decryption key: ")
        self.dekey_label.pack(side="left")
        
        self.dekey_entry = ttk.Entry(self.decryptkey, width="5")
        self.dekey_entry.pack(side="left")

        # Widgets inside encrypt message frame
        self.demessage_label = ttk.Label(self.decryptmessage, text="Enter the message you wish to decrypt:")
        self.demessage_label.pack()
        
        deS = tk.Scrollbar(self.decryptmessage)
        deT = tk.Text(self.decryptmessage, height=8, width=50)
        deS.pack(side="right", fill="y")
        deT.pack(side="left", fill="y")
        deS.config(command=deT.yview)
        deT.config(yscrollcommand=deS.set)

        # Create button for decrypting message
        self.decrypt_button = tk.Button(decrypt_tab, text="decrypt message", command = self.decryption)
        self.decrypt_button.pack()

        # Create frame for the returned decrypted message
        self.demessage = ttk.Frame(decrypt_tab)
        self.demessage.pack()
        
        self.decrypted_answer = tk.StringVar()  # Dynamic label for the encrypted answer

        self.dyn_deanswer_label = ttk.Label(self.demessage, textvariable=self.decrypted_answer)
        self.dyn_deanswer_label.pack()

        # Overall statement to run the app once the class definition has been called
        self.root.tk.mainloop()


    def encryption(self):
        # Verify that the input for the key and intended message is correct type
        try:
            enkey = float(self.enkey_entry.get())
            enmessage = str(enT.get())

        except TypeError:
            self.encrypted_answer.set("An error has occurred")


    def decryption(self):
        # Verify that the input for the key and intended message is correct type
        try:
            dekey = float(self.dekey_entry.get())
            demessage = str(deT.get())

        except TypeError:
            self.decrypted_answer.set("An error has occurred")
        
        

if __name__ == "__main__":
    try:
        caesar_cipher = caesarCipherGui()
    except KeyboardInterrupt:
        exit()
        
        
