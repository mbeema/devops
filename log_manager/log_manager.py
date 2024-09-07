"""
Script Name: Log Archiver and Cleaner
Author: Madhukar Beema
Created: 2021-08-16
Last Modified: 2023-07-20
Version: 1.0.2
Description:
    This script archives and/or deletes log files and directories based on a provided configuration.
    The configuration specifies the paths, filters, number of days to keep, and actions for each log.

History:
    2021-08-16: Version 1.0.0
        - Initial version.
    2023-07-20: Version 1.0.1
        - Added support for directory handling.
        - Improved error handling.
    2023-07-21: Version 1.0.2
        - Individual archive directory for each log entry.
"""

import os
import json
import tarfile
import datetime
import glob
import smtplib
from email.mime.text import MIMEText
import argparse

def send_email(subject, message, config):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = config["sender_email"]
    msg['To'] = config["receiver_email"]

    try:
        with smtplib.SMTP(config["smtp_server"], config["smtp_port"]) as server:
            server.starttls()
            if config.get("password"):
                server.login(config["sender_email"], config["password"])
            server.sendmail(config["sender_email"], config["receiver_email"], msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def log_activity(message, log_file):
    with open(log_file, 'a') as file:
        file.write(f"{datetime.datetime.now()} - {message}\n")

def archive_log(source, archive_path, source_type):
    with tarfile.open(archive_path, "w:gz") as tar:
        if source_type == "file":
            tar.add(source, arcname=os.path.basename(source))
        elif source_type == "directory":
            for root, _, files in os.walk(source):
                for file in files:
                    tar.add(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file), source))
    print(f"Archived {source} to {archive_path}")

def delete_old_files(directory, file_filter, days_to_keep):
    now = datetime.datetime.now()
    for file in glob.glob(os.path.join(directory, file_filter)):
        file_creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file))
        delta = now - file_creation_date
        if delta.days > days_to_keep:
            os.remove(file)
            print(f"Deleted {file}")

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Log Archiver and Cleaner")
    parser.add_argument('--email', action='store_true', help="Send email notifications for activities")
    args = parser.parse_args()

    # Load the configuration
    with open("config.json", "r") as file:
        config = json.load(file)

    activity_messages = []

    current_date = datetime.datetime.now().strftime('%Y%m%d')

    for log_config in config["logs"]:
        source_type = log_config["type"]
        source_path = log_config["path"]
        file_filter = log_config["filter"]
        days_to_keep = log_config["days_to_keep"]
        action = log_config["action"]
        archive_dir = log_config.get("archive_directory", "")

        if not os.path.exists(archive_dir) and action == "archive":
            os.makedirs(archive_dir)

        if action == "archive":
            archive_name = os.path.join(archive_dir, f"{os.path.basename(source_path)}.{current_date}.tar.gz")
            archive_log(source_path, archive_name, source_type)
            activity_msg = f"Archived {source_path} to {archive_name}"
            activity_messages.append(activity_msg)
            log_activity(activity_msg, config["activity_log"])
        elif action == "delete":
            delete_old_files(source_path, file_filter, days_to_keep)
            activity_msg = f"Deleted files older than {days_to_keep} days from {source_path}"
            activity_messages.append(activity_msg)

    # Send email with all activities if --email switch is provided
    if args.email and activity_messages:
        send_email("Log Archiver and Cleaner Activity", "\n".join(activity_messages), config["email"])

if __name__ == "__main__":
    main()
