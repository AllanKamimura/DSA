from random import randint


class Codec:
    url_map = {}

    charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    num = 6

    def get_random(self) -> int:
        return randint(0, len(self.charset) - 1)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        shortUrl = ""
        for i in range(self.num):
            shortUrl += self.charset[self.get_random()]

        self.url_map[shortUrl] = longUrl

        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.url_map[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
