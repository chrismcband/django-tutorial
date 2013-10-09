from django.db.models import Model, CharField, EmailField,\
    CommaSeparatedIntegerField

# Create your models here.
class Signup(Model):
    USE_PLANNING_CONSULTATION = 1
    USE_NEIGHBOURHOOD_PLANNING = 2
    USE_ARTS_AND_CULTURAL_ENGAGEMENT = 3
    USE_COLLABORATIVE_DESIGN_REVIEW = 4
    USE_PROPERTY_MARKETING = 5
    USE_EDUCATION = 6
    USE_OTHER = 7
    USE_CHOICES = (
        (USE_PLANNING_CONSULTATION, 'Planning Consultation'),
        (USE_NEIGHBOURHOOD_PLANNING, 'Neighbourhood Planning'),
        (USE_ARTS_AND_CULTURAL_ENGAGEMENT, 'Arts and Cultural Planning'),
        (USE_PROPERTY_MARKETING, 'Property Marketing'),
        (USE_EDUCATION, 'Education'),
        (USE_OTHER, 'Other')
    )

    FEEDBACK_FRIENDS_AND_COLLEAGUES = 1
    FEEDBACK_CLIENTS_AND_CUSTOMERS = 2
    FEEDBACK_ALL_STAFF = 3
    FEEDBACK_LOCAL_COMMUNITY = 4
    FEEDBACK_ANYONE = 5
    FEEDBACK_CHOICES = (
        (FEEDBACK_FRIENDS_AND_COLLEAGUES, 'Friends and colleagues'),
        (FEEDBACK_CLIENTS_AND_CUSTOMERS, 'Clients and customers'),
        (FEEDBACK_ALL_STAFF, 'All staff'),
        (FEEDBACK_LOCAL_COMMUNITY, 'Local community'),
        (FEEDBACK_ANYONE, "Anyone - we're really social")
    )

    FIND_BY_EMAIL_INVITE = 1
    FIND_IN_MY_WEBSITE = 2
    FIND_IN_MY_INTRANET = 3
    FIND_ON_STICKYWORLD = 4
    FIND_CHOICES = (
        (FIND_BY_EMAIL_INVITE, 'By email invite'),
        (FIND_IN_MY_WEBSITE, 'In my website'),
        (FIND_IN_MY_INTRANET, 'In my intranet'),
        (FIND_ON_STICKYWORLD, 'On stickyworld.com')
    )

    firstname = CharField(max_length=50)
    lastname = CharField(max_length=50)
    email = EmailField(max_length=254)
    password = CharField(max_length=100)
    subdomain = CharField(max_length=75)
    use = CommaSeparatedIntegerField(max_length=8, choices=USE_CHOICES)
    seek_feedback = CommaSeparatedIntegerField(max_length=8, choices=FEEDBACK_CHOICES)
    find_world = CommaSeparatedIntegerField(max_length=8, choices=FIND_CHOICES)

