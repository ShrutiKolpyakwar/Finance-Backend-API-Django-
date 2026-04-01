from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics
from .models import FinancialRecord, User
from .serializers import FinancialRecordSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsAdmin, IsAnalystOrAdmin
from django.db.models import Sum

# User Management (Admin only)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

# Financial Records
class FinancialRecordViewSet(viewsets.ModelViewSet):
    queryset = FinancialRecord.objects.all()   # ✅ ADD THIS LINE
    serializer_class = FinancialRecordSerializer

    def get_queryset(self):
        queryset = FinancialRecord.objects.all()

        category = self.request.query_params.get('category')
        type = self.request.query_params.get('type')

        if category:
            queryset = queryset.filter(category=category)
        if type:
            queryset = queryset.filter(type=type)

        return queryset
    
# Dashboard API
@api_view(['GET'])
@permission_classes([IsAnalystOrAdmin])
def dashboard_summary(request):
    total_income = FinancialRecord.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = FinancialRecord.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

    return Response({
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense
    })
    