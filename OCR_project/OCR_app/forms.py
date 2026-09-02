from django import forms
from .models import CourseRegistration


class CourseRegistrationForm(forms.ModelForm):

    course = forms.ChoiceField(
        choices=[
            ('Python Programming', 'Python Programming'),
            ('Web Development', 'Web Development'),
            ('Artificial Intelligence', 'Artificial Intelligence'),
        ],
        label='Select Course'
    )
    qualification = forms.ChoiceField(
        choices=[
            ('10th', '10th'),
            ('12th', '12th'),
            ('Diploma', 'Diploma'),
            ('Bachelor Degree', 'Bachelor Degree'),
            ('Master Degree', 'Master Degree'),
            ('Other', 'Other'),
        ],
        label='Select Qualification'
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
        }