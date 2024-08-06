import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os
import pyautogui

class FileExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Extractor Tool")

        self.selected_files = []
        self.destination_folder = ""

        self.create_widgets()

    def create_widgets(self):
        self.select_files_button = tk.Button(self.root, text="Select Files", command=self.select_files)
        self.select_files_button.pack(pady=10)

        self.select_destination_button = tk.Button(self.root, text="Select Destination", command=self.select_destination)
        self.select_destination_button.pack(pady=10)

        self.extract_button = tk.Button(self.root, text="Extract Files", command=self.extract_files)
        self.extract_button.pack(pady=10)

        # self.delete_button = tk.Button(self.root, text="Delete Files", command=self.delete_files, fg='red')
        # self.delete_button.pack(pady=10, side=tk.RIGHT)

    def select_files(self):
        files = filedialog.askopenfilenames(title="Select Files")
        if files:
            self.selected_files = files
            messagebox.showinfo("Info", f"Selected {len(files)} files.")

    def select_destination(self):
        folder = filedialog.askdirectory(title="Select Destination Folder")
        if folder:
            self.destination_folder = folder
            messagebox.showinfo("Info", f"Selected destination: {folder}")

    def extract_files(self):
        if not self.selected_files or not self.destination_folder:
            messagebox.showwarning("Warning", "Please select files and a destination folder first.")
            return

        for file in self.selected_files:
            if zipfile.is_zipfile(file):
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    zip_ref.extractall(self.destination_folder)
            else:
                messagebox.showwarning("Warning", f"{file} is not a zip file.")

        messagebox.showinfo("Info", "Extraction complete.")

    # def delete_files(self):
    #     if not self.selected_files:
    #         messagebox.showwarning("Warning", "Please select files first.")
    #         return
    #
    #     for file in self.selected_files:
    #         try:
    #             os.startfile(file, 'open')
    #             pyautogui.hotkey('alt', 'space')
    #             pyautogui.press('d')
    #             pyautogui.press('enter')
    #         except Exception as e:
    #             messagebox.showerror("Error", f"Failed to delete {file}. Error: {str(e)}")
    #             continue
    #
    #     messagebox.showinfo("Info", "Files deleted.")
    #     self.selected_files = []

if __name__ == "__main__":
    root = tk.Tk()
    app = FileExtractorApp(root)
    root.mainloop()
