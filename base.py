import base64
import kivy
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from PIL import Image
from itertools import chain
from kivy.graphics.texture import Texture
import numpy as np
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup


kivy.require("2.3.0")

class MyRoot(BoxLayout):
    """functions go here """
    image_source = StringProperty("")

    def __init__(self):
        super(MyRoot, self).__init__()

    def choose_file(self):
        """
            *opens a file selector window
            *allows the user to select an image file
        """

        content = BoxLayout(orientation="vertical")
        file_chooser = FileChooserIconView(
            filters=["*.jpg", "*.png"],
            path=os.path.expanduser("~")
        )

        def select_file(instance):
            if file_chooser.selection:
                self.selected(file_chooser.selection)
                popup.dismiss()

        # Create buttons for the popup
        buttons = BoxLayout(size_hint_y=None, height=40)
        select_button = Button(text="Select", size_hint_x=0.5)
        cancel_button = Button(text="Cancel", size_hint_x=0.5)

        select_button.bind(on_release=select_file)
        cancel_button.bind(on_release=lambda x: popup.dismiss())

        buttons.add_widget(select_button)
        buttons.add_widget(cancel_button)

        content.add_widget(file_chooser)
        content.add_widget(buttons)

        popup = Popup(
            title="Choose an image file",
            content=content,
            size_hint=(0.9, 0.9)
        )
        popup.open()

    def selected(self, selection):
        """
        *Process the selected image file.
        *Update the image path and preview.

        Args:
            selection: A list containing the path of the selected file.
                while a list is possible as user can select multiple files only the first file is converted to base64
        """
        if selection:
            self.original_path = selection[0]
            self.ids.image_path.text = selection[0]
            self.image_source = self.original_path

    def png_to_base64(self):
        """
        *Convert the selected image to base64.
        *Update the base64 text input.

        Args:
            self (MyRoot): The instance of the MyRoot class.
        """
        if hasattr(self, "original_path"):
            text_input = self.ids.basepart
            try:
                with open(self.original_path, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                text_input.text = encoded_string
            except FileNotFoundError:
                text_input.text = f"Error: File not found at {self.original_path}"
            except Exception as e:
                text_input.text =f"An error occurred: {e} for {self.original_path}"

class base(App):
    """app gets build here"""
    def build(self):
        return MyRoot()


if __name__ == "__main__":
    rz_image  = base()
    Window.size = (600, 650)
    rz_image.run()
