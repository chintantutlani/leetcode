# from rest_framework import serializers
#
# from problem import models
#
#
# class TagSerilazers(serializers.ModelSerializer):
#     class Meta:
#         model = models.Tag
#         fields = '__all__'
#
#
# class problemSerializer(serializers.ModelSerializer):
#     class Meta:
#         tag = TagSerilazers(many=True)
#         model = models.create_problem
#         fields =['problem', 'Created_at', 'prblm_name']