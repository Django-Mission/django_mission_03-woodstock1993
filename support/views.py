from django.shortcuts import render
from .models import Inquiry
from .serializers import InquirySerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class InquiryList(APIView):
    def get(self, request):
        inquiries = Inquiry.objects.all()
        serializer = InquirySerializer(inquiries, many=True)
        print(serializer)
        return Response(serializer.data)


