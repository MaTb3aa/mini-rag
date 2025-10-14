from .BaseDataModel import BaseDataModel
from .db_schemes import DataChunk
from .enums.DataBaseEnum import DataBaseEnum
from bson import ObjectId
from typing import Optional

class ChunkModel(BaseDataModel):
    def __init__(self, db_client: object):
        super().__init__(db_client=db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTION_CHUNK_NAME.value]
    
    async def create_chunk(self, chunk: DataChunk) -> DataChunk:
        result = await self.collection.insert_one(chunk.dict(exclude_none=True))
        chunk.id = result.inserted_id  
        return chunk

    async def get_chunk(self, chunk_id: str) -> Optional[DataChunk]:
        result = await self.collection.find_one({
            "_id": ObjectId(chunk_id)
        })

        if result is None:
            return None
        return DataChunk(**result)