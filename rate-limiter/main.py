import functools
from typing import Callable
import asyncio

queue: int = 0


def rate_limit(rpm: int) -> Callable:
    def decorator_rate_limit(func: Callable):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            global queue
            if queue >= rpm:
                return False

            else:
                queue += 1
            return await func(*args, **kwargs)

        return wrapper

    return decorator_rate_limit


@rate_limit(rpm=10)
async def say_hello():
    print("hello")


async def main():
    tasks = [asyncio.create_task(say_hello()) for _ in range(20)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
