import os
import resend

from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")


def send_appointment_email(appointment):
    recipient = "shadyzoweil@outlook.com"

    logo_url = "https://montrealwestdentistry.com/wp-content/uploads/2023/12/MWD-397x-88-px-logo.png"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>New Appointment Request</title>
    </head>

    <body style="
        margin: 0;
        padding: 0;
        background-color: #f4f7f9;
        font-family: Arial, Helvetica, sans-serif;
        color: #333333;
    ">

        <table width="100%" cellpadding="0" cellspacing="0" border="0"
            style="background-color: #f4f7f9; padding: 40px 20px;">

            <tr>
                <td align="center">

                    <table width="600" cellpadding="0" cellspacing="0" border="0"
                        style="
                            max-width: 600px;
                            width: 100%;
                            background-color: #ffffff;
                            border-radius: 12px;
                            overflow: hidden;
                            box-shadow: 0 2px 10px rgba(0,0,0,0.06);
                        ">

                        <!-- Header -->
                        <tr>
                            <td align="center"
                                style="
                                    background-color: #0297d1;
                                    padding: 30px 20px;
                                ">

                                <table cellpadding="0" cellspacing="0" border="0"
                                    style="
                                        background-color: #ffffff;
                                        border-radius: 10px;
                                        margin-bottom: 20px;
                                    ">
                                    <tr>
                                        <td style="padding: 12px 20px;">
                                            <img
                                                src="{logo_url}"
                                                alt="Montreal West Dentistry"
                                                style="
                                                    max-width: 180px;
                                                    max-height: 70px;
                                                    display: block;
                                                "
                                            >
                                        </td>
                                    </tr>
                                </table>

                                <h1 style="
                                    margin: 0;
                                    color: #ffffff;
                                    font-size: 24px;
                                    font-weight: 600;
                                ">
                                    New Appointment Request
                                </h1>

                            </td>
                        </tr>

                        <!-- Content -->
                        <tr>
                            <td style="padding: 35px 40px;">

                                <p style="
                                    margin: 0 0 25px 0;
                                    font-size: 16px;
                                    line-height: 1.6;
                                    color: #555555;
                                ">
                                    A new appointment request has been submitted
                                    through the AI receptionist.
                                </p>

                                <!-- Patient Information -->
                                <table width="100%" cellpadding="0" cellspacing="0" border="0"
                                    style="
                                        border: 1px solid #e5e9ec;
                                        border-radius: 8px;
                                        overflow: hidden;
                                    ">

                                    <tr>
                                        <td colspan="2"
                                            style="
                                                background-color: #f0f9fd;
                                                padding: 14px 18px;
                                                border-bottom: 1px solid #e5e9ec;
                                            ">
                                            <strong style="
                                                color: #0297d1;
                                                font-size: 15px;
                                            ">
                                                Appointment Details
                                            </strong>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            width: 35%;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            Patient Name
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {appointment.name}
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            Phone Number
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {appointment.phone_number}
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            Desired Date
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {appointment.desired_date}
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            Desired Time
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {appointment.desired_time}
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                        ">
                                            Reason for Visit
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                        ">
                                            {appointment.reason}
                                        </td>
                                    </tr>

                                </table>

                                <!-- Action Message -->
                                <table width="100%" cellpadding="0" cellspacing="0" border="0"
                                    style="margin-top: 25px;">

                                    <tr>
                                        <td style="
                                            background-color: #f8fafb;
                                            border-left: 4px solid #0297d1;
                                            padding: 15px 18px;
                                        ">
                                            <p style="
                                                margin: 0;
                                                font-size: 14px;
                                                line-height: 1.5;
                                                color: #555555;
                                            ">
                                                Please review this request and contact
                                                the patient to confirm the appointment.
                                            </p>
                                        </td>
                                    </tr>

                                </table>

                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td align="center"
                                style="
                                    background-color: #f8fafb;
                                    border-top: 1px solid #eeeeee;
                                    padding: 20px;
                                ">

                                <p style="
                                    margin: 0;
                                    font-size: 12px;
                                    color: #999999;
                                ">
                                    Montreal West Dentistry
                                </p>

                                <p style="
                                    margin: 6px 0 0 0;
                                    font-size: 11px;
                                    color: #aaaaaa;
                                ">
                                    Appointment request generated by AI Receptionist
                                </p>

                            </td>
                        </tr>

                    </table>

                </td>
            </tr>

        </table>

    </body>
    </html>
    """

    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": recipient,
        "subject": f"New Appointment Request - {appointment.name}",
        "html": html,
    })




def send_cancellation_email(cancellation):
    recipient = "shadyzoweil@outlook.com"

    logo_url = "https://montrealwestdentistry.com/wp-content/uploads/2023/12/MWD-397x-88-px-logo.png"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Appointment Cancellation Request</title>
    </head>

    <body style="
        margin: 0;
        padding: 0;
        background-color: #f4f7f9;
        font-family: Arial, Helvetica, sans-serif;
        color: #333333;
    ">

        <table width="100%" cellpadding="0" cellspacing="0" border="0"
            style="background-color: #f4f7f9; padding: 40px 20px;">

            <tr>
                <td align="center">

                    <table width="600" cellpadding="0" cellspacing="0" border="0"
                        style="
                            max-width: 600px;
                            width: 100%;
                            background-color: #ffffff;
                            border-radius: 12px;
                            overflow: hidden;
                            box-shadow: 0 2px 10px rgba(0,0,0,0.06);
                        ">

                        <!-- Header -->
                        <tr>
                            <td align="center"
                                style="
                                    background-color: #0297d1;
                                    padding: 30px 20px;
                                ">

                                <table cellpadding="0" cellspacing="0" border="0"
                                    style="
                                        background-color: #ffffff;
                                        border-radius: 10px;
                                        margin-bottom: 20px;
                                    ">

                                    <tr>
                                        <td style="padding: 12px 20px;">
                                            <img
                                                src="{logo_url}"
                                                alt="Montreal West Dentistry"
                                                style="
                                                    max-width: 180px;
                                                    max-height: 70px;
                                                    display: block;
                                                "
                                            >
                                        </td>
                                    </tr>

                                </table>

                                <h1 style="
                                    margin: 0;
                                    color: #ffffff;
                                    font-size: 24px;
                                    font-weight: 600;
                                ">
                                    Appointment Cancellation Request
                                </h1>

                            </td>
                        </tr>

                        <!-- Content -->
                        <tr>
                            <td style="padding: 35px 40px;">

                                <p style="
                                    margin: 0 0 25px 0;
                                    font-size: 16px;
                                    line-height: 1.6;
                                    color: #555555;
                                ">
                                    A patient has requested to cancel an existing
                                    appointment through the AI receptionist.
                                </p>

                                <!-- Patient Information -->
                                <table width="100%" cellpadding="0" cellspacing="0" border="0"
                                    style="
                                        border: 1px solid #e5e9ec;
                                        border-radius: 8px;
                                        overflow: hidden;
                                    ">

                                    <tr>
                                        <td colspan="2"
                                            style="
                                                background-color: #f0f9fd;
                                                padding: 14px 18px;
                                                border-bottom: 1px solid #e5e9ec;
                                            ">
                                            <strong style="
                                                color: #0297d1;
                                                font-size: 15px;
                                            ">
                                                Cancellation Details
                                            </strong>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            width: 35%;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            Patient Name
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {cancellation.name}
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            Phone Number
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {cancellation.phone_number}
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            Appointment Date
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {cancellation.appointment_date}
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                        ">
                                            Appointment Time
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                        ">
                                            {cancellation.appointment_time}
                                        </td>
                                    </tr>

                                </table>

                                <!-- Action Message -->
                                <table width="100%" cellpadding="0" cellspacing="0" border="0"
                                    style="margin-top: 25px;">

                                    <tr>
                                        <td style="
                                            background-color: #f8fafb;
                                            border-left: 4px solid #0297d1;
                                            padding: 15px 18px;
                                        ">

                                            <p style="
                                                margin: 0;
                                                font-size: 14px;
                                                line-height: 1.5;
                                                color: #555555;
                                            ">
                                                Please review the cancellation request
                                                and update the patient's appointment.
                                            </p>

                                        </td>
                                    </tr>

                                </table>

                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td align="center"
                                style="
                                    background-color: #f8fafb;
                                    border-top: 1px solid #eeeeee;
                                    padding: 20px;
                                ">

                                <p style="
                                    margin: 0;
                                    font-size: 12px;
                                    color: #999999;
                                ">
                                    Montreal West Dentistry
                                </p>

                                <p style="
                                    margin: 6px 0 0 0;
                                    font-size: 11px;
                                    color: #aaaaaa;
                                ">
                                    Cancellation request generated by AI Receptionist
                                </p>

                            </td>
                        </tr>

                    </table>

                </td>
            </tr>

        </table>

    </body>
    </html>
    """

    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": recipient,
        "subject": f"Appointment Cancellation Request - {cancellation.name}",
        "html": html,
    })


def send_reschedule_email(reschedule):
    recipient = "shadyzoweil@outlook.com"

    logo_url = "https://montrealwestdentistry.com/wp-content/uploads/2023/12/MWD-397x-88-px-logo.png"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Appointment Reschedule Request</title>
    </head>

    <body style="
        margin: 0;
        padding: 0;
        background-color: #f4f7f9;
        font-family: Arial, Helvetica, sans-serif;
        color: #333333;
    ">

        <table width="100%" cellpadding="0" cellspacing="0" border="0"
            style="background-color: #f4f7f9; padding: 40px 20px;">

            <tr>
                <td align="center">

                    <table width="600" cellpadding="0" cellspacing="0" border="0"
                        style="
                            max-width: 600px;
                            width: 100%;
                            background-color: #ffffff;
                            border-radius: 12px;
                            overflow: hidden;
                            box-shadow: 0 2px 10px rgba(0,0,0,0.06);
                        ">

                        <!-- Header -->
                        <tr>
                            <td align="center"
                                style="
                                    background-color: #0297d1;
                                    padding: 30px 20px;
                                ">

                                <table cellpadding="0" cellspacing="0" border="0"
                                    style="
                                        background-color: #ffffff;
                                        border-radius: 10px;
                                        margin-bottom: 20px;
                                    ">

                                    <tr>
                                        <td style="padding: 12px 20px;">
                                            <img
                                                src="{logo_url}"
                                                alt="Montreal West Dentistry"
                                                style="
                                                    max-width: 180px;
                                                    max-height: 70px;
                                                    display: block;
                                                "
                                            >
                                        </td>
                                    </tr>

                                </table>

                                <h1 style="
                                    margin: 0;
                                    color: #ffffff;
                                    font-size: 24px;
                                    font-weight: 600;
                                ">
                                    Appointment Reschedule Request
                                </h1>

                            </td>
                        </tr>

                        <!-- Content -->
                        <tr>
                            <td style="padding: 35px 40px;">

                                <p style="
                                    margin: 0 0 25px 0;
                                    font-size: 16px;
                                    line-height: 1.6;
                                    color: #555555;
                                ">
                                    A patient has requested to reschedule an existing
                                    appointment through the AI receptionist.
                                </p>

                                <!-- Patient Information -->
                                <table width="100%" cellpadding="0" cellspacing="0" border="0"
                                    style="
                                        border: 1px solid #e5e9ec;
                                        border-radius: 8px;
                                        overflow: hidden;
                                    ">

                                    <tr>
                                        <td colspan="2"
                                            style="
                                                background-color: #f0f9fd;
                                                padding: 14px 18px;
                                                border-bottom: 1px solid #e5e9ec;
                                            ">
                                            <strong style="
                                                color: #0297d1;
                                                font-size: 15px;
                                            ">
                                                Rescheduling Details
                                            </strong>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            width: 35%;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            Patient Name
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {reschedule.name}
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            Phone Number
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {reschedule.phone_number}
                                        </td>
                                    </tr>

                                    <tr>
                                        <td colspan="2"
                                            style="
                                                background-color: #f8fafb;
                                                padding: 12px 18px;
                                                border-bottom: 1px solid #eeeeee;
                                            ">
                                            <strong style="
                                                color: #555555;
                                                font-size: 14px;
                                            ">
                                                Current Appointment
                                            </strong>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            Current Date
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {reschedule.current_date}
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            Current Time
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {reschedule.current_time}
                                        </td>
                                    </tr>

                                    <tr>
                                        <td colspan="2"
                                            style="
                                                background-color: #f8fafb;
                                                padding: 12px 18px;
                                                border-bottom: 1px solid #eeeeee;
                                            ">
                                            <strong style="
                                                color: #555555;
                                                font-size: 14px;
                                            ">
                                                New Requested Appointment
                                            </strong>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            New Date
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {reschedule.new_date}
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            New Time
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {reschedule.new_time}
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                        ">
                                            Reason for Visit
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                        ">
                                            {reschedule.reason}
                                        </td>
                                    </tr>

                                </table>

                                <!-- Action Message -->
                                <table width="100%" cellpadding="0" cellspacing="0" border="0"
                                    style="margin-top: 25px;">

                                    <tr>
                                        <td style="
                                            background-color: #f8fafb;
                                            border-left: 4px solid #0297d1;
                                            padding: 15px 18px;
                                        ">

                                            <p style="
                                                margin: 0;
                                                font-size: 14px;
                                                line-height: 1.5;
                                                color: #555555;
                                            ">
                                                Please review the requested change,
                                                confirm availability, and contact
                                                the patient to confirm the new appointment.
                                            </p>

                                        </td>
                                    </tr>

                                </table>

                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td align="center"
                                style="
                                    background-color: #f8fafb;
                                    border-top: 1px solid #eeeeee;
                                    padding: 20px;
                                ">

                                <p style="
                                    margin: 0;
                                    font-size: 12px;
                                    color: #999999;
                                ">
                                    Montreal West Dentistry
                                </p>

                                <p style="
                                    margin: 6px 0 0 0;
                                    font-size: 11px;
                                    color: #aaaaaa;
                                ">
                                    Reschedule request generated by AI Receptionist
                                </p>

                            </td>
                        </tr>

                    </table>

                </td>
            </tr>

        </table>

    </body>
    </html>
    """

    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": recipient,
        "subject": f"Appointment Reschedule Request - {reschedule.name}",
        "html": html,
    })





def send_billing_email(billing):

    recipient = "shadyzoweil@outlook.com"

    logo_url = "https://montrealwestdentistry.com/wp-content/uploads/2023/12/MWD-397x-88-px-logo.png"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Billing Request</title>
    </head>

    <body style="
        margin: 0;
        padding: 0;
        background-color: #f4f7f9;
        font-family: Arial, Helvetica, sans-serif;
        color: #333333;
    ">

        <table width="100%" cellpadding="0" cellspacing="0" border="0"
            style="background-color: #f4f7f9; padding: 40px 20px;">
            <tr>
                <td align="center">

                    <table width="600" cellpadding="0" cellspacing="0" border="0"
                        style="
                            max-width: 600px;
                            width: 100%;
                            background-color: #ffffff;
                            border-radius: 12px;
                            overflow: hidden;
                            box-shadow: 0 2px 10px rgba(0,0,0,0.06);
                        ">

                        <!-- Header -->
                        <tr>
                            <td align="center"
                                style="
                                    background-color: #0297d1;
                                    padding: 30px 20px;
                                ">

                                <table cellpadding="0" cellspacing="0" border="0"
                                    style="
                                        background-color: #ffffff;
                                        border-radius: 10px;
                                        margin-bottom: 20px;
                                    ">
                                    <tr>
                                        <td style="padding: 12px 20px;">
                                            <img
                                                src="{logo_url}"
                                                alt="Montreal West Dentistry"
                                                style="
                                                    max-width: 180px;
                                                    max-height: 70px;
                                                    display: block;
                                                "
                                            >
                                        </td>
                                    </tr>
                                </table>

                                <h1 style="
                                    margin: 0;
                                    color: #ffffff;
                                    font-size: 24px;
                                    font-weight: 600;
                                ">
                                    Billing Request
                                </h1>

                            </td>
                        </tr>

                        <!-- Content -->
                        <tr>
                            <td style="padding: 35px 40px;">

                                <p style="
                                    margin: 0 0 25px 0;
                                    font-size: 16px;
                                    line-height: 1.6;
                                    color: #555555;
                                ">
                                    A patient has submitted a billing request
                                    through the AI receptionist.
                                </p>

                                <!-- Patient Information -->
                                <table width="100%" cellpadding="0" cellspacing="0" border="0"
                                    style="
                                        border: 1px solid #e5e9ec;
                                        border-radius: 8px;
                                        overflow: hidden;
                                    ">

                                    <tr>
                                        <td colspan="2"
                                            style="
                                                background-color: #f0f9fd;
                                                padding: 14px 18px;
                                                border-bottom: 1px solid #e5e9ec;
                                            ">
                                            <strong style="
                                                color: #0297d1;
                                                font-size: 15px;
                                            ">
                                                Patient Information
                                            </strong>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            width: 35%;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            Patient Name
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {billing.name}
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                        ">
                                            Phone Number
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                        ">
                                            {billing.phone_number}
                                        </td>
                                    </tr>
                                     <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                        ">
                                            Billing Reason
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                        ">
                                            {billing.billing_reason}
                                        </td>
                                    </tr>

                                </table>

                                <!-- Action Message -->
                                <table width="100%" cellpadding="0" cellspacing="0" border="0"
                                    style="margin-top: 25px;">
                                    <tr>
                                        <td style="
                                            background-color: #f8fafb;
                                            border-left: 4px solid #0297d1;
                                            padding: 15px 18px;
                                        ">
                                            <p style="
                                                margin: 0;
                                                font-size: 14px;
                                                line-height: 1.5;
                                                color: #555555;
                                            ">
                                                Please review the patient's billing request
                                                and contact them during regular business hours.
                                            </p>
                                        </td>
                                    </tr>
                                </table>

                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td align="center"
                                style="
                                    background-color: #f8fafb;
                                    border-top: 1px solid #eeeeee;
                                    padding: 20px;
                                ">

                                <p style="
                                    margin: 0;
                                    font-size: 12px;
                                    color: #999999;
                                ">
                                    Montreal West Dentistry
                                </p>

                                <p style="
                                    margin: 6px 0 0 0;
                                    font-size: 11px;
                                    color: #aaaaaa;
                                ">
                                    Billing request generated by AI Receptionist
                                </p>

                            </td>
                        </tr>

                    </table>

                </td>
            </tr>
        </table>

    </body>
    </html>
    """

    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": recipient,
        "subject": f"Billing Request - {billing.name}",
        "html": html,
    })



def send_emergency_email(emergency):

    recipient = "shadyzoweil@outlook.com"

    logo_url = "https://montrealwestdentistry.com/wp-content/uploads/2023/12/MWD-397x-88-px-logo.png"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Emergency Request</title>
    </head>

    <body style="
        margin: 0;
        padding: 0;
        background-color: #f4f7f9;
        font-family: Arial, Helvetica, sans-serif;
        color: #333333;
    ">

        <table width="100%" cellpadding="0" cellspacing="0" border="0"
            style="background-color: #f4f7f9; padding: 40px 20px;">
            <tr>
                <td align="center">

                    <table width="600" cellpadding="0" cellspacing="0" border="0"
                        style="
                            max-width: 600px;
                            width: 100%;
                            background-color: #ffffff;
                            border-radius: 12px;
                            overflow: hidden;
                            box-shadow: 0 2px 10px rgba(0,0,0,0.06);
                        ">

                        <!-- Header -->
                        <tr>
                            <td align="center"
                                style="
                                    background-color: #0297d1;
                                    padding: 30px 20px;
                                ">

                                <table cellpadding="0" cellspacing="0" border="0"
                                    style="
                                        background-color: #ffffff;
                                        border-radius: 10px;
                                        margin-bottom: 20px;
                                    ">
                                    <tr>
                                        <td style="padding: 12px 20px;">
                                            <img
                                                src="{logo_url}"
                                                alt="Montreal West Dentistry"
                                                style="
                                                    max-width: 180px;
                                                    max-height: 70px;
                                                    display: block;
                                                "
                                            >
                                        </td>
                                    </tr>
                                </table>

                                <h1 style="
                                    margin: 0;
                                    color: #ffffff;
                                    font-size: 24px;
                                    font-weight: 600;
                                ">
                                    Emergency Request
                                </h1>

                            </td>
                        </tr>

                        <!-- Content -->
                        <tr>
                            <td style="padding: 35px 40px;">

                                <p style="
                                    margin: 0 0 25px 0;
                                    font-size: 16px;
                                    line-height: 1.6;
                                    color: #555555;
                                ">
                                    A patient has reported a dental emergency
                                    through the AI receptionist.
                                </p>

                                <!-- Emergency Information -->
                                <table width="100%" cellpadding="0" cellspacing="0" border="0"
                                    style="
                                        border: 1px solid #e5e9ec;
                                        border-radius: 8px;
                                        overflow: hidden;
                                    ">

                                    <tr>
                                        <td colspan="2"
                                            style="
                                                background-color: #f0f9fd;
                                                padding: 14px 18px;
                                                border-bottom: 1px solid #e5e9ec;
                                            ">
                                            <strong style="
                                                color: #0297d1;
                                                font-size: 15px;
                                            ">
                                                Emergency Details
                                            </strong>
                                        </td>
                                    </tr>

                                    <!-- Patient Name -->
                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            width: 35%;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            Patient Name
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {emergency.name}
                                        </td>
                                    </tr>

                                    <!-- Phone Number -->
                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            Phone Number
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                            border-bottom: 1px solid #eeeeee;
                                        ">
                                            {emergency.phone_number}
                                        </td>
                                    </tr>

                                    <!-- Emergency Reason -->
                                    <tr>
                                        <td style="
                                            padding: 14px 18px;
                                            color: #777777;
                                        ">
                                            Emergency Reason
                                        </td>

                                        <td style="
                                            padding: 14px 18px;
                                            font-weight: 600;
                                            color: #333333;
                                        ">
                                            {emergency.emergency_reason}
                                        </td>
                                    </tr>

                                </table>

                                <!-- Action Message -->
                                <table width="100%" cellpadding="0" cellspacing="0" border="0"
                                    style="margin-top: 25px;">
                                    <tr>
                                        <td style="
                                            background-color: #f8fafb;
                                            border-left: 4px solid #0297d1;
                                            padding: 15px 18px;
                                        ">
                                            <p style="
                                                margin: 0;
                                                font-size: 14px;
                                                line-height: 1.5;
                                                color: #555555;
                                            ">
                                                Please review this emergency request
                                                and contact the patient as soon as possible.
                                            </p>
                                        </td>
                                    </tr>
                                </table>

                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td align="center"
                                style="
                                    background-color: #f8fafb;
                                    border-top: 1px solid #eeeeee;
                                    padding: 20px;
                                ">

                                <p style="
                                    margin: 0;
                                    font-size: 12px;
                                    color: #999999;
                                ">
                                    Montreal West Dentistry
                                </p>

                                <p style="
                                    margin: 6px 0 0 0;
                                    font-size: 11px;
                                    color: #aaaaaa;
                                ">
                                    Emergency request generated by AI Receptionist
                                </p>

                            </td>
                        </tr>

                    </table>

                </td>
            </tr>
        </table>

    </body>
    </html>
    """

    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": recipient,
        "subject": f"EMERGENCY REQUEST - {emergency.name}",
        "html": html,
    })




