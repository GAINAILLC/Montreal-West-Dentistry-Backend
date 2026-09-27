from fastapi import APIRouter, HTTPException

from app.models import (
    AppointmentRequest,
    CancellationRequest,
    RescheduleRequest,
    BillingRequest,
    EmergencyRequest
)

from app.services.email import (
    send_appointment_email,
    send_cancellation_email,
    send_reschedule_email,
    send_billing_email,
    send_emergency_email
)


router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.post("/request")
async def request_appointment(appointment: AppointmentRequest):
    try:
        send_appointment_email(appointment)

        return {
            "success": True,
            "message": "Appointment request sent successfully"
        }

    except Exception as error:
        print(f"Email error: {error}")

        raise HTTPException(
            status_code=500,
            detail="Failed to send appointment request"
        )


@router.post("/cancel")
async def cancel_appointment(cancellation: CancellationRequest):
    try:
        send_cancellation_email(cancellation)

        return {
            "success": True,
            "message": "Cancellation request sent successfully"
        }

    except Exception as error:
        print(f"Email error: {error}")

        raise HTTPException(
            status_code=500,
            detail="Failed to send cancellation request"
        )


@router.post("/reschedule")
async def reschedule_appointment(reschedule: RescheduleRequest):
    try:
        send_reschedule_email(reschedule)

        return {
            "success": True,
            "message": "Reschedule request sent successfully"
        }

    except Exception as error:
        print(f"Email error: {error}")

        raise HTTPException(
            status_code=500,
            detail="Failed to send reschedule request"
        )


@router.post("/billing")
async def billing_request(billing: BillingRequest):
    try:
        send_billing_email(billing)

        return {
            "success": True,
            "message": "Billing request sent successfully"
        }
    except Exception as error:
        print(f"Email error: {error}")

        raise HTTPException(
            status_code=500,
            detail="Failed to send billing request"
        )

@router.post("/emergency")
async def emergency_request(emergency: EmergencyRequest):
    try:
        send_emergency_email(emergency)

        return {
            "success": True,
            "message": "Emergency request sent successfully"
        }
    except Exception as error:
        print(f"Email error: {error}")

        raise HTTPException(
            status_code=500,
            detail="Failed to send emergency request"
        )