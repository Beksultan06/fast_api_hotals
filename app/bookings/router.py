from fastapi import APIRouter, Depends, Request
from app.bookings.schemas import SBookings
from app.bookings.dao import BookingDAO
from app.user.dependencies import get_current_user
from app.user.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)

@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookings]:
    return await BookingDAO.find_all(user_id=user.id)

@router.post("")
async def add_bookings(
    user: Users = Depends(get_current_user),
):
    await BookingDAO.add()