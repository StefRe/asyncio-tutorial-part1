"""Create a coroutine function to be executed as asyncio task."""
import asyncio

from logger import LOGGER


async def simple_coroutine(number: int):
    """
    Wait for a time delay & display number associated with coroutine.

    :param int number: Number to identify the current coroutine.
    """
    await asyncio.sleep(1)
    LOGGER.info(f"Coroutine {number} has finished executing.")
