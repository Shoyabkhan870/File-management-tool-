


import os
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

class FileBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("Python File Management Tool")
        self.root.geometry("600x400")

        # Frame for tree view
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Treeview for directory browsing
        self.tree = ttk.Treeview(self.frame, columns=('Path',), show="tree")
        self.tree.heading("#0", text="Name", anchor="w")
        self.tree.heading("Path", text="Path", anchor="w")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Button to open directory
        self.open_dir_button = ttk.Button(self.root, text="Open Directory", command=self.open_directory)
        self.open_dir_button.pack(pady=10)

        # Context menu
        self.tree.bind("<Double-1>", self.open_file)

    def open_directory(self):
        # Open a directory selection dialog
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.populate_tree(dir_path)

    def populate_tree(self, directory, parent=""):
        # Clear existing tree
        self.tree.delete(*self.tree.get_children())

        for root, dirs, files in os.walk(directory):
            # Create tree nodes
            root_id = self.tree.insert(parent, tk.END, text=os.path.basename(root), open=True, values=(root,))
            for dir_name in dirs:
                self.tree.insert(root_id, tk.END, text=dir_name, values=(os.path.join(root, dir_name),))
            for file_name in files:
                self.tree.insert(root_id, tk.END, text=file_name, values=(os.path.join(root, file_name),))

    def open_file(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            file_path = self.tree.item(selected_item[0], "values")[0]
            if os.path.isfile(file_path):
                # Open the file (modify as per your use case)
                try:
                    with open(file_path, "r") as file:
                        content = file.read()
                        messagebox.showinfo("File Content", content[:1000])
                except Exception as e:
                    messagebox.showerror("Error", f"Unable to open file: {e}")

if __name__ == "__main__":
    root = ("link unavailable")()
    app = FileBrowser(root)
    root.mainloop()
