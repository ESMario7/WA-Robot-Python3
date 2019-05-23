# WA-Robot-Python3
This project works with WhatsApp Web Application on Ubuntu. It will send messages and images to a contacts list from a .csv file and keep track of every action the bot does. In order for it to work, you'll need to use your phone for the QR code and you'll also need to use Google Contacts to import the contacts list to your phone. 

Assuming you already imported the contacts list to your phone using the .csv file, you'll need to check is they loaded correctly on your phone. If the contacts were imported correctly, you just need to check or change the message, image or images that you are going to use. Remember to check the .csv file that contents the xpath of WhatsApp Web because they'll change eventually. If one of the xpath changes you can just go to WhatsApp Web and copy the new xpath and replace te old one.

How it works:

The bot will need someone to enter WhatsApp Web since it needs to pass a QR code. After that, just press enter. The bot will tell you when it uses an image for every contact. It'll go trough the contacts list by name until the list is complete. At the end, the program will create a log.txt file that will contain a register of all the contacts the bot worked with. The bot will append to the log.txt each time it operates.
