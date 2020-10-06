import rpyc
from rpyc.utils.server import ThreadedServer
import datetime
import subprocess

date_time = datetime.datetime.now()

class MonitorService(rpyc.Service):
    def on_connect(self, conn):
        print('\nConnected on {}'.format(date_time))
    
    def on_disconnect(self, conn):
        print('Disconnected on {}\n'.format(date_time))

    def exposed_run_command(self, command):
        try:
            output = subprocess.check_output(command, shell=True)
            print(output)
        except subprocess.CalledProcessError as Error:
            print(Error.returncode)
            print(Error.output)

if __name__ == "__main__":
    t = ThreadedServer(MonitorService, port = 19961)
    t.start()
