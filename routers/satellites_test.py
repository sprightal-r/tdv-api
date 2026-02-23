from fastapi.testclient import TestClient
from main import app
from store import satellitestore
import copy

client = TestClient(app)

# Copy rows to preserve data in store
rows = copy.deepcopy(satellitestore.rows)

json_rows = [x.model_dump() for x in rows]

def test_list_satellites():
    response = client.get("/satellites/")
    assert response.status_code == 200
    assert response.json() == json_rows