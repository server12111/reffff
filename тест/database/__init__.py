from sqlalchemy import text

from database.engine import engine
from database.models import Base


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        # Migration: add referral_reward_pending column to existing databases
        try:
            await conn.execute(
                text("ALTER TABLE users ADD COLUMN referral_reward_pending BOOLEAN NOT NULL DEFAULT 0")
            )
        except Exception:
            pass  # Column already exists


__all__ = ["init_db"]
