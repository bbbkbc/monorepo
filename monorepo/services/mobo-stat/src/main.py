import subprocess


class Commands:
    turbo_command = "sudo turbostat -s Core,CPU,Avg_MHz,Busy%,Bzy_MHz,CoreTmp,PkgTmp,Totl%C0,PkgWatt,CorWatt,RAM_% -i 0.1"
    i7z_command = "sudo iz7"


class MoboStat:
    @staticmethod
    def stream_command(command):
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )

        headers = []  # This will store the headers123BlazeJ
        for i, output in enumerate(process.stdout):
            output = output.strip()  # Remove newline characters and trailing spaces
            if i == 0:  # Assuming the first line contains headers
                headers = output.split('\t')  # Split the headers by tab
                continue  # Skip the rest of the loop for the first iteration
            if output == '' and process.poll() is not None:
                break
            if output:
                data = output.split('\t')  # Split the data by tab
                data_dict = dict(zip(headers, data))
                if data_dict['Core'] == "-":
                    print(data_dict)

        rc = process.poll()
        return rc

    def emit_event(self):
        pass


if __name__ == '__main__':
    MoboStat.stream_command(Commands.turbo_command)
