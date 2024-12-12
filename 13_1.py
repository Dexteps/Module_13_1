import  asyncio
async def start_strongman(name: str, power: int) -> None:
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        print(f'Силач {name} поднял шар номер {i}')
        await asyncio.sleep(1 / power)
    print(f'Силач {name} закончил соревнования')


async def main():
    task1 = asyncio.create_task(start_strongman('Андрей',3))
    task2 = asyncio.create_task(start_strongman('Петя', 4))
    task3 = asyncio.create_task(start_strongman('Иван', 5))
    await task1
    await task2
    await task3



if __name__ == '__main__':
    asyncio.run(main())
