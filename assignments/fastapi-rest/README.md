# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework to practice designing endpoints, request/response models, and basic persistence. The API should be documented, testable, and run locally with minimal setup.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Service

#### Description
Create a FastAPI application that exposes a set of CRUD endpoints for a simple resource (e.g., Todo items or Books). The application must use Pydantic models for request and response validation and should include clear OpenAPI documentation (automatic from FastAPI).

#### Requirements
Completed program should:

- Provide endpoints to Create, Read (single and list), Update, and Delete items.
- Use Pydantic models for input validation and output serialization.
- Store data in memory (e.g., a list or dict) so the app can run without external databases.
- Return appropriate HTTP status codes (201 for created, 404 for not found, etc.).
- Include example curl or HTTP requests in the README demonstrating the API.
- Be runnable locally (e.g., `uvicorn starter_code:app --reload`) and include a short run instruction.

#### Example
```
POST /items  -> 201 Created
GET /items   -> 200 OK
GET /items/1 -> 200 OK or 404 Not Found
```

### 🛠️ Testing & Documentation

#### Description
Add tests and ensure the API documentation is accessible.

#### Requirements (pick at least one)

- Provide a few automated tests using `requests` or `pytest` + `httpx` to verify core endpoints.
- Show how to access the interactive OpenAPI docs (`/docs`) and the JSON schema (`/openapi.json`).
- Add input validation tests that show the API returns `422 Unprocessable Entity` for invalid input.
- (Optional) Add simple persistence using a JSON file so data persists across restarts.

---

## 📎 Starter Code
A minimal `starter-code.py` is included to help you get started.

---

## 📝 Submission Notes
- Make sure your `README.md` has clear run instructions and at least one example request for each endpoint.
- If you add dependencies, include a `requirements.txt` or mention dependencies in the README.
