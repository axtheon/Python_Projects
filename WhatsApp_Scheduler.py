import pywhatkit

def send_whatsapp_message(phone_number: str, message: str, hours: int, minutes: int):
    """
    Send a WhatsApp message at a specific time using pywhatkit.

    Parameters:
        phone_number (str): Recipient's number with country code. Example: "+923001234567"
        message (str): The message to be sent.
        hours (int): Hour in 24-hour format (e.g., 22 for 10 PM).
        minutes (int): Minute of the hour (e.g., 30 for :30).
    """
    try:

        pywhatkit.sendwhatmsg(phone_number, message, hours, minutes)
        print(f"Message scheduled to {phone_number} at {hours}:{minutes:02d}")

    except Exception as e:

        print("Something went wrong. Please check:")
        print("   1. Your internet connection")
        print("   2. WhatsApp Web login")
        print("   3. Phone number format (e.g., +923001234567)")
        print(f"   Error details: {e}")


if __name__ == "__main__":
    print("WhatsApp Message Scheduler")
    print("-" * 40)

    phone_number = input("Enter recipient's phone number with country code (e.g., +923001234567): ").strip()
    message = input("Enter your message: ").strip()
    hours = int(input("Enter hour (24h format, e.g., 19 for 7 PM): ").strip())
    minutes = int(input("Enter minutes (e.g., 30 for half past): ").strip())

    send_whatsapp_message(phone_number, message, hours, minutes)


