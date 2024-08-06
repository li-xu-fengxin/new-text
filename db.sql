CREATE TABLE IF NOT EXISTS sensor_info(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_address TEXT,
    sensor_type TEXT,
    row_command TEXT,
    upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data TEXT
);