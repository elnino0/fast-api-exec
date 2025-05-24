import asyncio
import aiohttp

async def login(url: str, username: str, password: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, json={"email": username, "password": password}) as response:
                if response.status == 200:
                    data = await response.text()  # Or response.json() for JSON
                    return data
                else:
                    print(f"Request failed with status: {response.status}")
                    return None
        except aiohttp.ClientError as e:
            print(f"An error occurred: {e}")
            return None

async def main():
    urls = [
        "http://localhost:8000/auth/login",
    ]
    tasks = [login(url,"fatJohn.com","password") for url in urls]
    results = await asyncio.gather(*tasks)

    for i, result in enumerate(results):
        print(f"Result from {urls[i]}: {result[:50]}..." if result else f"Failed to fetch {urls[i]}")

if __name__ == "__main__":
    asyncio.run(main())