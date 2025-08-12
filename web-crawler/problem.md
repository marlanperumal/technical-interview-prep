# Web Crawler / Concurrent Downloader

- Problem: Write a function that takes a starting URL and a depth, and crawls the web, visiting links up to that depth. The crawling should be done concurrently to speed up the process.
- What it tests: Concurrency in Python (threading or asyncio), handling network requests, data structures for managing visited URLs (sets) and URLs to visit (queues), and understanding of potential issues like circular dependencies.
- Key concepts: Breadth-First Search (BFS), queues, sets for lookups, and Python's threading or asyncio libraries.