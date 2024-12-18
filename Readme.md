# Automated Data Processing Script

## Overview
This project contains a Python script that automates the process of reading data from a CSV file, processing the data, and updating a SQLite database. The script is scheduled to run automatically using Windows Task Scheduler.

## Files
- `data_script.py`: The main script that reads, processes, and updates the data.
- `test_script.py`: A test script to ensure the main script works correctly.
- `data.csv`: Sample data file used for testing.
- `script.log`: Log file for recording any errors that occur during script execution.

## Requirements
- Python 3.x
- pandas
- sqlite3
- logging

## Installation
1. Install Python from the [official website](https://www.python.org/downloads/).
2. Install the required Python packages:
   ```sh
   pip install pandas
   ```

## Usage
1. Place the `data.csv` file on your desktop.
2. Update the path to the CSV file in `data_script.py`:
   ```python
   data = pd.read_csv('C:\\Users\\YourUsername\\Desktop\\data.csv')
   ```
3. Run the script manually to ensure it works:
   ```sh
   python data_script.py
   ```
4. Schedule the script using Windows Task Scheduler:
   - Open Task Scheduler and create a new task.
   - Set the trigger to the desired time.
   - Set the action to run your Python script, e.g., `python C:\path\to\data_script.py`.
   - Save the task.

## Testing
Run the test script to ensure the main script works correctly:
```sh
python test_script.py

