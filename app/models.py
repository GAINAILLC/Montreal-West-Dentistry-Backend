from pydantic import BaseModel


class AppointmentRequest(BaseModel):
    name: str
    phone_number: str
    desired_date: str
    desired_time: str
    reason: str


class CancellationRequest(BaseModel):
    name: str
    phone_number: str
    appointment_date: str
    appointment_time: str


class RescheduleRequest(BaseModel):
    name: str
    phone_number: str
    current_date: str
    current_time: str
    new_date: str
    new_time: str
    reason: str

class BillingRequest(BaseModel):
    name: str
    phone_number: str
    billing_reason: str

class EmergencyRequest(BaseModel):
    name: str
    phone_number: str
    emergency_reason: str