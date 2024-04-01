import subprocess

print("[INFO] Sucessfully started HTTP EXECUTER")

def start_exe():
    try:
        with open("/rasmnout/sys/output.log", "+r") as f:
            fg = f.read()
            while True:
                f.seek(0)
                fgg = f.read()
                if fgg == fg:
                    pass
                else:
                    fg = fgg
                    process = subprocess.Popen(fgg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    output, error = process.communicate()
                    print(output.decode())
                    status = "sucessfully"
                    if error:
                        print("[PROBLEM] PROBLEM:")
                        print(error.decode())
                        status = "error"
                    with open("/rasmnout/log/all-output.log","a") as f:
                      f.write(output.decode())
                    with open("/rasmnout/log/output.log","w") as f:
                      f.write(output.decode())
                    with open("/rasmnout/log/status.log","w") as f:
                      f.write(status)
    except FileNotFoundError:
        print("[PROBLEM] error with file execute.rsmnt")

start_exe()
