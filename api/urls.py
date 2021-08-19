from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import PollViewSet, QuestionViewSet, AnswerViewSet, ChoicesViewSet, AnswersByID

router = routers.SimpleRouter()
router.register(r'polls', PollViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'choices', ChoicesViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('login/', obtain_auth_token, name='login'),
    path('answer_user/<int:pk>/', AnswersByID.as_view())
]
