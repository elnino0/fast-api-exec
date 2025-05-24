import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from a .env file (if it exists)
load_dotenv()

# Print all environment variables (similar to console.log("env: ", process.env) in JS)
print("env:", os.environ)

class ENV:
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    POSTGRES_PORT: Optional[int]
    POSTGRES_URI: Optional[str]
    POSTGRES_USER: Optional[str]
    POSTGRES_USER_PASS: Optional[str]
    POSTGRESS_DATABASE: Optional[str]
    APP_PORT: Optional[int]
    JWT_SECRECT: Optional[str]
    ALGORITHM: Optional[str]
    EXPIRES_IN: Optional[int]

class Config:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        
    POSTGRES_PORT: int
    POSTGRES_URI: str
    POSTGRES_USER: str
    POSTGRES_USER_PASS: str
    POSTGRESS_DATABASE: str
    APP_PORT: int
    JWT_SECRECT: str
    ALGORITHM: str
    EXPIRES_IN: int

def get_config() -> ENV:
    app_port_str = os.environ.get("APP_PORT")
    app_port = int(app_port_str) if app_port_str else 3000

    return ENV(
        POSTGRES_PORT=int(os.environ.get("POSTGRES_PORT", "5432")),
        POSTGRES_URI=os.environ.get("POSTGRES_URI", "localhost"),
        POSTGRES_USER=os.environ.get("POSTGRES_USER", "your_user"),
        POSTGRES_USER_PASS=os.environ.get("POSTGRES_USER_PASS", "your_password"),
        POSTGRESS_DATABASE=os.environ.get("POSTGRESS_DATABASE", "fat_db"),
        APP_PORT=app_port,
        JWT_SECRECT=os.environ.get("JWT_SECRECT", "supersecrectssh"),
        ALGORITHM=os.environ.get("ALGORITHM", "HS256"),
        EXPIRES_IN=int(os.environ.get("EXPIRES_IN", "15")),
    )

def get_sanitized_config(config: ENV) -> Config:
    sanitized_config = {}
    for key, value in config.__dict__.items():
        if value is None:
            raise ValueError(f"Missing key {key} in .env file")
        sanitized_config[key] = value
    return Config(**sanitized_config)

config_env = get_config()
AppConfig = get_sanitized_config(config_env)
