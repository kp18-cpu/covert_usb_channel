# covert_usb_channel
This covert channel is a replica of USB covert channel process. 
The sender will send the binary data based on the mode selected by the receiver and based on the mode sender will send the data.
This is synchronous channel as it is timing based covert channel, so receiver should listen to receive the message to ensure the message properly getting delivered.

# How to run this both file.
# Make sure you have python installed in your system and KIVY
For installing kivy give "pip install kivy" and then began the terminal for .py files.
1. Open this both .py file (sender and receiver) on any code editor.
2. Start two terminal's one is for receiver and another one for sender.
3. First start the receiver by giving "python receiver.py" and the kivy app will start, then in the application giving the mode through which you need the message.
4. Then start the sender in other terminal by giving "python sender.py".
5. It will ask for the mode, give the mode you selected in receiver end, and give the message to send the message, and you will see the result in kivy application.


Below image shows the receiver end...
![image](https://github.com/kp18-cpu/covert_usb_channel/assets/144280339/1a526022-9ced-4e8d-9ce5-436eb1874a2b)

Below image shows the sender sent the message and receiver got it.
![image](https://github.com/kp18-cpu/covert_usb_channel/assets/144280339/6fa143b3-0a2a-4b5e-a51d-ca094f622d51)

