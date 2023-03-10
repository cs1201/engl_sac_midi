import machine

BAUD_RATE = 31250
MIDI_CHANNEL_DEFAULT = 1

uart = machine.UART(0, BAUD_RATE)

class MidiMessage:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class MidiParser:
    def __init__(self, uart_id):
        self.uart_id = uart_id
        self.uart = machine.UART(0, BAUD_RATE)
        self.channel = 0
        self.status = 0
        self.program = 0

    def parse(self):
        if not self.uart.any():
            return None

        byte = self.uart.read(1)[0]

        if ((byte >= 0xC0) and (byte <= 0xCF)):
            self.status = byte
            self.channel = (byte & 0xF)+1
            return None
        else:
            if self.status == 0:
                # Have not yet recieved PC status byte
                return None
            self.program = byte
            print(f"Program Change: ch={self.channel}, program={self.program}")
            self.status = 0
            return {"channel": self.channel, "program": self.program}

