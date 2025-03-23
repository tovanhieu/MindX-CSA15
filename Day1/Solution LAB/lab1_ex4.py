# define class
class DateHandler():
    
  def __init__(self):
    pass
  
  @classmethod
  def format_date(cls, time):
    return time.strftime("%d/%m/%Y")

  @classmethod
  def get_days_between(cls, time_start, time_end):
    return (time_end - time_start).days


# driver code
from datetime import datetime

start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)

print("Start:", DateHandler.format_date(start_date))
print("End:", DateHandler.format_date(end_date))
print("Days between:",
       DateHandler.get_days_between(start_date, end_date))