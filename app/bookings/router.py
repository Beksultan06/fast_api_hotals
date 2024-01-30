from datetime import date
from fastapi import APIRouter, Depends, Request
from app.bookings.schemas import SBookings
from app.bookings.dao import BookingDAO
from app.user.dependencies import get_current_user
from app.user.models import Users
from app.exeptions import RoomCannotBeBooked

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)

@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookings]:
    return await BookingDAO.find_all(user_id=user.id)

@router.post("")
async def add_bookings(room_id: int, date_from: date, date_to: date,
    user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(user.id, room_id,date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked
    