import subprocess

def run():
    try:
        with open("/rasmnout/log/execute.log", "r") as f:
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
                    with open("/rasmnout/log/all-output.log", "a") as all_output_file:
                        all_output_file.write(output.decode())
                    with open("/rasmnout/log/output.log", "w") as output_file:
                        output_file.write(output.decode())
    except FileNotFoundError:
        print("[PROBLEM] Error with file execute.rsmnt")

run()
