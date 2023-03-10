from midi import MidiParser
from sac import SAC

MIDI_CHANNEL = 2

mp = MidiParser(uart_id=0)
sac = SAC(uart_id=1)

while True:
    pc = mp.parse()
    if pc:
        if pc['channel'] == MIDI_CHANNEL:
            print(f"Selecting SAC channel: {pc['program']}")
            sac.selectChannel(pc['program'])