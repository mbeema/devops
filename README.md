# Log Archiver and Cleaner

This script provides functionality to archive and/or delete log files and directories based on a provided configuration.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contribution](#contribution)
- [License](#license)
- [Author](#author)

## Features

- Archive log files and directories.
- Delete old log files based on a specified retention period.
- Flexible configuration using a JSON file.
- Optional email notifications for activities.

## Requirements

- Python 3.x
- A JSON configuration file named `config.json` in the same directory.

## Installation

1. Clone the repository or download the script and configuration file.
2. Ensure you have Python 3.x installed.
3. Modify the `config.json` file to suit your needs.

## Usage

Run the script without sending emails:

```bash
python log_manager.py
python log_manager.py --email

