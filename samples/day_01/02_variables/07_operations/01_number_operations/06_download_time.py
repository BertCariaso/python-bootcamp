speed = float(input("Download Speed (Mbps): "))
file_size = int(input("File Size (MB): "))

# MegaBytes per second (MBps) = 8 * Megabits per second (Mbps)
download_speed_MBps = None

# Download Time (seconds) = File Size (MB) / MegaBytes per second (MBps)
download_time_seconds = None

# Download Time (minutes) = Download Time (Seconds) / 60
download_time_minutes = None

print(download_time_minutes)