from django import forms
from django.forms.extras.widgets import SelectDateWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

# For some models 
from datetime import date, timedelta

from models import *
from ldap_student_lookup import get_student_info

from charterclub.models import Prospective

DAYS = [("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday")]


################################################################################
# form for entering a new member into the database
# takes a netid as input as uses ldap lookup (?) to find corresponding
# first name, last name, and graduation year.
################################################################################
class NewMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['netid', 'allow_rsvp', 'house_account']

    def save(self, commit=True):
        newMember = super(NewMemberForm, self).save(commit = False)
        
        student = get_student_info(newMember.netid)
        newMember.first_name = student.first_name
        newMember.last_name = student.last_name
        newMember.year = student.year
        
        if commit:
            newMember.save()

        return newMember

################################################################################
# NewOfficerForm
# form to create a new officer: take an existing member and turn
# them into an officer, adding their title
################################################################################
class NewOfficerForm(forms.ModelForm):
    class Meta:
        model = Officer
        fields = ['position']
        
    member_choice = forms.ModelChoiceField(widget = forms.Select, queryset = Member.objects.all())             

    def save(self, commit=True):
        newOfficer = super(NewOfficerForm, self).save(commit = False)
        member_choice = self.cleaned_data.get("member_choice", None)
        newOfficer.first_name = member_choice.first_name
        newOfficer.last_name = member_choice.last_name
        newOfficer.netid = member_choice.netid
        newOfficer.year = member_choice.year
        newOfficer.house_account = member_choice.house_account
        newOfficer.allow_rsvp = member_choice.allow_rsvp

        if commit:
            newOfficer.save()
        
        return newOfficer

class EditOfficerForm(forms.ModelForm):
    class Meta:
        model = Officer
        fields = ['position']

year = (date.today() + timedelta(days=6*30)).year
years = [year, year+1, year+2, year+3]

YEARS = []

for y in years:
    YEARS.append((y, str(y)))

################################################################################
# MailingListForm
# To add sophomores based on the mailing list
################################################################################
class MailingListForm(forms.Form):
    # Fields of this Form
    netid = forms.CharField(max_length=10)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    year = forms.ChoiceField(widget=forms.Select, choices=YEARS)

    # Submit buttons
    helper = FormHelper()   
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

    # Add sophomores based on the data collected
    def add_soph(self):
        if self.is_valid():
            data = self.cleaned_data
            
            p = Prospective.objects.filter(netid=data['netid'])
            if not p:
                pnew = Prospective(netid=data['netid'],
                                   first_name=data['first_name'],
                                   last_name=data['last_name'],
                                   year=data['year'],
                                   events_attended=0)
                pnew.save()

################################################################################
# For Django Admin
# Form for uploading a list of members
################################################################################
class MemberListForm(forms.Form):
    placeholder = '''Quan, Zhou, quanzhou, 2015, 255.00
    Rory, Fitzpatrick, roryf, 2016, 255.00
    Jeremy, Whitton, jwhitton, 2016, 0.00
    '''.replace('    ','')
    content = forms.CharField(label='content', 
                        max_length=2000,
                        widget=forms.Textarea(attrs={
                        'style' : 'height:480px',
                        'placeholder': placeholder}))
    # Submit buttons
    helper = FormHelper()
    helper.add_input(Submit('submit', 'submit'))

    ## --- User defined Methods -----

    # Check if content has proper character seperated values
    # def clean_content(self):
    #     data = self.cleaned_data['content']
    #     table = []

    #     for row in data:
    #         table.append([l.strip() for l in row.split(',')])
        
    #     # Check that every row can be split into 4 colums
    #     for (i,row) in enumerate(table):
    #         if not len(row) == 4:
    #             raise form.ValidationError('Comma Error: Not enough columns in %s' % data[i])        
    #         if not any(row):
    #             raise form.ValidationError('Comma Error: Empty column in %s' % data[i])        
    #         if not (row[2].isalnum()):
    #             raise form.ValidationError('"%s" is not a valid netid' % row[2])

    #     self.table = table
    #     return data.strip()

    # Tries to parse itself. 
    # If successful, returns the results [was prospective, new member, existing member]
    # If unsuccessful, raises an error
    def parse_content(self):
        results = {}
        self.clean_content()

        # Now try to do lookup for students
        for row in self.table:
            netid = row[2]
            pquery_o = Prospective.objects.filter(netid=netid)
            mquery_o = Member.objects.filter(netid=netid)

            if query_o:
                results[netid] = 'Was Prospective. Points: %s'  % (query_o[0].get_num_points())
            elif mquery_o:
                results[netid] = 'Member "%s" already exists in database' % mquery_o[0].__unicode__()
            else:
                results[netid] = 'Adding New Member'

        return results

        

    # def __init__(self, *args, **kwargs):
    #     super(MemberListForm, self).__init__(*args, **kwargs)
    #     self.helper.form_tag = False

