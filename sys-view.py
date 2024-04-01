import os
with open("/rasmnout/sys/output.log","r") as f:
  content = f.read()
print(content)

try:
  while True:
    with open("/rasmnout/sys/output.log","r") as f:
      new_content = f.read()
      if not new_content == content:
        print(new_content)
        content = new_content
      else:
        pass
except Exception as e:
    print(f"[ERROR] {e}")
except KeyboardInterrupt:
  os.system("sudo shutdown -r now")
    
