from django.urls import path

from . import views

# 设置命名空间app_name，以便于在模板中指定对应空间下的url名称
app_name = 'polls'

# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

# 使用通用视图，改良urlconf。
# 第二个和第三个匹配准则中，路径字符串中匹配模式的名称已经由 <question_id> 改为 <pk>  (即primary_key)
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]