import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import pyttsx3

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('texttospeech.jpeg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo_label
logo_label.grid(column=1, row=0)


# instructions
instructions = tk.Label(root, text="Select a PDF file to read it's text",
font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

# function to open file
def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file",
    filetype=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        number_of_pages = read_pdf.getNumPages()
        page_content = page.extractText()

        # test browse_text
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        # saying the text
        engine = pyttsx3.init()
        for i in range(0, number_of_pages):
            # say method on the engine that passing input text to be spoken
            engine.say(page_content)

            # run and wait method to process the voice commands
            engine.runAndWait()

        browse_text.set("Browse")


# browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, font="Raleway",
bg="#20bebe", fg="white", height=2, width=15, command=lambda:open_file())
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()

 
