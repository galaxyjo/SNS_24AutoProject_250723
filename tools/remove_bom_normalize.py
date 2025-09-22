import pathlib

root = pathlib.Path(r"C:\SNS_24AutoProject_250723")
log = []

for f in root.rglob("*.py"):
    if f.stat().st_size < 50:
        continue
    try:
        data = f.read_bytes()
        text = data.decode("utf-8-sig").replace("\r\n", "\n")
        f.write_text(text, encoding="utf-8")
        log.append(f"OK\t{f}")
    except Exception as e:
        log.append(f"ERR\t{f}\t{e}")

with open(
    r"C:\SNS_24AutoProject_250723\encoding_clean_log_0804.txt", "w", encoding="utf-8"
) as f:
    f.write("\n".join(log))
