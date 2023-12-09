#Receiver app works along with kivy application.
#Below are kivy modules used for the application.
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.effects.scroll import ScrollEffect
from kivy.graphics import Color
from kivy.graphics import Color, Rectangle
import socket

class Receiver_App(App):
    def build(self):
        self.result_binary_data=""
        self.elements=[
             "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si",
            "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni",  
            "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb",
             "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
            "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho",
            "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
             "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np",
            "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg",
            "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
        ]
        
        # Box Layout for elements
        layout = BoxLayout(orientation='vertical')
    
        # Showing the message status
        self.status_message_label = Label(text=" W A I T I N G .....", font_size=55)
        layout.add_widget(self.status_message_label)
        with layout.canvas.before:
            Color(rgb=(0.2, 0.2, 0.2)) 
            self.rect = Rectangle(pos=layout.pos, size=layout.size)

        # Mode selection button
        uni_mode_button = Button(text=" U N I C O D E ", # unicode symbol
                           on_press=self.sel_unicode_mode,
                           background_color=(0.5,0.5,0.5,1),
                           background_normal='',
                           color=(1,1,1,1),
                           font_size=50,
                           font_name = "Roboto")
        

        periodic_mode_button = Button(text=" P E R I O D I C ", # periodic table symbol
                           on_press=self.sel_periodic_mode,
                           background_color=(0.5,0.5,0.5,1), 
                           background_normal='',
                           color=(1,1,1,1),
                           font_size=50,
                           font_name = "Roboto")
        

        layout.add_widget(periodic_mode_button)
        layout.add_widget(uni_mode_button)
        

        return layout
    
    def sel_unicode_mode(self, instance):
        self.mode = 'U'
        self.receive_bin_data()

    def sel_periodic_mode(self, instance):
        self.mode = 'P'
        self.receive_bin_data()

    def receive_bin_data(self):
        # Socket for listening incoming binary data.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_addr = ('localhost', 8888)
            server_socket.bind(server_addr)
            server_socket.listen()

            self.status_message_label.text = "Waiting for connection..."

            # Accept connection from the sender
            connection, sender_addr = server_socket.accept()
            self.status_message_label.text = f"Connected to {sender_addr}"

            # Showing receiving each digit at a time.
            while True:
                received_bin_digit = connection.recv(8).decode()
                if received_bin_digit.lower() == 'done':
                    break
                self.result_binary_data += received_bin_digit
                print("Received:", received_bin_digit)

            # Based on the mode decode the message.
            decoded_message = self.decode_binary_data(self.elements)
            self.status_message_label.text = f"M E S S A G E : {decoded_message}"

            # Clear the list for new message.
            self.result_binary_data = ""

            # Close the connection
            connection.close()

    def decode_binary_data(self, elements):
        decoded_string = ""
        for i in range(0, len(self.result_binary_data), 8):
            byte_val = self.result_binary_data[i:i+8]
            if byte_val == '00100000':    # for the spaces, we will use this binary data.
                decoded_string += ' '
            else:
                decimal_val = int(byte_val, 2)
                if self.mode == 'U':
                    decoded_string += chr(decimal_val)
                elif self.mode == 'P':
                    if decimal_val > 0 and decimal_val <= 118:
                        element = elements[decimal_val-1]
                        decoded_string += element[0]
                    elif decimal_val > 118:                 # for handling the value received more than 118 for handling the errors.
                        decimal_val = decimal_val % 118
                        element = elements[decimal_val-1]
                        decoded_string += element[0]
                    else:
                        decoded_string += 'X'  # Placeholder for invalid decimal_val numbers
                
        return decoded_string

if __name__ == '__main__':
    Receiver_App().run()