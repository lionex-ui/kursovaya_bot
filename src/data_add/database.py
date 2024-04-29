from datetime import datetime

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import *


async def insert_child(
        group_id: int,
        first_name: str,
        last_name: str,
        sex: str,
        birthday: datetime,
        session: AsyncSession
) -> None:

    stmt = insert(child).values(
        group_id=group_id,
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        birthday=birthday
    )

    await session.execute(stmt)
    await session.commit()


async def insert_educator(
        group_id: int,
        first_name: str,
        last_name: str,
        sex: str,
        birthday: datetime,
        session: AsyncSession
) -> None:

    stmt = insert(educator).values(
        group_id=group_id,
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        birthday=birthday
    )

    await session.execute(stmt)
    await session.commit()


async def insert_group(
        name: str,
        session: AsyncSession
) -> None:

    stmt = insert(group).values(
        name=name
    )

    await session.execute(stmt)
    await session.commit()
