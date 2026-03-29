import json
import os
import aiofiles
from typing import Dict, Any

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

async def load_config() -> Dict[str, Any]:
    try:
        async with aiofiles.open(os.path.join(BASE_DIR, "data", "other.json"), "r", encoding="utf-8") as f:
            return json.loads(await f.read())
    except:
        return {}
