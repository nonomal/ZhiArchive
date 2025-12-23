from fastapi import APIRouter

router = APIRouter()


from . import core, login  # noqa: E402

router.include_router(
    login.router,
    prefix="/login",
)
router.include_router(
    login.public_router,
    prefix="/login",
)
router.include_router(
    core.router,
    prefix="/core",
)
router.include_router(
    core.public_router,
    prefix="/core",
)
