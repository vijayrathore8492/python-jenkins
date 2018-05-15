create table jobs (
    id INT PRIMARY KEY,
    name CHAR(100) NOT NULL,
    is_running INT NOT NULL,
    is_queued INT NOT NULL,
    is_enabled INT NOT NULL,
    timestamp INTEGER NOT NULL
)