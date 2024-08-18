from django.shortcuts import render,HttpResponse

# Create your views here.

# 查询字符串的形式1
def book_detail_query_string(request):
    book_id = request.GET.get('id')
    name = request.GET.get('name')
    return HttpResponse(f"您查询的图书id是: {book_id}, 图书名称是：{name}")

# path的形式

def book_detail_path(requset, book_id):
    return HttpResponse(f"您查询的图书id是: {book_id}")

# str类型
def book_str(request, book_id):
    return HttpResponse(f"您查询的图书id是: {book_id}")

# slug类型
def book_slug(request, book_id):
    return HttpResponse(f"您查询的图书id是: {book_id}")

# path类型
def book_path(request, book_id):
    return HttpResponse(f"您查询的图书id是: {book_id}")