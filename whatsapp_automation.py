import pywhatkit as kit

phone_number = input("Enter phone number with country code: ")

kit.sendwhatmsg(phone_number, "Hello", 15, 19)