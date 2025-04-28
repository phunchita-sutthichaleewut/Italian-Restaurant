from django import forms
from .models import JodApplication

ROOM_TYPE_CHOICES = [
    ('private', 'ห้องส่วนตัว'),
    ('shared', 'ห้องรวม'),
    ('vip', 'ห้อง VIP'),
]

ROOM_SIZE_CHOICES = [
    ('small', 'เล็ก (2-4 คน)'),
    ('medium', 'กลาง (5-8 คน)'),
    ('large', 'ใหญ่ (9-12 คน)'),
]

TIME_CHOICES = [
    ('10:00', '10:00 - 11:00'),
    ('12:00', '12:00 - 13:00'),
    ('14:00', '14:00 - 15:00'),
    ('18:00', '18:00 - 19:00'),
]

SET_CHOICES = [
    ('SET A', 'SET A (Price = 1000)'),
    ('SET B', 'SET B (Price = 1500)'),
    ('SET C', 'SER C (Price = 2000)'),
]

class JodApplicationForm(forms.ModelForm):
    room_type = forms.ChoiceField(choices=ROOM_TYPE_CHOICES, widget=forms.Select())
    room_size = forms.ChoiceField(choices=ROOM_SIZE_CHOICES, widget=forms.Select())
    booking_time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select())
    set_food = forms.ChoiceField(choices=SET_CHOICES, widget=forms.Select())  # ✅ เพิ่มบรรทัดนี้
    booking_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = JodApplication
        fields = [
            'first_name', 'last_name', 'email', 'phone_number',
            'room_type', 'room_size', 'set_food',
            'booking_date', 'booking_time', 'application_status'
        ]
        widgets = {
            'application_status': forms.Select(choices=JodApplication.STATUS_CHOICES),
        }
