from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_users():
    """Retrieve a list of users (not implemented yet)."""
    return {"message": "User management will be implemented soon"}
