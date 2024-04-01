
with open("/rasmnout/sys/output.log","r") as f:
  content = f.read()
print(content)
while True:
  try:
    with open("/rasmnout/sys/output.log","r") as f:
      new_content = f.read()
      if not new_content == content:
        print(new_content)
        content = new_content
      else:
        pass
  except Exception as e:
    print(f"[ERROR] {e}")
