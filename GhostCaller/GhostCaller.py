import binascii
#GhostCaller an Android CallerID spoofer developed by Deccatron

def construct_pdu(sender, recipient, message):
    try:
        # Convert sender, recipient, and message to hexadecimal representation
        sender_hex = binascii.hexlify(sender.encode()).decode()
        recipient_hex = binascii.hexlify(recipient.encode()).decode()
        message_hex = binascii.hexlify(message.encode()).decode()

        # Calculate PDU length
        pdu_length = len(message_hex) // 2 + 13  # Length of message + 7 bytes for SMS-SUBMIT + 6 bytes for sender + 1 byte for message length

        # Construct PDU
        pdu = (
            f'00'  # SMSC address length (0, which means the SMSC stored in the phone should be used)
            f'11'  # PDU Type (11 for SMS-SUBMIT)
            f'00'  # Message reference (arbitrary value)
            f'00{len(sender_hex) // 2:02X}'  # Sender address length (0 for alphanumeric, length of sender in octets)
            f'91{sender_hex}F'  # Sender address (91 prefix for international format)
            f'00'  # Protocol identifier
            f'00'  # Data coding scheme (0 for default 7-bit alphabet)
            f'{pdu_length:02X}'  # Length of message
            f'{recipient_hex}'  # Recipient address
            f'00'  # Validity period (not used in this example)
            f'00'  # User data header length (not used in this example)
            f'{message_hex}'  # Message
        )

        return pdu

    except Exception as e:
        print(f"Error constructing PDU: {e}")
        return None

# Example usage
def main():
    sender = "CustomSender"
    recipient = "+1234567890"  # Phone number of the recipient
    message = "Hello, this is a test message."

    pdu = construct_pdu(sender, recipient, message)
    if pdu:
        print("Constructed PDU:", pdu)

if __name__ == "__main__":
    main()