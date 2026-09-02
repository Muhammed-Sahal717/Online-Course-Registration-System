from django import forms
from .models import CourseRegistration


class CourseRegistrationForm(forms.ModelForm):

    course = forms.ChoiceField(
        choices=[
            ('Python Programming', 'Python Programming'),
            ('Web Development', 'Web Development'),
            ('Data Science', 'Data Science'),
            ('Artificial Intelligence', 'Artificial Intelligence'),
            ('Database Management', 'Database Management'),
        ],
        label='Select Course'
    )

    class Meta:
        model = CourseRegistration

        fields = [
            'student_name',
            'email',
            'phone',
            'course',
            'qualification',
            'profile_photo',
        ]

        widgets = {
            'student_name': forms.TextInput(attrs={
                'placeholder': 'Enter your name'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email'
            }),

            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter your phone number'
            }),

            'qualification': forms.TextInput(attrs={
                'placeholder': 'Enter your qualification'
            }),
        }