# django_api

로그인 기능 △
유저 생성 기능 △
유저 조회 기능 ✓
유저 제거, 수정 기능 ✓

```bash
```


```
#ServerApi\view.py
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_user = data['user_id']
        user_data = StudentUser.objects.get(user_id=search_user)

        if data['user_pw'] == user_data.user_pw:
            return JsonResponse({"Message": "login success"}, status=200)
        else:
            return JsonResponse({"Message" : "login fail"}, status=400)
```
