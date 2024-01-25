from fastapi import APIRouter, Request
from app.bookings.schemas import SBookings
from app.bookings.dao import BookingDAO

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)

@router.get("")
async def get_bookings(user): #-> list[SBookings]:
    return await BookingDAO.find_all()