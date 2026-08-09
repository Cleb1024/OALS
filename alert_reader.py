log_path = "alert.log"

with open(log_path, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        print(line.strip())