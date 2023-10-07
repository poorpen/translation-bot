from dataclasses import dataclass



@dataclass(frozen=True)
class AddUser:
    username: str
    first_name: str
    last_name: str
