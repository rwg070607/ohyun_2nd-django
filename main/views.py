from django.shortcuts import render
from django.http import HttpResponse

grade_db = [
  {
    "_id": "c0caaf80-4dd7-470b-A22a-f4ad48b412d7",
    "index": "1",
    "teacher": "리서인",
    "phone": "010-7101-1635",
    "grade": "2",
    "class": "5",
    "lorem": "방황하였으며 이것은 행위는 쉬이 전제가 재적의원 소리다이것은 간에. 사람은 군무원이"
  },
  {
    "_id": "d66c7ad2-7a2d-4c51-Cbeb-3279d142ff50",
    "index": "2",
    "teacher": "전하라",
    "phone": "010-5392-2328",
    "grade": "3",
    "class": "10",
    "lorem": "노력하고 요구에 후임자를 선서를 변호인을 변호인의 붙인다 법률을. 없다 거듭"
  },
  {
    "_id": "cd1e1a16-6fed-4f9d-C97d-4a56c8080ea6",
    "index": "3",
    "teacher": "탄도빈",
    "phone": "010-7713-5796",
    "grade": "2",
    "class": "10",
    "lorem": "가지에 열매를 60일 국군의 대한 용기가 발할 권한에. 구할 파란"
  },
  {
    "_id": "e9f3d448-8b08-406b-Ba01-d8093e640dce",
    "index": "4",
    "teacher": "난리한",
    "phone": "010-9907-1429",
    "grade": "3",
    "class": "11",
    "lorem": "중립성은 재의의 재판관의 문서로써 써 새로 인간이 여부가. 새가 속하는"
  },
  {
    "_id": "f034a820-66d8-45ce-Ca87-396aa3b6bfcd",
    "index": "5",
    "teacher": "옥로은",
    "phone": "010-2438-5691",
    "grade": "1",
    "class": "9",
    "lorem": "밝은 싹이 제한 가득 국무회의는 기반이 관리 신속한. 이상이 가져야"
  }
]

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def jejuohyun(request):
    return render(request, 'main/jejuohyun.html')

def grade(request):
    return render(request, 'main/grade.html')

def my_page(request):
    return render(request, 'main/my_page.html')
