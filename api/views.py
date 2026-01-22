from rest_framework import status
from django.core.mail import send_mail
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import Portfolio
from .serializers import PortfolioSerializer

# -------------------- PORTFOLIO --------------------

@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def portfolio_list_create(request):
    if request.method == 'GET':
        portfolios = Portfolio.objects.all()
        serializer = PortfolioSerializer(
            portfolios,
            many=True,
            context={"request": request}
        )
        return Response(serializer.data)

    serializer = PortfolioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
def portfolio_detail(request, name):
    try:
        obj = Portfolio.objects.get(name=name)
    except Portfolio.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    serializer = PortfolioSerializer(obj)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def portfolio_update_delete(request, id):
    try:
        obj = Portfolio.objects.get(id=id)
    except Portfolio.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    if request.method == 'PUT':
        serializer = PortfolioSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    obj.delete()
    return Response({"message": "Deleted"}, status=204)


# -------------------- SKILLS --------------------
@api_view(['GET', 'PUT'])
def skills_api(request):
    skill, _ = Skill.objects.get_or_create(id=1)

    if request.method == 'GET':
        return Response(SkillSerializer(skill).data)

    serializer = SkillSerializer(skill, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# -------------------- EXPERIENCE --------------------
@api_view(['GET', 'POST'])
def experience_list_create(request):
    if request.method == 'GET':
        serializer = ExperienceSerializer(Experience.objects.all(), many=True)
        return Response(serializer.data)

    serializer = ExperienceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT', 'DELETE'])
def experience_update_delete(request, id):
    obj = Experience.objects.get(id=id)

    if request.method == 'PUT':
        serializer = ExperienceSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    obj.delete()
    return Response({"message": "Deleted"})


# -------------------- EDUCATION --------------------
@api_view(['GET', 'POST'])
def education_list_create(request):
    if request.method == 'GET':
        return Response(EducationSerializer(Education.objects.all(), many=True).data)

    serializer = EducationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


@api_view(['PUT', 'DELETE'])
def education_update_delete(request, id):
    obj = Education.objects.get(id=id)

    if request.method == 'PUT':
        serializer = EducationSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    obj.delete()
    return Response({"message": "Deleted"})


# -------------------- FEEDBACK --------------------
@api_view(['GET', 'POST'])
def feedback_list_create(request):
    if request.method == 'GET':
        return Response(FeedbackSerializer(Feedback.objects.all(), many=True).data)

    serializer = FeedbackSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


@api_view(['PUT', 'DELETE'])
def feedback_update_delete(request, id):
    obj = Feedback.objects.get(id=id)

    if request.method == 'PUT':
        serializer = FeedbackSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    obj.delete()
    return Response({"message": "Deleted"})


# -------------------- CONTACT --------------------
@api_view(['POST', 'GET'])
def contact_api(request):
    if request.method == 'GET':
        return Response(ContactSerializer(ContactMessage.objects.all(), many=True).data)

    serializer = ContactSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    msg = serializer.save()

    # Email admin
    send_mail(
        "New Contact Message",
        msg.message,
        msg.email,
        ["admin@example.com"],
        fail_silently=True
    )

    # Auto reply
    send_mail(
        "Thanks for contacting me",
        "I received your message and will reply soon.",
        "admin@example.com",
        [msg.email],
        fail_silently=True
    )

    return Response({"message": "Message sent"}, status=201)
