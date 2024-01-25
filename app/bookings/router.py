from fastapi import APIRouter
from app.bookings.schemas import SBookings
from app.bookings.utils import BookingDAO

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)

@router.get("")
async def get_bookings() -> list[SBookings]:
    return await BookingDAO.find_all()