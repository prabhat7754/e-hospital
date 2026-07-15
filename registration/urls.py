from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from .views import (
    SignUpView,
    PatientProfileUpdateView,
    DoctorProfileUpdateView,
    PatientDashboardView,
    DoctorDashboardView,
    PatientDetailView,
    MarkHealthDataReviewedView,
    BookDoctorView,
    SubmitReviewView,
    SendUserIdToNodeMCUView,
    ForgotPassword,
    PasswordResetSent,
    ResetPassword,
)

app_name = "registration"

urlpatterns = [
    # Authentication
    path(
        "signup/",
        SignUpView.as_view(),
        name="signup",
    ),

    path(
        "login/",
        LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),

    # Patient
    path(
        "patient/profile/",
        PatientProfileUpdateView.as_view(),
        name="patient-profile",
    ),

    path(
        "patient/dashboard/<int:pk>/",
        PatientDashboardView.as_view(),
        name="patient-dashboard",
    ),

    path(
        "patient/<int:pk>/",
        PatientDetailView.as_view(),
        name="patient-detail",
    ),

    # Doctor
    path(
        "doctor/profile/",
        DoctorProfileUpdateView.as_view(),
        name="doctor-profile",
    ),

    path(
        "doctor/dashboard/",
        DoctorDashboardView.as_view(),
        name="doctor-dashboard",
    ),

    path(
        "book-doctor/",
        BookDoctorView.as_view(),
        name="book-doctor",
    ),

    path(
        "submit-review/",
        SubmitReviewView.as_view(),
        name="submit-review",
    ),

    path(
        "health-data/mark-reviewed/",
        MarkHealthDataReviewedView.as_view(),
        name="mark-reviewed",
    ),

    # Password Reset
    path(
        "forgot-password/",
        ForgotPassword,
        name="forgot-password",
    ),

    path(
        "password-reset-sent/<str:reset_id>/",
        PasswordResetSent,
        name="password-reset-sent",
    ),

    path(
        "reset-password/<str:reset_id>/",
        ResetPassword,
        name="reset-password",
    ),

    # Approval Page
    path(
        "approval_pending/",
        TemplateView.as_view(
            template_name="registration/approval_pending.html"
        ),
        name="approval_pending",
    ),

    # NodeMCU
    path(
        "send-user-id/",
        SendUserIdToNodeMCUView.as_view(),
        name="send_user_id",
    ),
]