

from datetime import datetime

now = datetime.now()

report_date = now.strftime("%B %d, %Y ")
filename_date = now.strftime("%Y-%m-%d")
log_timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

print(
    f"\nReport date: {report_date}\n"
    f"Filename date: {filename_date}\n"
    f"Log timestamp: {log_timestamp}\n"
)


#   Code	Meaning         Example
#   %Y    Four-digit year	 2026
#   %m	  Month number	      10
#   %d    Day number	      11
#   %B	  Full month name	October
#   %H    24-hour hour	      22
#   %M    Minute	          49
#   %S    Second              31

