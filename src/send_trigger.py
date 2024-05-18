from psychopy import parallel
import time

class Trigger:
    def __init__(self, port_address=0x4FF8):
        self.port = parallel.ParallelPort(address="0x4FF8")
        self.port.setData(port_address)

    def send_trigger(self, trigger_value):
        self.port = parallel.ParallelPort(address="0x4FF8")
        self.port.setData(trigger_value)