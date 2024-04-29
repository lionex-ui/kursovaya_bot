from datetime import datetime

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import *


async def update_child(
        child_id: int,
        group_id: int,
        first_name: str,
        last_name: str,
        sex: str,
        birthday: datetime,
        session: AsyncSession
) -> None:

    stmt = update(child).where(child.c.id == child_id).values(
        group_id=group_id,
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        birthday=birthday
    )

    await session.execute(stmt)
    await session.commit()


async def update_educator(
        educator_id: int,
        group_id: int,
        first_name: str,
        last_name: str,
        sex: str,
        birthday: datetime,
        session: AsyncSession
) -> None:

    stmt = update(educator).where(educator.c.id == educator_id).values(
        group_id=group_id,
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        birthday=birthday
    )

    await session.execute(stmt)
    await session.commit()


async def update_group(
        group_id: int,
        name: str,
        session: AsyncSession
) -> None:

    stmt = update(group).where(group.c.id == group_id).values(
        name=name
    )

    await session.execute(stmt)
    await session.commit()
