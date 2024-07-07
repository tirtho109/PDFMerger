import os
from tkinter import Tk, Label, Button, Listbox, END, filedialog, messagebox, Frame
from tkinterdnd2 import TkinterDnD, DND_FILES
from PyPDF2 import PdfMerger

class PDFMergerApp:
    def __init__(self, master):
        self.master = master
        master.title("PDF Merger")

        self.label = Label(master, text="Select and Sort PDF files to merge:")
        self.label.pack()

        self.listbox = Listbox(master, selectmode="extended")
        self.listbox.pack(fill="both", expand=True)

        self.button_frame = Frame(master)
        self.button_frame.pack(fill="x")

        self.browse_button = Button(self.button_frame, text="Browse", command=self.browse_files)
        self.browse_button.pack(side="left", anchor="sw")

        self.merge_button = Button(self.button_frame, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.pack(side="right", anchor="se")

        self.listbox.bind('<Button-1>', self.start_drag)
        self.listbox.bind('<B1-Motion>', self.do_drag)
        self.listbox.bind('<ButtonRelease-1>', self.stop_drag)

        self.drag_data = {"item": None, "index": None}

    def browse_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        for file_path in file_paths:
            self.listbox.insert(END, file_path)

    def merge_pdfs(self):
        selected_files = self.listbox.get(0, END)

        if not selected_files:
            messagebox.showerror("Error", "No PDF files selected")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if not output_path:
            return

        merger = PdfMerger()

        for pdf in selected_files:
            merger.append(pdf)

        with open(output_path, 'wb') as output_file:
            merger.write(output_file)

        merger.close()
        messagebox.showinfo("Success", f"Successfully merged {len(selected_files)} PDFs into {output_path}")

    def start_drag(self, event):
        self.drag_data["item"] = self.listbox.get(self.listbox.nearest(event.y))
        self.drag_data["index"] = self.listbox.nearest(event.y)
        return "break"

    def do_drag(self, event):
        i = self.listbox.nearest(event.y)
        if i < len(self.listbox.get(0, END)):
            self.listbox.delete(self.drag_data["index"])
            self.listbox.insert(i, self.drag_data["item"])
            self.drag_data["index"] = i
        return "break"

    def stop_drag(self, event):
        self.drag_data = {"item": None, "index": None}
        return "break"

def main():
    root = TkinterDnD.Tk()
    app = PDFMergerApp(root)
    root.geometry("500x500")
    root.mainloop()

if __name__ == "__main__":
    main()
