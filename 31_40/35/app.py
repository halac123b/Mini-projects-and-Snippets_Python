import tkinter
import os

class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tkinter.StringVar()
        self.selected_images_listbox = tkinter.Listbox(self.root, selectmode=tkinter.MULTIPLE)

    def inintialize_UI(self):
        title_label = tkinter.Label(self.root, text="Image to PDF Converter", font=("Helvetica", 16, "bold"))
        title_label.pack()