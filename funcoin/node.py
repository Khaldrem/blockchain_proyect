import asyncio

from lib.blockchain import Blockchain
from lib.connections import ConnectionPool
from lib.peers import P2PProtocol
from lib.server import Server

blockchain = Blockchain()
connection_pool = ConnectionPool

server = Server(blockchain, connection_pool, P2PProtocol)

async def main():
    await server.listen()

asyncio.run(main())
