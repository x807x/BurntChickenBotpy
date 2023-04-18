from enum import Enum
class Day(Enum):
    Sunday=["Sunday"]
    Monday=["Monday"]
    Tuesday=["Tuesday"]
    Wednesday=["Wednesday"]
    Thursday=["Thursday"]
    Friday=["Friday"]
    Saturday=["Saturday"]
    Weekday=Monday+Tuesday+Wednesday+Thursday+Friday
    Weekend=Sunday+Saturday
    Everyday=Sunday+Monday+Tuesday+Wednesday+Thursday+Friday+Saturday