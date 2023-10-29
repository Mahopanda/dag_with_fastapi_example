from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel,Field
from data_processor import DataProcessor

app = FastAPI()

# 初始化DataProcessor的實例
processor = DataProcessor()

# 定義FastAPI的資料模型
class DataInput(BaseModel):
    attribute:str = Field(default="A", title="Attribute")
    value: float = Field(default=95.5, title="Value")
    text: str=Field(default="Hello123", title="Text")
    
   


@app.post("/process/")
def process_data(input: DataInput):
    try:

        result = processor.process(input.dict())
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


