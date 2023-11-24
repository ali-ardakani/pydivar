import asyncio
from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientConnectorError, ServerDisconnectedError



import abc
from typing import Any, Protocol

class PostDetailProvider(Protocol):
    """
    A protocol defining the interface for getting post details.

    This protocol should be implemented by classes that provide the functionality
    to retrieve post details using a token, session, and semaphore.

    Attributes:
        token (str): The authentication token.
        session (ClientSession): The session object for making HTTP requests.
        semaphore (asyncio.Semaphore): The semaphore for controlling concurrent access.

    Returns:
        Any: The post details.

    """

    @abc.abstractmethod
    async def get_detail(self, token: str, session: ClientSession, semaphore: asyncio.Semaphore) -> Any:
        pass
    
class DefaultPostDetailProvider(PostDetailProvider):
    """
    Default implementation of the PostDetailProvider interface.
    Retrieves post details from the Divar API using the provided token.
    """

    BASE_URL = "https://api.divar.ir/v8/posts-v2/web/{token}"
    MAX_RETRY = 3

    async def get_detail(self, token: str, session: ClientSession, semaphore: asyncio.Semaphore) -> Any:
        """
        Retrieves the detail of a post using the given token.

        Args:
            token (str): The token of the post.
            session (ClientSession): The aiohttp ClientSession object for making HTTP requests.
            semaphore (asyncio.Semaphore): The semaphore for limiting concurrent requests.

        Returns:
            Any: The JSON response containing the post detail, or None if the post is not found.

        Raises:
            ClientConnectorError: If there is an error connecting to the server.
            ServerDisconnectedError: If the server disconnects unexpectedly.
        """
        async with semaphore:
            for retry in range(3):
                try:
                    async with session.get(self.BASE_URL.format(token=token)) as response:
                        if response.status == 200:
                            print(f"Get detail of {token}")
                            return await response.json()
                        elif response.status == 404:
                            print(f"Token {token} not found")
                            return None
                        else:
                            print(f"Status code {response.status} for token {token}")
                            await asyncio.sleep(5)
                            return await self.get_detail(token, session, semaphore)
                except ClientConnectorError as e:
                    if retry < self.MAX_RETRY:
                        await asyncio.sleep(5)
                        continue
                    raise e
                except ServerDisconnectedError as e:
                    if retry < self.MAX_RETRY:
                        await asyncio.sleep(10)
                        continue
                    raise e
        
class PostDetailService:
    """
    A service class for retrieving post details.

    Args:
        provider (PostDetailProvider): The provider for retrieving post details. Defaults to DefaultPostDetailProvider().

    Methods:
        get_post_details: Retrieves the details of multiple or a single post concurrently.

    """

    def __init__(self, provider: PostDetailProvider = DefaultPostDetailProvider()):
        self.provider = provider
    
    async def _get_post_detail(self, token: str, semaphore: asyncio.Semaphore):
        async with ClientSession() as session:
            return await self.provider.get_detail(token, session, semaphore)
    
    def get_post_details(self, token: str | list, maximum_task: int = 5):
        """
        Retrieves the details of multiple or a single post concurrently.
        
        Args:
            token (str | list): The token(s) of the post(s). Can be a single token or a list of tokens.
            maximum_task (int): The maximum number of concurrent tasks. Defaults to 5.

        Returns:
            list: The details of the posts.

        """
        if isinstance(token, str):
            token = [token]

        loop = asyncio.get_event_loop()
        ads = []
        semaphore = asyncio.Semaphore(maximum_task)
        tasks = [self._get_post_detail(t, semaphore) for t in token]
        ads = loop.run_until_complete(asyncio.gather(*tasks))
        return ads
