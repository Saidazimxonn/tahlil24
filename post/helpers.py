from  .models import Email

def create_email(post_request):
    email = post_request.get('email', '')
    Email.objects.create(
        email=email,
    )
    