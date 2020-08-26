from pyrogram import filters
from tagadmin import OWNER_ID


def f_owner_filter(_, __, m):
    return bool(m.from_user.id == OWNER_ID)


owner_filter = filters.create(f_owner_filter)
