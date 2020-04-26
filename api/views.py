from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, ]    # Staff 인증 요청에 한해서 뷰호출 허용


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # url : GET movies/on_now_list/ 현재 상영중인 영화들 조회
    @action(methods=['get'], detail=False, url_path='on-now-list', url_name='on-now-list')
    def on_now_list(self, request):
        mvs = self.get_queryset()
        on_now_mvs = []
        for movie in mvs:
            if movie.is_on_now:
                on_now_mvs.append(movie)
        serializer = self.get_serializer(on_now_mvs, many=True)
        return Response(serializer.data)


class TimeTableViewSet(viewsets.ModelViewSet):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer

    # 모델에 추가하지 않고 볼 수 있도록!
    @action(methods=['get'], detail=True)
    def running_time(self, request, pk):
        mv = self.get_object()
        start_time = mv.start_time
        end_time = mv.end_time
        running_time = end_time - start_time
        return Response("running time : " + str(running_time))


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]    # 비인증 요청에게는 읽기 권한만 허용


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, ]        # 인증된 요청에 한해서 뷰호출 허용: 유저가 존재하고 로그인 되어 있을 경우
