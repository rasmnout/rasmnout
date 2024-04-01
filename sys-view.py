import subprocess
import time

def run():
    try:
        while True:
            with open("/rasmnout/log/execute.log", "r") as f:
                current_position = f.tell()  # Store current position
                fg = f.read()
                f.seek(current_position)  # Seek back to the stored position
                fgg = f.read()
                
                if fgg == fg:
                    pass
                else:
                    fg = fgg
                    process = subprocess.Popen(fgg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    output, error = process.communicate()
                    print(output.decode())
                    status = "successfully"
                    if error:
                        print("[PROBLEM] PROBLEM:")
                        print(error.decode())
                        status = "error"
                    with open("/rasmnout/log/all-output.log", "a") as f:
                        f.write(output.decode())
                    with open("/rasmnout/log/output.log", "w") as f:
                        f.write(output.decode())
                    with open("/rasmnout/log/status.log", "w") as f:
                        f.write(status)
            time.sleep(1)  # Add a short delay to avoid busy-waiting
    except FileNotFoundError:
        print("[PROBLEM] error with file execute.log")

run()
