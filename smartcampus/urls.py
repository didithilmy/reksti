from django.urls import path
from .views import StudentView, AttendanceRecordView, PostAttendanceRecordView

urlpatterns = [
    path('students/<student_id>/', StudentView.as_view(), name='student-details'),
    path('attendance/<room_no>/<int:from>/<int:to>', AttendanceRecordView.as_view(), name='attendance-record'),
    path('attendance/<room_no>/<password>/', PostAttendanceRecordView.as_view(), name='attendance-create'),

]