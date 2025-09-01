import logging
import asyncio
import asyncpg
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from config import WebConfig
from schemas import GreetingUpdate, GreetingResponse
import secrets


app = FastAPI(title="Greeting Bot Admin Panel")
security = HTTPBasic()

logging.basicConfig(level=logging.INFO)

db_pool = None


async def get_db_pool():
    global db_pool
    if db_pool is None:
        for i in range(5): 
            try:
                logging.info(f"Attempting to connect to DB (try {i+1}/5)...")
                db_pool = await asyncpg.create_pool(WebConfig.get_db_url())
                logging.info("DB pool created successfully.")
                break 
            except (ConnectionRefusedError, asyncpg.exceptions.InvalidPasswordError) as e:
                logging.warning(f"DB connection failed: {e}. Retrying in 3 seconds...")
                if i == 4: 
                    raise
                await asyncio.sleep(3) 
    return db_pool


async def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, WebConfig.WEB_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, WebConfig.WEB_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.on_event("startup")
async def startup_event():
    await get_db_pool()
    logging.info("Web service started and DB pool initialized.")


@app.on_event("shutdown")
async def shutdown_event():
    global db_pool
    if db_pool:
        await db_pool.close()
        logging.info("DB pool closed.")


@app.get("/", response_model=GreetingResponse)
async def get_greeting_text(username: str = Depends(get_current_username)):
    pool = await get_db_pool()
    async with pool.acquire() as conn:
        row = await conn.fetchrow("SELECT greeting_text FROM greetings ORDER BY id LIMIT 1")
        if row:
            return GreetingResponse(current_greeting_text=row['greeting_text'])
        else:
            return GreetingResponse(current_greeting_text="Привет! Добро пожаловать!")


@app.post("/update_greeting", response_model=GreetingResponse)
async def update_greeting_text(
    greeting_update: GreetingUpdate,
    username: str = Depends(get_current_username)
):
    pool = await get_db_pool()
    async with pool.acquire() as conn:
        existing_greeting = await conn.fetchrow("SELECT id FROM greetings WHERE id = 1")

        if existing_greeting:
            await conn.execute(
                "UPDATE greetings SET greeting_text = $1 WHERE id = 1",
                greeting_update.new_greeting_text
            )
        else:
            await conn.execute(
                "INSERT INTO greetings (id, greeting_text) VALUES (1, $1)",
                greeting_update.new_greeting_text
            )
        logging.info(f"Greeting updated to: {greeting_update.new_greeting_text}")
        return GreetingResponse(current_greeting_text=greeting_update.new_greeting_text)
    