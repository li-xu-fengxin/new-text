import serial
import time
from queue import Queue



import logging

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

class Ble:

    def __init__(self) -> None:
        
        self.ser = serial.Serial('/dev/ttyS5', 9600)

        self.task_queue = Queue(100)

    # def start_ble_server(self):

    #     while True:

    #         try:

    #             data = self.ser.read(self.ser.in_waiting).decode()

    #         except Exception as e:

    #             logger.error(str(e))

    #         else:

    #             logger.info(f"receive_str:{data}")


    def start_ble_server(self):

        while True:
            try:
                if self.ser.in_waiting > 0:
                    data = self.ser.read(self.ser.in_waiting).decode()
                    logger.info(f"receive_str:{data}")
            except Exception as e:
                logger.error(str(e))


if __name__ == "__main__":

    Ble().start_ble_server()