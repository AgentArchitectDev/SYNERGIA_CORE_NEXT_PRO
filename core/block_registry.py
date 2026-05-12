import json
from pathlib import Path


class BlockRegistry:

    def __init__(self):

        self.blocks_dir = Path("blocks")

    def get_blocks(self):

        blocks = []

        for block in self.blocks_dir.iterdir():

            if not block.is_dir():
                continue

            meta_file = block / "meta.json"

            if not meta_file.exists():
                continue

            meta = json.loads(
                meta_file.read_text(encoding="utf-8")
            )

            meta["id"] = block.name

            blocks.append(meta)

        return blocks


registry = BlockRegistry()
