from fastapi import FastAPI, status
from pydantic import BaseModel, Field
import uvicorn

# Ініціалізація вебдодатка з метаданими для документації
app = FastAPI(
    title="Practice Project API",
    version="1.0.0",
    description="Backend service prototype"
)

# Pydantic-модель для валідації вхідних даних клієнта
class DataItem(BaseModel):
    title: str = Field(..., min_length=3, max_length=100, description="Назва об'єкта")
    description: str | None = Field(None, description="Опціональний опис")
    value: float = Field(..., gt=0, description="Числове значення, більше за нуль")

# Кореневий ендпоінт для перевірки працездатності сервісу
@app.get("/", tags=["Root"])
async def read_root():
    return {
        "status": "success",
        "message": "API is up and running successfully",
        "version": "1.0.0"
    }

# Ендпоінт для створення запису та виконання обчислень
@app.post("/items/", tags=["Items"], status_code=status.HTTP_201_CREATED)
async def create_item(item: DataItem):
    # Імітація бізнес-логіки та розрахунків
    calculated_tax = round(item.value * 0.2, 2)
    total_cost = round(item.value + calculated_tax, 2)

    return {
        "status": "created",
        "received_data": item,
        "calculation_results": {
            "base_value": item.value,
            "calculated_tax": calculated_tax,
            "total_cost": total_cost
        }
    }

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)