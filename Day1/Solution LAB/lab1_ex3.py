from datetime import datetime

# define class
class CustomDate():
    
  def __init__(self):
    self.time = datetime.now()
  
  def get_date(self):
    return self.time.strftime("%d/%m/%Y")  # method 1
    # return f"{self.time.day:02d}/{self.time.month:02d}/{self.time.year:04d}"  # method 2
  
  def get_time(self):
    return self.time.strftime("%H:%M:%S")  # method 1
    # return f"{self.time.hour:02d}:{self.time.minute:02d}:{self.time.second:02d}"  # method 2


# driver code
now = CustomDate()
print(now.get_date())
print(now.get_time())