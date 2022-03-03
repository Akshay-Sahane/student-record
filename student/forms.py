from django import forms


from .models import Student
class StudentForm(forms.ModelForm):
    SName=forms.CharField(label='Student Name',widget=forms.TextInput(attrs={'placeholder':'enter student name','class':'form-control'}),
        error_messages={'required':'please enter student name'})
    SClass=forms.CharField(label='student class',widget=forms.TextInput(attrs={'placeholder':'enter student class','class':'form-control'}),
        error_messages={'required':'please enter student class'})
    SAge=forms.CharField(label='student age',widget=forms.NumberInput(attrs={'placeholder':'enter student age','class':'form-control'}),
        error_messages={'required':'please enter student age'})
    class Meta:
        model=Student
        fields='__all__'