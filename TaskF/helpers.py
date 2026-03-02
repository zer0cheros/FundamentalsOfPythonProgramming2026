import pathlib
from datetime import date, datetime
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



def format_date(d: date) -> str:
    """Formats a date as dd.mm.yyyy."""
    return f"{d.day:02d}.{d.month:02d}.{d.year}"


def format_number(value: float) -> str:
    """Formats a float with two decimals and a comma decimal separator."""
    return f"{value:.2f}".replace(".", ",")


def month_name(month: int) -> str:
    """Returns the English month name for 1–12."""
    names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    return names[month - 1]


def parse_timestamp(ts: str) -> datetime:
    """Parses an ISO timestamp (e.g. 2025-10-13T00:00:00) into a datetime."""
    return datetime.fromisoformat(ts)
