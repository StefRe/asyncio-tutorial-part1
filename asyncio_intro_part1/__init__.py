"""Tutorial demonstrating asyncio coroutines and tasks."""
import asyncio
import inspect
import time

from logger import LOGGER

from asyncio_intro_part1.coroutines import simple_coroutine
from asyncio_intro_part1.tasks import create_tasks


async def init_script(start_time: float):
    """Script entry point."""
    await async_gather_example(start_time)
    await async_tasks_example(start_time)


async def async_gather_example(start_time: float):
    """
    Run a function three times concurrently.

    :param float start_time: Time at which the script began.
    """
    await asyncio.gather(
        simple_coroutine(1),
        simple_coroutine(2),
        simple_coroutine(3),
    )
    LOGGER.info(
        f"Executed {inspect.currentframe().f_code.co_name} in {time.perf_counter() - start_time:0.2f} seconds. \
        -----------------------------------------------------------------------------------------------------"
    )


async def async_tasks_example(start_time: float):
    """
    Create and inspect tasks to wrap simple functions.

    :param float start_time: Time at which the script began.
    """
    LOGGER.info(
        f"Executing function {inspect.currentframe().f_code.co_name} momentarily..."
    )
    time.sleep(2)
    tasks = await create_tasks(simple_coroutine)
    LOGGER.info(f"Tasks about to be executed:")
    for task in tasks:
        LOGGER.info(task)
    tasks = await asyncio.gather(*tasks)
    LOGGER.info(f"Remaining tasks: {tasks}")
    LOGGER.info(
        f"Executed {inspect.currentframe().f_code.co_name} in {time.perf_counter() - start_time:0.2f} seconds."
    )
