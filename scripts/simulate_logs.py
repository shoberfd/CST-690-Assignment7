import json
import random
import datetime as dt
from faker import Faker
import os

# initialize Faker and log parameters
fake = Faker()
LOG_COUNT = 500
BOT_NAMES = ["InvoiceProcessor", "ReportGenerator", "DataEntryBot", "UserOnboarding"]
STATUSES = ["SUCCESS", "SUCCESS", "SUCCESS", "ERROR", "SUCCESS", "TIMEOUT"]
ERROR_MESSAGES = [
    "API endpoint returned status 503",
    "Database connection timed out",
    "KeyError: 'TransactionID' not found in payload",
    "File not found: /data/source/report.csv",
    None
]

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)
log_file_path = f"logs/bot_activity_{dt.date.today()}.jsonl"

print(f"Generating {LOG_COUNT} log entries into {log_file_path}...")

# Generate and write log entries
with open(log_file_path, "w") as f:
    for i in range(LOG_COUNT):
        bot_name = random.choice(BOT_NAMES)
        status = random.choice(STATUSES)
        error = random.choice(ERROR_MESSAGES) if status in ["ERROR", "TIMEOUT"] else None
        log_entry = {
            "timestamp": fake.iso8601(),
            "level": "ERROR" if status == "ERROR" else "INFO",
            "bot_name": bot_name,
            "run_id": fake.uuid4(),
            "status": status,
            "duration_ms": random.randint(500, 30000) if status == "SUCCESS" else random.randint(30000, 60000),
            "records_processed": random.randint(1, 1000) if status == "SUCCESS" else 0,
            "error_message": error,
            "machine_name": f"prod-vm-{random.randint(1,4)}"
        }
        f.write(json.dumps(log_entry) + "\n")

print("Log simulation complete.")