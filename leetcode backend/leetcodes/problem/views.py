
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from problem import models, serializer
import sqlite3

#
# @api_view(['GET','POST'])
# def drf_get_create(request):
#     if request.method =="GET":
#         all_problem=models.create_problem.objects.all()
#         serialized_data = serializer.problemSerializer(all_problem)
#         return Response(data={'problem':serialized_data.data})
#     else:
#         problem_obj = serializer.problemSerializer(data=request.data)
#         if problem_obj.is_valid():
#             problem_obj.save()
#             return Response(data={"data":problem_obj.data})
#         return Response(data={"error":problem_obj.errors})
#
# @api_view(['GET','PUT','DELETE'])
# def drf_get_put_delete(request,id):
#     if request.method == "GET":
#         try:
#             problem_1 = models.create_problem.objects.get(id=id)
#             serializer_data= serializer.problemSerializer(problem_1)
#             return Response(data = serializer_data.data)
#         except models.create_problem.DoesNotExist:
#             return Response(data={'msg':'problem does not exits'})
#     elif request.method == "PUT":
#
#         old_problem = models.create_problem.objects.get(id=id)
#         new_problem_data = serializer.problemSerializer(old_problem,request.data)
#         if new_problem_data.is_valid():
#             new_problem_data.save()
#             return Response(data ={'data': new_problem_data.data})
#         return Response(data={"error": new_problem_data.errors})
#
#     elif request.method == 'DELETE':
#         try:
#             delete_problem = models.create_problem.objects.get(id=id)
#             delete_problem.delete()
#             delete_problem.save()
#             return Response(data={"msg": "problem deleted"})
#         except models.create_problem.DoesNotExist:
#             return Response(data={'msg': 'problem doesnot exits'})
#


class problemGetOrCreate(APIView):
    def get(self,request):
        con = sqlite3.connect("db.sqlite3")
        c = con.cursor()
        c.execute("SELECT * from problem_create_problem")
        data = c.fetchall()
        print("======>",data)
        con.commit()
        con.close()
        # all_problem = models.create_problem.objects.all()
        # serialized_data = serializer.problemSerializer(all_problem, many=True)
        arr = []
        for i in data:
            arr.append({
                        'prblm_name':i[1],
                        'problem':i[2],
                        'Created_at':i[3],
                        'updated_at': i[4]


                        })

        print("============>",)
        return Response(data={'problem': arr})

    def post(self,request):
        req_data = request.data
        con = sqlite3.connect("db.sqlite3")
        c = con.cursor()
        problem_name = req_data['prblm_name']
        problem_add = req_data['problem']
        created_at =req_data[ 'Created_at']
        updated =  req_data[ 'updated_at']
        data_tuple = ( problem_name,problem_add,created_at, updated)
        c.execute("INSERT INTO problem_create_problem (prblm_name,problem,Created_at,updated_at) VALUES(?,?,?,?)",data_tuple)
        con.commit()
        con.close()
        return Response(data={"data": "data saved"})
        # problem_obj = serializer.problemSerializer(data=request.data)
        # if problem_obj.is_valid():
        # #     problem_obj.save()
        # return Response(data={"data": data})
        # return Response(data={"error": data.errors})


class problemDetailsGetPutDelete(APIView):
    def get(self,request,id):
        con = sqlite3.connect("db.sqlite3")
        c = con.cursor()
        c.execute("SELECT * FROM problem_create_problem WHERE id =?",[id])
        data = c.fetchone()
        print("=========================>",data)
        con.commit()
        con.close()
        # try:
        #     problem_1 = models.create_problem.objects.get(id=id)
        #     serializer_data= serializer.problemSerializer(problem_1)
        #     return Response(data = serializer_data.data)
        # except models.create_problem.DoesNotExist:
        return Response(data={'problem': data})

    def put(self,request,id):
        req_data = request.data
        con = sqlite3.connect("db.sqlite3")
        c = con.cursor()
        problem_name = req_data['prblm_name']
        problem_add = req_data['problem']
        created_at = req_data['Created_at']
        updated = req_data['updated_at']
        data_tuple = (problem_name, problem_add, created_at, updated)

        my_query = ("UPDATE problem_create_problem SET prblm_name=?,problem=?,Created_at=?,updated_at=?  WHERE  id=?")

        c.execute(my_query,(problem_name, problem_add, created_at, updated,id))
        data = c.fetchone()
        print("======>", data)
        con.commit()
        con.close()
        # old_problem = models.create_problem.objects.get(id=id)
        # new_problem_data = serializer.problemSerializer(old_problem, request.data)
        # if new_problem_data.is_valid():
        #     new_problem_data.save()
        #     return Response(data={'data': new_problem_data.data})
        return Response(data={"error": "done update"})

    def delete(self,request,id):
        con = sqlite3.connect("db.sqlite3")
        c = con.cursor()
        c.execute("DELETE  FROM problem_create_problem WHERE id=?",[id])
        data = c.fetchone()
        print("=>", data)
        con.commit()
        con.close()
        # try:
        #     delete_problem = models.create_problem.objects.get(id=id)
        #     delete_problem.delete()
        #
        #     return Response(data={"msg": "problem deleted"})
        # except models.create_problem.DoesNotExist:
        return Response(data={'msg': ' deleted'})

