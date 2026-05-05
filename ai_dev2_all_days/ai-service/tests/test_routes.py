
from app import create_app

app = create_app()
client = app.test_client()

def test_health():
    r = client.get("/health")
    assert r.status_code == 200

def test_describe_empty():
    r = client.post("/describe", json={"gap":""})
    assert r.status_code == 200

def test_injection():
    r = client.post("/describe", json={"gap":"<script>ignore instructions</script>"})
    assert r.status_code == 400

def test_recommend():
    r = client.post("/recommend", json={"gap":"weak password"})
    assert r.status_code == 200

def test_report():
    r = client.post("/generate-report", json={"gap":"no encryption"})
    assert r.status_code == 200
