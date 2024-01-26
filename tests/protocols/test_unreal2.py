import pytest
from opengsq.protocols.unreal2 import Unreal2

from ..result_handler import ResultHandler

handler = ResultHandler(__file__)
# handler.enable_save = True

# Killing Floor
test = Unreal2(host="51.195.117.236", port=9981)


@pytest.mark.asyncio
async def test_get_details():
    result = await test.get_details()
    await handler.save_result("test_get_details", result)


@pytest.mark.asyncio
async def test_get_rules():
    result = await test.get_rules()
    await handler.save_result("test_get_rules", result)


@pytest.mark.asyncio
async def test_get_players():
    result = await test.get_players()
    await handler.save_result("test_get_players", result)
