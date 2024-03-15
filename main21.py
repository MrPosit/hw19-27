import time
import aiohttp
import asyncio


async def get_data_async(url, session, i):
    async with session.get(url) as response:
        return await response.text()


async def paralell():
    async with aiohttp.ClientSession() as session:
        events = [get_data_async(f"https://jsonplaceholder.typicode.com/comments/{i}", session, i) for i in range(1,101)]
        result = await asyncio.gather(*events)
        for index, data in enumerate(result):
            with open (f"data_{index+1}.json", "w") as file:
                file.write(data)


start= time.time()
if __name__ == "__main__":
    asyncio.run(paralell())
end= time.time()

print("time Elapsed: "+ str(end-start))