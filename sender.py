#Sender with two modes of communication (Unicode and periodic)
import random
import socket

elements=["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si",
          "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni",  
          "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb",
          "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
          "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho",
          "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
          "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np",
          "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg",
          "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]


def periodic_binary(inp_str):  
    binary_data_list = []
    for char in inp_str:
        if char == ' ':
            binary_data_list.append('00100000')
        else:
            char_val = char.upper()
            charnum_array = []
            for i in range(0, 118):
                element = elements[i]
                char_element = element[0]
                if char_element == char_val:
                    charnum_array.append(i + 1)
            final_number_of_elements = random.choice(charnum_array)
            binary_format = bin(final_number_of_elements).replace("0b", "")
            binary_data_list.append(binary_format.zfill(8))
    return binary_data_list

def unicode_binary(inp_str):
    binary_data_list = []
    for char in inp_str:
        if char == ' ':
            binary_data_list.append('00100000')
        else:
            char_int = ord(char)
            char_bin = f'{char_int:08b}'
            binary_data_list.append(char_bin)
    return binary_data_list

while True:
  enc_mode = input("Enter U for Unicode, P for Periodic: Exit : CTRL+C : ")
  if enc_mode in ('U', 'P'):
    break
  else:
    print("Invalid mode, please try again.")

inp_str = input("Enter string: ")

if enc_mode == 'U':
    bin_data = unicode_binary(inp_str)
elif enc_mode == 'P':
    bin_data = periodic_binary(inp_str)
else:
    print("Invalid mode, give proper mode")

# Establishing socket connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    server_addr = ('localhost', 8888)
    client_socket.connect(server_addr)

    # Showing sending each digit at a time
    for binary_dig in bin_data:
        client_socket.sendall(binary_dig.encode())
        print("Sent:", binary_dig)

    # Sending done to say the transaction is done.
    client_socket.sendall('done'.encode())
    print("Transmission completed.")
