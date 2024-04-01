import subprocess

print("[INFO] Sucessfully started HTTP EXECUTER")

def start_exe():
    try:
        with open("execute.rsmnt", "+r") as f:
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
                    if error:
                        print("[PROBLEM] PROBLEM:")
                        print(error.decode())
                    with open("/rasmnout/log/all-output.log","a") as f:
                      f.write(output.decode())
                    with open("/rasmnout/log/output.log","w") as f:
                      f.write(output.decode())
    except FileNotFoundError:
        print("[PROBLEM] error with file execute.rsmnt")

start_exe()
