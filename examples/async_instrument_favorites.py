import asyncio
import os

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import (
    CreateFavoriteGroupRequest,
    DeleteFavoriteGroupRequest,
    EditFavoritesActionType as At,
    EditFavoritesRequestInstrument,
    GetFavoriteGroupsRequest,
)

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        r = await client.instruments.get_favorites()

        print("Список избранных инструментов:")
        for i in r.favorite_instruments:
            print(f"{i.ticker} - {i.name}")

        request = CreateFavoriteGroupRequest()
        request.group_name = "My test favorite group"
        request.group_color = "aa0000"  # red color
        r = await client.instruments.create_favorite_group(request=request)
        group_id = r.group_id
        print(f"Создана новая группа избранного с ИД: {group_id}")

        await client.instruments.edit_favorites(
            instruments=[EditFavoritesRequestInstrument(instrument_id="BBG001M2SC01")],
            action_type=At.EDIT_FAVORITES_ACTION_TYPE_ADD,
            group_id=group_id,
        )

        request = GetFavoriteGroupsRequest()
        request.instrument_id = ["BBG001M2SC01"]
        r = await client.instruments.get_favorite_groups(request=request)
        print(f"Список групп избранного:")
        for i in r.groups:
            print(
                f"{i.group_id} - {i.group_name}. Количество элементов: {i.size}. "
                f"Содержит выбранный инструмент {request.instrument_id[0]}: "
                f"{i.contains_instrument} "
            )

        request = DeleteFavoriteGroupRequest()
        request.group_id = group_id
        await client.instruments.delete_favorite_group(request=request)
        print(f"Удалена группа избранного с ИД: {group_id}")


if __name__ == "__main__":
    asyncio.run(main())
