from dataclasses import dataclass, field


@dataclass
class DBConfig:
    dbms: str
    driver: str
    db_name: str
    user: str
    password: str
    host: str
    port: int
