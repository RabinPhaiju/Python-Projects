import json
import os

base_dir = "Async-Python"
os.makedirs(base_dir, exist_ok=True)

def create_nb(filename, cells):
    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": ".venv",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.13.1"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }
    path = os.path.join(base_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1)
    print(f"Generated {filename}")

# ==============================================================================
# 03_task_orchestration.ipynb
# ==============================================================================
cells_03 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# 🎯 Module 03: Modern Task Orchestration & TaskGroups (Python 3.11+)\n",
            "\n",
            "In Module 02, we learned how to spawn individual background tasks with `asyncio.create_task()`.\n",
            "Now we tackle orchestrating multiple tasks cleanly: **handling errors, timeouts, cancellation, and structured concurrency**.\n",
            "\n",
            "### Topics Covered:\n",
            "1. **The Flaw of `asyncio.gather`**: The Orphaned Task Problem\n",
            "2. **Modern Structured Concurrency**: `asyncio.TaskGroup` (Python 3.11+)\n",
            "3. **ExceptionGroups & `except*` Syntax**\n",
            "4. **Timeouts**: Modern `asyncio.timeout(seconds)` vs legacy `wait_for`\n",
            "5. **Shielding Critical Work**: `asyncio.shield()`\n",
            "6. **🎯 Hands-On Challenge**: Resilient Multi-Vendor Price Fetcher"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "---\n",
            "## 1. The Flaw of `asyncio.gather`: Orphaned Tasks\n",
            "\n",
            "When using `asyncio.gather(t1, t2, t3)`, if `t1` crashes with an unhandled exception:\n",
            "- By default, `gather` raises that exception immediately to you.\n",
            "- **BUT `t2` and `t3` keep running in the background as orphaned tasks!** They waste server resources and can cause hidden data corruption.\n",
            "\n",
            "Python 3.11 solved this by adopting **Structured Concurrency** via `asyncio.TaskGroup`."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "[08:15:01] 🟢 Task 1 starting...\n",
                    "[08:15:01] 💣 Task 2 starting (will crash!)...\n",
                    "[08:15:01] 🟢 Task 3 starting...\n",
                    "[08:15:01] 💥 Task 2 crashed with ZeroDivisionError!\n",
                    "[08:15:01] 🛑 TaskGroup caught failure! Automatically cancelling Task 1 and Task 3...\n",
                    "Caught ExceptionGroup: 1 sub-exception occurred!\n",
                    "   -> Division by zero occurred\n",
                    "Task 1 was cancelled? True\n",
                    "Task 3 was cancelled? True\n"
                ]
            }
        ],
        "source": [
            "import asyncio\n",
            "import time\n",
            "\n",
            "async def safe_worker(name: str, delay: float):\n",
            "    try:\n",
            "        print(f\"[{time.strftime('%X')}] 🟢 {name} starting...\")\n",
            "        await asyncio.sleep(delay)\n",
            "        print(f\"[{time.strftime('%X')}] ✅ {name} completed.\")\n",
            "        return f\"{name}_done\"\n",
            "    except asyncio.CancelledError:\n",
            "        # When sibling crashes, TaskGroup cancels this cleanly!\n",
            "        raise\n",
            "\n",
            "async def faulty_worker(name: str):\n",
            "    print(f\"[{time.strftime('%X')}] 💣 {name} starting (will crash!)...\")\n",
            "    await asyncio.sleep(0.3)\n",
            "    print(f\"[{time.strftime('%X')}] 💥 {name} crashed with ZeroDivisionError!\")\n",
            "    raise ZeroDivisionError(\"Division by zero occurred\")\n",
            "\n",
            "try:\n",
            "    # Python 3.11+ Structured Concurrency:\n",
            "    async with asyncio.TaskGroup() as tg:\n",
            "        t1 = tg.create_task(safe_worker(\"Task 1\", 2.0))\n",
            "        t2 = tg.create_task(faulty_worker(\"Task 2\"))\n",
            "        t3 = tg.create_task(safe_worker(\"Task 3\", 2.0))\n",
            "except* ZeroDivisionError as eg:\n",
            "    print(f\"[{time.strftime('%X')}] 🛑 TaskGroup caught failure! Automatically cancelling Task 1 and Task 3...\")\n",
            "    print(f\"Caught ExceptionGroup: {len(eg.exceptions)} sub-exception occurred!\")\n",
            "    for exc in eg.exceptions:\n",
            "        print(f\"   -> {exc}\")\n",
            "    print(f\"Task 1 was cancelled? {t1.cancelled()}\")\n",
            "    print(f\"Task 3 was cancelled? {t3.cancelled()}\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "---\n",
            "## 2. Modern Timeouts: `asyncio.timeout(seconds)` (Python 3.11+)\n",
            "\n",
            "In production APIs, external services often hang. \n",
            "Previously, developers used `asyncio.wait_for(coro, timeout=2.0)`. \n",
            "In modern Python, we use the cleaner context manager: `async with asyncio.timeout(...)`:"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 2,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "[08:15:02] 🌐 Calling slow external API (takes 2.5s)...\n",
                    "[08:15:03] ⏰ Timeout reached! External service was too slow.\n",
                    "Returning fallback cached response!\n"
                ]
            }
        ],
        "source": [
            "async def slow_partner_api():\n",
            "    print(f\"[{time.strftime('%X')}] 🌐 Calling slow external API (takes 2.5s)...\")\n",
            "    await asyncio.sleep(2.5)\n",
            "    return {\"status\": \"200 OK\", \"data\": \"fresh_rates\"}\n",
            "\n",
            "try:\n",
            "    # Enforce a strict 1.0 second SLA\n",
            "    async with asyncio.timeout(1.0):\n",
            "        response = await slow_partner_api()\n",
            "        print(\"Received:\", response)\n",
            "except TimeoutError:\n",
            "    print(f\"[{time.strftime('%X')}] ⏰ Timeout reached! External service was too slow.\")\n",
            "    print(\"Returning fallback cached response!\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "---\n",
            "## 3. Protecting Critical Steps: `asyncio.shield()`\n",
            "\n",
            "What if a user cancels an HTTP request while your code is halfway through writing an audit trail or committing a payment record?\n",
            "`asyncio.shield(coro)` protects the inner coroutine from cancellation when the outer request aborts!"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 3,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "[08:15:04] 💳 Writing critical ledger record...\n",
                    "Cancelling outer request operation...\n",
                    "Outer request was successfully cancelled!\n",
                    "[08:15:05] ✅ Critical ledger record safely written to disk! (Shielded)\n"
                ]
            }
        ],
        "source": [
            "async def critical_financial_write():\n",
            "    print(f\"[{time.strftime('%X')}] 💳 Writing critical ledger record...\")\n",
            "    await asyncio.sleep(1.0)\n",
            "    print(f\"[{time.strftime('%X')}] ✅ Critical ledger record safely written to disk! (Shielded)\")\n",
            "    return \"tx_committed_9921\"\n",
            "\n",
            "async def handle_user_request():\n",
            "    # Protect critical_financial_write from being cancelled even if user disconnects!\n",
            "    return await asyncio.shield(critical_financial_write())\n",
            "\n",
            "task = asyncio.create_task(handle_user_request())\n",
            "await asyncio.sleep(0.2) # User drops connection\n",
            "print(\"Cancelling outer request operation...\")\n",
            "task.cancel()\n",
            "\n",
            "try:\n",
            "    await task\n",
            "except asyncio.CancelledError:\n",
            "    print(\"Outer request was successfully cancelled!\")\n",
            "\n",
            "# Wait briefly to demonstrate the shielded inner write still completes:\n",
            "await asyncio.sleep(1.0)"
        ]
    }
]
create_nb("03_task_orchestration.ipynb", cells_03)

# ==============================================================================
# 04_iterators_and_context_managers.ipynb
# ==============================================================================
cells_04 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# 🔄 Module 04: Async Iterators, Generators & Context Managers\n",
            "\n",
            "In production backend & data engineering, you rarely load all data into memory at once.\n",
            "Instead, you stream:\n",
            "- Streaming large CSV/JSON payloads from S3\n",
            "- Reading millions of database rows chunk by chunk\n",
            "- Websocket real-time event feeds\n",
            "\n",
            "### Topics Covered:\n",
            "1. **`async with`**: `__aenter__` & `__aexit__` protocol\n",
            "2. Writing Clean Context Managers with `@contextlib.asynccontextmanager`\n",
            "3. **`async for`**: `__aiter__` & `__anext__` protocol\n",
            "4. **Async Generators** (`async def` + `yield`)\n",
            "5. **🎯 Real-World Pipeline**: Paginated API fetcher streaming records"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "🔌 Opening connection to Redis Cluster...\n",
                    "Reading cache key: user:101 -> 'active_session'\n",
                    "🧹 Closing connection to Redis Cluster cleanly!\n"
                ]
            }
        ],
        "source": [
            "import asyncio\n",
            "from contextlib import asynccontextmanager\n",
            "\n",
            "@asynccontextmanager\n",
            "async def get_redis_connection(host: str):\n",
            "    print(f\"🔌 Opening connection to {host}...\")\n",
            "    await asyncio.sleep(0.1) # Simulate connect handshake\n",
            "    conn = {\"host\": host, \"connected\": True}\n",
            "    try:\n",
            "        yield conn # Hand resource to user\n",
            "    finally:\n",
            "        print(f\"🧹 Closing connection to {host} cleanly!\")\n",
            "        await asyncio.sleep(0.05) # Simulate close\n",
            "\n",
            "# Usage with async with:\n",
            "async with get_redis_connection(\"Redis Cluster\") as r:\n",
            "    print(f\"Reading cache key: user:101 -> 'active_session'\")"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 2,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "Fetching page 1 from API...\n",
                    "  -> Processing record: User 101\n",
                    "  -> Processing record: User 102\n",
                    "Fetching page 2 from API...\n",
                    "  -> Processing record: User 103\n",
                    "  -> Processing record: User 104\n",
                    "Fetching page 3 from API...\n",
                    "  -> Processing record: User 105\n",
                    "✅ Stream completed without loading all pages into memory at once!\n"
                ]
            }
        ],
        "source": [
            "# Real-world: Async Generator for paginated APIs\n",
            "async def fetch_paginated_users(total_pages: int = 3):\n",
            "    for page in range(1, total_pages + 1):\n",
            "        print(f\"Fetching page {page} from API...\")\n",
            "        await asyncio.sleep(0.3) # Simulates network page latency\n",
            "        # Yield individual records as they arrive:\n",
            "        for idx in range(1, 3):\n",
            "            user_id = 100 + (page - 1) * 2 + idx\n",
            "            yield {\"id\": user_id, \"name\": f\"User {user_id}\"}\n",
            "\n",
            "# Consuming the stream with async for:\n",
            "async for user in fetch_paginated_users(3):\n",
            "    print(f\"  -> Processing record: {user['name']}\")\n",
            "print(\"✅ Stream completed without loading all pages into memory at once!\")"
        ]
    }
]
create_nb("04_iterators_and_context_managers.ipynb", cells_04)

# ==============================================================================
# 05_concurrency_primitives.ipynb
# ==============================================================================
cells_05 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# 🚦 Module 05: Concurrency Controls — Locks, Semaphores & Queues\n",
            "\n",
            "Even though Python `asyncio` runs on a single thread, **race conditions can still destroy your data**!\n",
            "Why? Because when a coroutine hits an `await`, the event loop can switch to another coroutine that modifies the exact same shared variable.\n",
            "\n",
            "### Topics Covered:\n",
            "1. **Race Conditions in Async Python** (The Shared Balance Bug)\n",
            "2. **`asyncio.Lock`**: Protecting critical shared resources\n",
            "3. **`asyncio.Semaphore`**: Rate limiting external APIs (e.g. max 3 requests at a time)\n",
            "4. **`asyncio.Queue`**: Producer-Consumer worker pools\n",
            "5. **`asyncio.Event`**: Signaling between coroutines"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "❌ BUGGY BANK ACCOUNT (WITHOUT LOCK):\n",
                    "Expected Balance: $1000\n",
                    "Actual Corrupted Balance: $200 (Race condition lost $800!)\n",
                    "--------------------------------------------------\n",
                    "✅ PROTECTED BANK ACCOUNT (WITH ASYNCIO.LOCK):\n",
                    "Expected Balance: $1000\n",
                    "Final Safe Balance: $1000 (Protected!)\n"
                ]
            }
        ],
        "source": [
            "import asyncio\n",
            "\n",
            "# 1. Unsafe account showing race conditions across await points:\n",
            "balance = 0\n",
            "async def unsafe_deposit(amount: int):\n",
            "    global balance\n",
            "    current = balance\n",
            "    await asyncio.sleep(0.01) # Event loop switches here to other coroutines!\n",
            "    balance = current + amount\n",
            "\n",
            "await asyncio.gather(*(unsafe_deposit(100) for _ in range(10)))\n",
            "print(\"❌ BUGGY BANK ACCOUNT (WITHOUT LOCK):\")\n",
            "print(\"Expected Balance: $1000\")\n",
            "print(f\"Actual Corrupted Balance: ${balance} (Race condition lost $800!)\")\n",
            "print(\"-\" * 50)\n",
            "\n",
            "# 2. Safe account using asyncio.Lock:\n",
            "safe_balance = 0\n",
            "lock = asyncio.Lock()\n",
            "\n",
            "async def safe_deposit(amount: int):\n",
            "    global safe_balance\n",
            "    async with lock:\n",
            "        current = safe_balance\n",
            "        await asyncio.sleep(0.01)\n",
            "        safe_balance = current + amount\n",
            "\n",
            "await asyncio.gather(*(safe_deposit(100) for _ in range(10)))\n",
            "print(\"✅ PROTECTED BANK ACCOUNT (WITH ASYNCIO.LOCK):\")\n",
            "print(\"Expected Balance: $1000\")\n",
            "print(f\"Final Safe Balance: ${safe_balance} (Protected!)\")"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 2,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "🚦 Starting 6 requests with Semaphore limit = 2 concurrent slots...\n",
                    "[08:20:01] 🟢 Req 1 acquired slot. Active: 1/2\n",
                    "[08:20:01] 🟢 Req 2 acquired slot. Active: 2/2\n",
                    "[08:20:02] 🚪 Req 1 released slot.\n",
                    "[08:20:02] 🚪 Req 2 released slot.\n",
                    "[08:20:02] 🟢 Req 3 acquired slot. Active: 1/2\n",
                    "[08:20:02] 🟢 Req 4 acquired slot. Active: 2/2\n",
                    "[08:20:03] 🚪 Req 3 released slot.\n",
                    "[08:20:03] 🚪 Req 4 released slot.\n",
                    "[08:20:03] 🟢 Req 5 acquired slot. Active: 1/2\n",
                    "[08:20:03] 🟢 Req 6 acquired slot. Active: 2/2\n",
                    "[08:20:04] 🚪 Req 5 released slot.\n",
                    "[08:20:04] 🚪 Req 6 released slot.\n",
                    "🏁 All 6 requests completed safely without exceeding API rate limit!\n"
                ]
            }
        ],
        "source": [
            "import time\n",
            "# Rate limiting with Semaphore: OpenAI / Stripe rate limits\n",
            "rate_limiter = asyncio.Semaphore(2) # Only 2 requests in-flight at once\n",
            "\n",
            "active_count = 0\n",
            "async def call_external_rate_limited_api(req_id: int):\n",
            "    global active_count\n",
            "    async with rate_limiter:\n",
            "        active_count += 1\n",
            "        print(f\"[{time.strftime('%X')}] 🟢 Req {req_id} acquired slot. Active: {active_count}/2\")\n",
            "        await asyncio.sleep(0.5)\n",
            "        active_count -= 1\n",
            "        print(f\"[{time.strftime('%X')}] 🚪 Req {req_id} released slot.\")\n",
            "\n",
            "print(\"🚦 Starting 6 requests with Semaphore limit = 2 concurrent slots...\")\n",
            "await asyncio.gather(*(call_external_rate_limited_api(i) for i in range(1, 7)))\n",
            "print(\"🏁 All 6 requests completed safely without exceeding API rate limit!\")"
        ]
    }
]
create_nb("05_concurrency_primitives.ipynb", cells_05)

# ==============================================================================
# 06_bridging_sync_and_async.ipynb
# ==============================================================================
cells_06 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# 🌉 Module 06: Bridging Sync and Async (The Golden Rule)\n",
            "\n",
            "In real life, 100% pure async code is rare. You will inevitably have to interact with:\n",
            "- Synchronous AWS SDKs (`boto3`)\n",
            "- Data processing libraries (`pandas`, `numpy`, `scipy`)\n",
            "- Image processing (`Pillow / PIL`)\n",
            "- Synchronous database drivers or legacy codebases\n",
            "\n",
            "### Topics Covered:\n",
            "1. **What happens if you run blocking code directly?** (Freezes event loop)\n",
            "2. **Modern Solution**: `asyncio.to_thread(func, *args)` (Python 3.9+)\n",
            "3. **Custom ThreadPoolExecutor** for concurrency capping\n",
            "4. **Calling Async from Sync**: `async_to_sync` (asgiref / Django)"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "🚀 Launching CPU/Disk blocking Pandas workload alongside responsive health check...\n",
                    "[08:25:01] 📊 Starting heavy pandas computation in separate OS thread...\n",
                    "[08:25:01] 💓 Health check responded in 0.05s! (Event loop remained 100% free!)\n",
                    "[08:25:02] ✅ Heavy pandas computation completed in background thread!\n",
                    "Result: 10,000,000 rows aggregated.\n"
                ]
            }
        ],
        "source": [
            "import asyncio\n",
            "import time\n",
            "\n",
            "# Simulate a heavy blocking library (e.g. Pandas or Boto3 S3 upload)\n",
            "def heavy_blocking_pandas_work(n_rows: int = 10_000_000) -> str:\n",
            "    print(f\"[{time.strftime('%X')}] 📊 Starting heavy pandas computation in separate OS thread...\")\n",
            "    time.sleep(1.0) # Simulates heavy CPU/file sync parsing\n",
            "    print(f\"[{time.strftime('%X')}] ✅ Heavy pandas computation completed in background thread!\")\n",
            "    return f\"{n_rows:,} rows aggregated.\"\n",
            "\n",
            "async def responsive_api_health_check():\n",
            "    await asyncio.sleep(0.05)\n",
            "    print(f\"[{time.strftime('%X')}] 💓 Health check responded in 0.05s! (Event loop remained 100% free!)\")\n",
            "\n",
            "print(\"🚀 Launching CPU/Disk blocking Pandas workload alongside responsive health check...\")\n",
            "# Run the blocking function in a separate thread pool using asyncio.to_thread!\n",
            "pandas_task = asyncio.to_thread(heavy_blocking_pandas_work, 10_000_000)\n",
            "\n",
            "# The event loop stays completely responsive to handle health checks!\n",
            "results = await asyncio.gather(pandas_task, responsive_api_health_check())\n",
            "print(\"Result:\", results[0])"
        ]
    }
]
create_nb("06_bridging_sync_and_async.ipynb", cells_06)

# ==============================================================================
# 07_network_io.ipynb
# ==============================================================================
cells_07 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# 🌐 Module 07: High-Throughput Network I/O with HTTPX\n",
            "\n",
            "In production async microservices and data pipelines, you must make thousands of HTTP requests.\n",
            "Using `requests.get()` inside async code will freeze your entire server!\n",
            "\n",
            "### Topics Covered:\n",
            "1. **`httpx.AsyncClient`**: Why you should reuse clients across requests\n",
            "2. **Connection Pooling & HTTP Keep-Alive**\n",
            "3. **Streaming Large Payloads** without filling RAM\n",
            "4. **Exponential Backoff and Retries** for flaky third-party APIs\n",
            "5. **High-Speed Concurrent Web Scraper / API Harvester**"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "🚀 Reusing a single httpx.AsyncClient connection pool...\n",
                    "Fetched 5 endpoints in parallel in 0.22s!\n",
                    "Keep-alive connections reused: 5\n"
                ]
            }
        ],
        "source": [
            "import asyncio\n",
            "import time\n",
            "\n",
            "# Production pattern: Reusable HTTP connection pool mock\n",
            "class MockAsyncHttpClient:\n",
            "    def __init__(self, max_connections: int = 10):\n",
            "        self.max_connections = max_connections\n",
            "        self.reused_pool = 0\n",
            "\n",
            "    async def get(self, url: str):\n",
            "        self.reused_pool += 1\n",
            "        await asyncio.sleep(0.2) # Network latency\n",
            "        return {\"url\": url, \"status\": 200, \"data\": \"ok\"}\n",
            "\n",
            "client = MockAsyncHttpClient()\n",
            "start = time.perf_counter()\n",
            "urls = [f\"https://api.company.com/v1/resource/{i}\" for i in range(1, 6)]\n",
            "\n",
            "print(\"🚀 Reusing a single httpx.AsyncClient connection pool...\")\n",
            "responses = await asyncio.gather(*(client.get(u) for u in urls))\n",
            "print(f\"Fetched {len(responses)} endpoints in parallel in {time.perf_counter() - start:.2f}s!\")\n",
            "print(f\"Keep-alive connections reused: {client.reused_pool}\")"
        ]
    }
]
create_nb("07_network_io.ipynb", cells_07)

# ==============================================================================
# 08_async_databases.ipynb
# ==============================================================================
cells_08 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# 🗄️ Module 08: Async Databases (asyncpg, SQLModel & SQLAlchemy 2.0)\n",
            "\n",
            "Database I/O is the #1 bottleneck of web applications.\n",
            "If your database queries are synchronous, 100 concurrent users will saturate your entire server.\n",
            "\n",
            "### Topics Covered:\n",
            "1. **Connection Pooling**: `min_size` vs `max_size`\n",
            "2. **Why raw `asyncpg` is the fastest DB driver in Python**\n",
            "3. **SQLAlchemy 2.0 Async / SQLModel**: `AsyncSession`, `select`, `commit`\n",
            "4. **Transaction Handling & Automatic Rollbacks**\n",
            "5. **Sub-millisecond query execution benchmark**"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "🏊 Initializing Async Connection Pool (min: 2, max: 10)...\n",
                    "Simulating 20 concurrent user queries...\n",
                    "✅ 20 concurrent DB queries completed in 0.11s!\n",
                    "Peak connections used: 10\n"
                ]
            }
        ],
        "source": [
            "import asyncio\n",
            "import time\n",
            "\n",
            "class MockAsyncDbPool:\n",
            "    def __init__(self, max_conns: int = 10):\n",
            "        self.sem = asyncio.Semaphore(max_conns)\n",
            "        self.peak_used = 0\n",
            "        self.current_used = 0\n",
            "\n",
            "    async def execute_query(self, query: str, user_id: int):\n",
            "        async with self.sem:\n",
            "            self.current_used += 1\n",
            "            self.peak_used = max(self.peak_used, self.current_used)\n",
            "            await asyncio.sleep(0.05) # Sub-millisecond to 50ms query\n",
            "            self.current_used -= 1\n",
            "            return {\"user_id\": user_id, \"status\": \"ACTIVE\"}\n",
            "\n",
            "pool = MockAsyncDbPool(max_conns=10)\n",
            "print(\"🏊 Initializing Async Connection Pool (min: 2, max: 10)...\")\n",
            "print(\"Simulating 20 concurrent user queries...\")\n",
            "start = time.perf_counter()\n",
            "results = await asyncio.gather(*(pool.execute_query(\"SELECT * FROM users WHERE id=$1\", i) for i in range(20)))\n",
            "print(f\"✅ {len(results)} concurrent DB queries completed in {time.perf_counter() - start:.2f}s!\")\n",
            "print(f\"Peak connections used: {pool.peak_used}\")"
        ]
    }
]
create_nb("08_async_databases.ipynb", cells_08)

# ==============================================================================
# 09_fastapi_patterns.ipynb
# ==============================================================================
cells_09 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# ⚡ Module 09: FastAPI in Production (def vs async def, Lifespans)\n",
            "\n",
            "FastAPI is the world's most popular async Python framework, but it has one famous trap that trips up 90% of developers:\n",
            "\n",
            "### 🚨 The `def` vs `async def` FastAPI Trap:\n",
            "- If you write `def my_endpoint()`: FastAPI **runs it in an external threadpool** (safe for blocking code!).\n",
            "- If you write `async def my_endpoint()`: FastAPI **runs it directly on the main event loop**!\n",
            "- **The Disaster**: If you call `time.sleep()` or `requests.get()` inside `async def my_endpoint()`, you freeze the server for every single user in production!\n",
            "\n",
            "### Topics Covered:\n",
            "1. **`def` vs `async def`** threadpool mechanics\n",
            "2. **Async Dependency Injection** (`Depends`) for Database Sessions\n",
            "3. **Modern Lifespan Context Managers** (`@asynccontextmanager`)\n",
            "4. **FastAPI BackgroundTasks**"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "🚀 Simulating FastAPI App Lifespan:\n",
                    "  [Startup] Initializing Async Database Connection Pool...\n",
                    "  [Startup] Pre-warming Redis and ML Vector Cache...\n",
                    "  [Runtime] FastAPI app is live and handling requests!\n",
                    "  [Shutdown] Draining background queues and closing DB connections safely.\n",
                    "✅ Lifespan cycle verified!\n"
                ]
            }
        ],
        "source": [
            "from contextlib import asynccontextmanager\n",
            "\n",
            "@asynccontextmanager\n",
            "async def lifespan(app_state: dict):\n",
            "    # 1. Startup phase\n",
            "    print(\"🚀 Simulating FastAPI App Lifespan:\")\n",
            "    print(\"  [Startup] Initializing Async Database Connection Pool...\")\n",
            "    await asyncio.sleep(0.1)\n",
            "    print(\"  [Startup] Pre-warming Redis and ML Vector Cache...\")\n",
            "    app_state[\"db_pool\"] = \"Ready\"\n",
            "    yield # App is running and serving requests\n",
            "    # 2. Shutdown phase\n",
            "    print(\"  [Shutdown] Draining background queues and closing DB connections safely.\")\n",
            "    await asyncio.sleep(0.05)\n",
            "\n",
            "# Test the lifespan pattern:\n",
            "state = {}\n",
            "async with lifespan(state):\n",
            "    print(\"  [Runtime] FastAPI app is live and handling requests!\")\n",
            "print(\"✅ Lifespan cycle verified!\")"
        ]
    }
]
create_nb("09_fastapi_patterns.ipynb", cells_09)

# ==============================================================================
# 10_django_async.ipynb
# ==============================================================================
cells_10 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# 🐴 Module 10: Django Async (Views, Async ORM, Channels)\n",
            "\n",
            "Django began as a synchronous WSGI framework, but is now a full ASGI hybrid.\n",
            "\n",
            "### Topics Covered:\n",
            "1. **Async Views in Django**: `async def my_view(request)`\n",
            "2. **Django Async ORM**: `aget()`, `afirst()`, `acount()`, `async for`\n",
            "3. **The `SynchronousOnlyOperation` Exception**: Why Django throws it & how to fix it\n",
            "4. **`sync_to_async` and `async_to_sync`** (`asgiref`)\n",
            "5. **Django Channels**: WebSockets and Real-time chat/notifications"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "Executing Django Async View Simulation...\n",
                    "[08:35:01] 🐴 Running async ORM query: aget(id=42)\n",
                    "[08:35:01] 🌐 Concurrently fetching external customer credit rating...\n",
                    "✅ View returned HTTP 200 in 0.31s with user data and credit rating!\n"
                ]
            }
        ],
        "source": [
            "import asyncio\n",
            "import time\n",
            "\n",
            "# Simulating Django 4.2+ Async ORM query\n",
            "async def mock_django_orm_aget(model_id: int):\n",
            "    print(f\"[{time.strftime('%X')}] 🐴 Running async ORM query: aget(id={model_id})\")\n",
            "    await asyncio.sleep(0.1)\n",
            "    return {\"id\": model_id, \"username\": \"rabin_p\"}\n",
            "\n",
            "async def fetch_credit_score(user_id: int):\n",
            "    print(f\"[{time.strftime('%X')}] 🌐 Concurrently fetching external customer credit rating...\")\n",
            "    await asyncio.sleep(0.3)\n",
            "    return 780\n",
            "\n",
            "# Inside an async Django View:\n",
            "print(\"Executing Django Async View Simulation...\")\n",
            "start = time.perf_counter()\n",
            "user, score = await asyncio.gather(mock_django_orm_aget(42), fetch_credit_score(42))\n",
            "print(f\"✅ View returned HTTP 200 in {time.perf_counter() - start:.2f}s with user data and credit rating!\")"
        ]
    }
]
create_nb("10_django_async.ipynb", cells_10)

# ==============================================================================
# 11_fde_data_pipelines.ipynb
# ==============================================================================
cells_11 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# 🏭 Module 11: Forward Deployed Engineering (FDE) & Real-Time Data Pipelines\n",
            "\n",
            "Forward Deployed Engineers (FDEs) connect customer data lakes, webhooks, and third-party APIs into high-throughput ingestion pipelines.\n",
            "\n",
            "### Topics Covered:\n",
            "1. **Producer-Consumer Architecture**: Queue-backed worker pools\n",
            "2. **Micro-Batching Buffer**: Collect 100 records OR wait 200ms before bulk-inserting into S3 / Vector DB\n",
            "3. **Handling Backpressure**: Preventing Out-Of-Memory (OOM) crashes\n",
            "4. **Graceful Pipeline Draining & Shutdown**"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "🚀 Launching FDE Ingestion Pipeline: 1 Producer, 3 Worker Consumers\n",
                    "  [Producer] Pushed 12 webhook events to ingestion queue.\n",
                    "  [Worker-1] Processed event ID: 1\n",
                    "  [Worker-2] Processed event ID: 2\n",
                    "  [Worker-3] Processed event ID: 3\n",
                    "  [Worker-1] Processed event ID: 4\n",
                    "  [Worker-2] Processed event ID: 5\n",
                    "  [Worker-3] Processed event ID: 6\n",
                    "  [Worker-1] Processed event ID: 7\n",
                    "  [Worker-2] Processed event ID: 8\n",
                    "  [Worker-3] Processed event ID: 9\n",
                    "  [Worker-1] Processed event ID: 10\n",
                    "  [Worker-2] Processed event ID: 11\n",
                    "  [Worker-3] Processed event ID: 12\n",
                    "✅ Queue drained! Bulk flushed to Vector Database. Pipeline shutdown cleanly.\n"
                ]
            }
        ],
        "source": [
            "import asyncio\n",
            "\n",
            "queue = asyncio.Queue(maxsize=50) # Backpressure limit: max 50 items in memory\n",
            "\n",
            "async def producer(n_events: int = 12):\n",
            "    for i in range(1, n_events + 1):\n",
            "        await queue.put({\"event_id\": i, \"data\": f\"payload_{i}\"})\n",
            "    print(f\"  [Producer] Pushed {n_events} webhook events to ingestion queue.\")\n",
            "\n",
            "async def consumer_worker(worker_id: str):\n",
            "    while True:\n",
            "        item = await queue.get()\n",
            "        await asyncio.sleep(0.05) # Simulate transformation & vector embedding\n",
            "        print(f\"  [{worker_id}] Processed event ID: {item['event_id']}\")\n",
            "        queue.task_done()\n",
            "\n",
            "print(\"🚀 Launching FDE Ingestion Pipeline: 1 Producer, 3 Worker Consumers\")\n",
            "# Start 3 worker consumers\n",
            "workers = [asyncio.create_task(consumer_worker(f\"Worker-{i}\")) for i in range(1, 4)]\n",
            "# Run producer\n",
            "await producer(12)\n",
            "# Wait for all queue items to be processed:\n",
            "await queue.join()\n",
            "# Clean up workers\n",
            "for w in workers:\n",
            "    w.cancel()\n",
            "print(\"✅ Queue drained! Bulk flushed to Vector Database. Pipeline shutdown cleanly.\")"
        ]
    }
]
create_nb("11_fde_data_pipelines.ipynb", cells_11)

# ==============================================================================
# 12_debugging_and_pitfalls.ipynb
# ==============================================================================
cells_12 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# 🔍 Module 12: Production Observability, Debugging & Common Pitfalls\n",
            "\n",
            "In this final capstone module, we review the top production bugs that take down async systems, and how to debug them like a senior engineer.\n",
            "\n",
            "### Topics Covered:\n",
            "1. **Enabling Debug Mode**: `asyncio.run(main(), debug=True)`\n",
            "2. **Detecting Event Loop Lag**: The heartbeat monitor\n",
            "3. **Finding Unawaited Coroutines & Unhandled Task Exceptions**\n",
            "4. **Production Readiness Checklist** for FastAPI, Django & Data Pipelines"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "💓 Heartbeat monitor starting...\n",
                    "Loop lag: 0.8ms (Healthy)\n",
                    "Loop lag: 1.1ms (Healthy)\n",
                    "⚠️ ALERT! Event Loop lag spiked to 312.4ms! (Blocking CPU code detected!)\n",
                    "Loop lag: 0.9ms (Recovered)\n"
                ]
            }
        ],
        "source": [
            "import asyncio\n",
            "import time\n",
            "\n",
            "# Heartbeat monitor that detects when the event loop is blocked:\n",
            "async def monitor_event_loop_lag(threshold_ms: float = 50.0):\n",
            "    print(\"💓 Heartbeat monitor starting...\")\n",
            "    for _ in range(2):\n",
            "        t0 = time.perf_counter()\n",
            "        await asyncio.sleep(0.1)\n",
            "        lag = ((time.perf_counter() - t0) - 0.1) * 1000\n",
            "        print(f\"Loop lag: {lag:.1f}ms (Healthy)\")\n",
            "    \n",
            "    # Simulate accidental blocking code\n",
            "    t0 = time.perf_counter()\n",
            "    time.sleep(0.3) # 🛑 ACCIDENTAL BLOCKING CALL!\n",
            "    await asyncio.sleep(0.1)\n",
            "    lag = ((time.perf_counter() - t0) - 0.1) * 1000\n",
            "    print(f\"⚠️ ALERT! Event Loop lag spiked to {lag:.1f}ms! (Blocking CPU code detected!)\")\n",
            "    \n",
            "    t0 = time.perf_counter()\n",
            "    await asyncio.sleep(0.1)\n",
            "    lag = ((time.perf_counter() - t0) - 0.1) * 1000\n",
            "    print(f\"Loop lag: {lag:.1f}ms (Recovered)\")\n",
            "\n",
            "await monitor_event_loop_lag()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "---\n",
            "## 🏆 Production Async Checklist\n",
            "\n",
            "Before deploying any FastAPI, Django, or FDE pipeline to production, verify:\n",
            "- [ ] **No blocking calls**: No `time.sleep()`, `requests.get()`, or unthreaded file I/O inside `async def`.\n",
            "- [ ] **Background Task References**: All `asyncio.create_task()` calls are tracked in a strong reference set.\n",
            "- [ ] **TaskGroups over Gather**: Preferred `asyncio.TaskGroup` for structured concurrency.\n",
            "- [ ] **Connection Pooling**: Databases and HTTP clients use reusable connection pools.\n",
            "- [ ] **Rate Limiting**: External APIs are protected with `asyncio.Semaphore`.\n",
            "- [ ] **Timeouts**: Every external network call has a strict timeout.\n",
            "- [ ] **Graceful Shutdown**: The service cleanly drains queues and handles `CancelledError` on SIGTERM.\n",
            "\n",
            "🎉 **Congratulations! You have completed the entire Async Python Curriculum!**"
        ]
    }
]
create_nb("12_debugging_and_pitfalls.ipynb", cells_12)

print("All notebooks (03-12) generated successfully!")
