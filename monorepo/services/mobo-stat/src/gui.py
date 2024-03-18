import subprocess
from PySide6.QtCore import QObject, Signal, Slot, QCoreApplication


class Commands:
    turbo_command = "sudo turbostat -s Core,CPU,Avg_MHz,Busy%,Bzy_MHz,CoreTmp,PkgTmp,Totl%C0,PkgWatt,CorWatt,RAM_% -i 0.1"
    i7z_command = "sudo i7z"


class MoboStat(QObject):
    data_emitter = Signal(dict)  # Correct placement for the signal

    def __init__(self):
        super().__init__()  # Proper initialization of the QObject base class

    def stream_command(self, command):
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )

        headers = []
        for output in process.stdout:
            output = output.strip()
            if headers == []:
                headers = output.split('\t')
                continue
            if output == '' and process.poll() is not None:
                break
            if output:
                data = output.split('\t')
                data_dict = dict(zip(headers, data))
                self.data_emitter.emit(data_dict)

        rc = process.poll()
        return rc


# Slot to handle emitted data
def handle_data(data):
    print(data)  # Simple print statement to verify emitted data


if __name__ == '__main__':
    app = QCoreApplication([])  # Necessary to initialize the Qt event loop
    moboStat = MoboStat()
    moboStat.data_emitter.connect(handle_data)  # Connect the signal to the slot

    # You might need to run stream_command in a separate thread to avoid blocking,
    # but for simplicity, let's just call it directly for now.
    moboStat.stream_command(Commands.turbo_command)

    app.exec()  # Start the event loop
