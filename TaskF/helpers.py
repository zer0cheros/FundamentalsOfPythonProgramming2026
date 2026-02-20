import pathlib

mainMenu = [
    {"id": 1, "content": "Daily summary for a date range"},
    {"id": 2, "content": "Monthly summary for one month"},
    {"id": 3, "content": "Full year 2025"},
    {"id": 4, "content": "Exit"},
]

underHeaders = [
    {"id": 1, "content": "Write the report to the file report.txt"},
    {"id": 2, "content": "Create a new report"},
    {"id": 3,"content": "Exit"}
]

path = pathlib.Path(__file__).parent

months = [
    {"id": 1, "content": "January"},
    {"id": 2, "content": "February"},
    {"id": 3, "content": "March"},
    {"id": 4, "content": "April"},
    {"id": 5, "content": "May"},
    {"id": 6, "content": "June"},
    {"id": 7, "content": "July"},
    {"id": 8, "content": "August"},
    {"id": 9, "content": "September"},
    {"id": 10, "content": "October"},
    {"id": 11, "content": "November"},
    {"id": 12, "content": "December"}
]

DATE_COL = "Time"
AMOUNT_COL = " Consumption (net) kWh"
PRODUCT_COL = " Production (net) kWh"
AVERAGE_TEMP = " Daily average temperature"