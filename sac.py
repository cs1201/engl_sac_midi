import machine
import ubinascii

BAUD_RATE = 31250

class SAC:
    SAC_CHANNEL_MSG = [b'\x40', b'\x41', b'\x42', b'\x43']
    
    def __init__(self, uart_id):
        self.uart_id = uart_id
        self.uart = machine.UART(self.uart_id, BAUD_RATE)
        self.uart.init(BAUD_RATE, tx=machine.Pin(8), bits=8, parity=None, stop=1)
        return
    
    def selectChannel(self, channel):
        if channel > len(self.SAC_CHANNEL_MSG):
            return
        msg = bytes(self.SAC_CHANNEL_MSG[channel-1])
        self.uart.write(msg)

        
