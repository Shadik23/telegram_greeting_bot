CREATE TABLE IF NOT EXISTS greetings (
    id SERIAL PRIMARY KEY,
    greeting_text TEXT NOT NULL DEFAULT 'Привет! Добро пожаловать!'
);

INSERT INTO greetings (greeting_text)
SELECT 'Привет! Добро пожаловать!'
WHERE NOT EXISTS (SELECT 1 FROM greetings WHERE id = 1);