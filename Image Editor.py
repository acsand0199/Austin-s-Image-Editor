from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

# Define global variables
original_image = None
edited_image = None  # This variable keeps a reference to the edited image
displayed_image = None  # This variable keeps a reference to the displayed image

def main():
    root = Tk() # creates main window
    root.title("Austin's Image Editor")

    def open_image():
        global original_image, edited_image, displayed_image
        file_path = filedialog.askopenfilename() # triggers the askopenfilename function from the filedialog. askopenfilename returns the file path of the selected file as a string.
        if file_path:
            original_image = Image.open(file_path)
            edited_image = original_image.copy()  # Make a copy to store edited version
            displayed_image = ImageTk.PhotoImage(original_image) #ImageTk module used PhotoImage to convert the original image into a Tkinter compatible photo image
            img_label.config(image=displayed_image) #.config method configures the label widget to be equal to the displayed image 

    def apply_filter(filter_function):
        global edited_image, displayed_image
        if edited_image:
            edited_image = filter_function(edited_image) #applies a specific image filter function (filter_function) to an edited image
            displayed_image = ImageTk.PhotoImage(edited_image)
            img_label.config(image=displayed_image)

    def blur_filter(image): #Image is expected to be a PIL image object
        return image.filter(ImageFilter.BLUR) 

    def sharpen_filter(image):
        return image.filter(ImageFilter.SHARPEN)

    def enhance_edges_filter(image):
        return image.filter(ImageFilter.EDGE_ENHANCE)

    def contour_filter(image):
        return image.filter(ImageFilter.CONTOUR)

    def save_image():
        global edited_image
        if edited_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg") #opens a save dialog box with a default extension of jpg
            if file_path:
                edited_image.save(file_path) #saves the edited image

    open_button = Button(root, text="Open Image", command=open_image)
    blur_button = Button(root, text="Blur", command=lambda: apply_filter(blur_filter)) # lambda creates a small inline function without a name 
    sharpen_button = Button(root, text="Sharpen", command=lambda: apply_filter(sharpen_filter))
    enhance_edges_button = Button(root, text="Enhance Edges", command=lambda: apply_filter(enhance_edges_filter))
    contour_button = Button(root, text="Contour", command=lambda: apply_filter(contour_filter))
    save_button = Button(root, text="Save Image", command=save_image)

    img_label = Label(root)
    open_button.place(x=1400, y=0)
    blur_button.place(x=1400, y=30)
    sharpen_button.place(x=1400, y=60)
    enhance_edges_button.place(x=1400, y=90)
    contour_button.place(x=1400, y=120)
    save_button.place(x=1400, y=150)
    img_label.place(x=120, y=0)

    root.attributes('-fullscreen', True) #sets the tkinter window to full screen

    def toggle_fullscreen(event=None): # event none means parameter is optional
        state = root.attributes('-fullscreen') # retrieve current state of the fullscreen attribute and assigns it to state
        root.attributes('-fullscreen', not state) # not sets state equal to false exiting the full screen

    root.bind("<Escape>", toggle_fullscreen) #when you press escape calls the toggle_fullscreen function 

    root.mainloop()

if __name__ == "__main__":
    main()