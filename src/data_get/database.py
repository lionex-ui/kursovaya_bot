from typing import Optional

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import *


async def get_children(
        session: AsyncSession
) -> list:

    query = select(child)

    data = await session.execute(query)

    return list(data.all())


async def get_child_by_id(
        child_id: int,
        session: AsyncSession
) -> Optional[tuple]:

    query = select(child).where(child.c.id == child_id)

    data = await session.execute(query)

    return data.first()


async def get_most_frequent_child_name(
        session: AsyncSession
) -> Optional[tuple]:

    query = select(
        child.c.first_name,
        func.count()
    ).select_from(child).group_by(child.c.first_name).order_by(func.count().desc()).limit(1)

    data = await session.execute(query)

    return data.first()


async def get_avg_child_age(
        group_id: int,
        session: AsyncSession
) -> int:

    query = select(
        func.avg(
            func.date_part("year", func.current_date()) - func.date_part("year", child.c.birthday)
        )
    ).select_from(
        child
    ).where(
        child.c.group_id == group_id
    )

    data = await session.execute(query)

    return round(data.scalar())


async def group_children_by_year(
        session: AsyncSession
) -> list:

    query = select(
        func.extract("year", child.c.birthday),
        func.count(),
        func.array_agg(child.c.id)
    ).select_from(
        child
    ).group_by(
        func.extract("year", child.c.birthday)
    ).order_by(
        func.extract("year", child.c.birthday)
    )

    data = await session.execute(query)

    return list(data.all())


async def get_educator(
        session: AsyncSession
) -> list:

    query = select(educator)

    data = await session.execute(query)

    return list(data.all())


async def get_educator_by_id(
        educator_id: int,
        session: AsyncSession
) -> Optional[tuple]:

    query = select(educator).where(educator.c.id == educator_id)

    data = await session.execute(query)

    return data.first()


async def get_most_frequent_educator_name(
        session: AsyncSession
) -> Optional[tuple]:

    query = select(
        educator.c.first_name,
        func.count()
    ).select_from(educator).group_by(educator.c.first_name).order_by(func.count().desc()).limit(1)

    data = await session.execute(query)

    return data.first()


async def get_avg_educator_age(
        session: AsyncSession
) -> int:

    query = select(
        func.avg(
            func.date_part("year", func.current_date()) - func.date_part("year", educator.c.birthday)
        )
    ).select_from(
        educator
    )

    data = await session.execute(query)

    return round(data.scalar())


async def group_educator_by_year(
        session: AsyncSession
) -> list:

    query = select(
        func.extract("year", educator.c.birthday),
        func.count(),
        func.array_agg(educator.c.id)
    ).select_from(
        educator
    ).group_by(
        func.extract("year", educator.c.birthday)
    ).order_by(
        func.extract("year", educator.c.birthday)
    )

    data = await session.execute(query)

    return list(data.all())


async def get_groups(
        session: AsyncSession
) -> list:

    query = select(
        group.c.id,
        group.c.name,
        func.concat(educator.c.first_name, " ", educator.c.last_name),
        func.count(child.c.id)
    ).select_from(
        group
    ).join(
        educator, group.c.id == educator.c.group_id
    ).join(
        child, group.c.id == child.c.group_id
    ).group_by(
        group.c.id,
        group.c.name,
        educator.c.first_name,
        educator.c.last_name
    ).order_by(
        group.c.id.asc()
    )

    data = await session.execute(query)

    return list(data.all())
