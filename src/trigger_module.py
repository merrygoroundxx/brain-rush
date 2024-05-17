import parallel
import time

class Trigger:
    def __init__(self, port_address=0x378):
        self.port = parallel.Parallel()
        self.port.setData(port_address)

    def send_trigger(self, trigger_value, duration=0.1):
        """Send a trigger signal to the parallel port.
        
        Args:
            trigger_value (int): The value to send through the parallel port.
            duration (float): The duration to hold the trigger signal (in seconds).
        """
        self.port.setData(trigger_value)
        time.sleep(duration)
        self.port.setData(0)
