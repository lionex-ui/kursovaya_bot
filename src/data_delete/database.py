from datetime import date

from sqlalchemy import delete, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import *


async def delete_child(
        child_id: int,
        session: AsyncSession
) -> None:

    stmt = delete(child).where(child.c.id == child_id)

    await session.execute(stmt)
    await session.commit()


async def delete_educator(
        educator_id: int,
        session: AsyncSession
) -> None:

    stmt = delete(educator).where(educator.c.id == educator_id)

    await session.execute(stmt)
    await session.commit()


async def delete_group(
        group_id: int,
        session: AsyncSession
) -> None:

    stmt = delete(child).where(child.c.group_id == group_id)
    await session.execute(stmt)

    stmt = delete(educator).where(educator.c.group_id == group_id)
    await session.execute(stmt)

    stmt = delete(group).where(group.c.id == group_id)
    await session.execute(stmt)

    await session.commit()


async def delete_old_children(
        session: AsyncSession
) -> None:

    stmt = delete(child).where(
        func.extract("year", child.c.birthday) <= date.today().year - 10
    )
    await session.execute(stmt)
    await session.commit()
