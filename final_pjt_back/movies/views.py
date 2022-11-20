from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieListSerializer, GenreSerializer, MovieSerializer,ReviewSerializer
from .models import Movie_Image, Movie, Review, Genre, Keyword
import random
from django.contrib.auth import get_user_model
# from ..accounts.models import User
# from myapp.models import Entry
from django.db.models import Q


# 랜덤한 하나의 이미지를 딕셔너리에 담아 반환하는 함수
def make_still(movie_id):
    img_serial = Movie_Image.objects.filter(movie_id=movie_id)
    img_ser_len = len(img_serial)
    if img_ser_len < 1:
        return '' 
    rannum = random.randrange(0, img_ser_len)
    stil_image = img_serial[rannum].image_path
    # img_lst = []
    # for im in range(img_ser_len):
    #     img_lst.append({ im : img_serial[im].image_path })
    return stil_image

# ______________________인기순 영화목록 (main)vote_movie______________________
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)

        for i in range(len(serializer.data)):
            if 'movie_key' not in serializer.data[i]:
                serializer.data[i].update(movie_key='')
                continue
            mk = serializer.data[i]['movie_key']
            stil_image = make_still(mk)
            serializer.data[i].update(stil_image=stil_image)
        return Response(serializer.data)

#______________________vote_movie______________________
@api_view(['GET'])
def movie_vote(request):
    if request.method == 'GET':
        movies = Movie.objects.all().order_by('-vote_average')
        serializer = MovieListSerializer(movies, many=True)
        for i in range(len(serializer.data)):
            if 'movie_key' not in serializer.data[i]:
                serializer.data[i].update(movie_key='')
                continue
            mk = serializer.data[i]['movie_key']
            stil_image = make_still(mk)
            serializer.data[i].update(stil_image=stil_image)
        return Response(serializer.data)

#______________________recommend_movie______________________
@api_view(['GET'])
def recommend_movie(request, username):
#     좋아요를 누른 영화는 제거한다(50000)
#       장르별로 가장 많이 나온 장르 10개를 위에서부터 10점씩 준다
#       키워드별로 가장 많이 나온 키워드에 10점씩 준다
#       점수 기반으로 리스트를 정렬한다

    
    userId = get_user_model().objects.filter(username=username)[0].id
    # 1. request.user가 좋아하는 영화 목록을 받는다 == feed와 동일함
    user_like_movie = Movie.objects.filter(movie_like_user=userId)
    user_like_movie_list = MovieListSerializer(user_like_movie, many=True)
    # 1.. 좋아요를 누르지 않은 영화만 가져온다! 
    user_like_non = Movie.objects.filter(~Q(movie_like_user=userId))
    

    # 2. 좋아하는 영화 기반 | 포함된 영화 장르만 리스트로 만든다
    len_likemovies = len(user_like_movie_list.data)
    genres = []
    for l in range(len_likemovies):
        genres += user_like_movie_list.data[l]['genres']
    # 장르의 갯수가 많은 순서로 정렬
    genres_dict = []
    print(genres)
    for l in genres:
        genres_dict.append({l : genres.count(l)})
        print(l, genres.count(l))
        while l in genres:
            genres.remove(l)
    like_genres = list(map(lambda x : Genre.objects.get(pk=x).movie_set.all(), genres))
    #     like_genres = [l for l in like_genres if l not in like_genres]
    # 장르 테이블에서 역참조
        # genre = Genre.objects.get(pk=genre_pk)
        # seri = genre.movie_set.all()
        # # 영화 obj 쿼리셋을 받아서 영화리스트 시리얼라이저 사용
        # serializer = MovieListSerializer(seri, many=True)





    # like_movie = GenreSerializer(like_genres[0],  many=True)
    # like_movies = []
    # for g in like_genres:
    #     like_movies += GenreSerializer(g,  many=True)
    # print(like_movie.data)
    # like_genre_movies = list(map(lambda x : Movie.objects.get(pk=x), like_genres))

    # 3. 해당 리스트에서 키워드가 중복되는 영화들을 우선순위로 보여준다 

    return Response(user_like_movie_list.data)
#______________________movie_detail______________________

@api_view(['GET', 'POST'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        mk = serializer.data['movie_key']

        # 스틸컷 딕셔너리 만들기
        img_serial = Movie_Image.objects.filter(movie_id=mk)
        img_ser_len = len(img_serial)
        img_lst = []
        for im in range(img_ser_len):
            img_lst.append({ im : img_serial[im].image_path })

        sd = dict(serializer.data)
        sd.update(stil_images=img_lst)

        return Response(sd)

#______________________review______________________
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # 이제 댓글은 로그인한 사람만 쓸 수 있어요
def review_create(request, movie_pk):
    print('로그인 되었습니다..............', request.data)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data= request.data)
    if serializer.is_valid(raise_exception=True):
        # user = get_user_model()
        # user = user.objects.get(pk=1)  # ------------------------로그인 기능 구현 후 바꿀 부분
        # serializer.save(movie=movie, write_user=user)
        serializer.save(movie=movie, write_user=request.user)
        # serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# ______________________discovery_movie______________________
@api_view(['GET'])
def discovery_movie_list(request):
    if request.method == 'GET':
        genres = get_list_or_404(Genre)
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def discovery_movie(request, genre_pk):
    if request.method == 'GET':
        # 장르 테이블에서 역참조
        genre = Genre.objects.get(pk=genre_pk)
        seri = genre.movie_set.all()
        # 영화 obj 쿼리셋을 받아서 영화리스트 시리얼라이저 사용
        serializer = MovieListSerializer(seri, many=True)

        for i in range(len(serializer.data)):
            if 'movie_key' not in serializer.data[i]:
                serializer.data[i].update(movie_key='')
                continue
            mk = serializer.data[i]['movie_key']
            stil_image = make_still(mk)
            serializer.data[i].update(stil_image=stil_image)
        return Response(serializer.data)



@api_view(['GET'])
def keyword_movie(request, keyword_pk):
    keyword = Keyword.objects.filter(pk=keyword_pk)
    movie = Movie.objects.filter(keyword= keyword[0])
    serializer = MovieListSerializer(movie, many=True)
    for i in range(len(serializer.data)):
        if 'movie_key' not in serializer.data[i]:
            serializer.data[i].update(movie_key='')
            continue
        mk = serializer.data[i]['movie_key']
        stil_image = make_still(mk)
        serializer.data[i].update(stil_image=stil_image)
    return Response(serializer.data)
#______________________like movie______________________
@api_view(['POST'])
def like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = get_user_model().objects.filter(username=request.user)

        user_id = user[0].id
        if movie.movie_like_user.filter(pk=user_id).exists():
            movie.movie_like_user.remove(request.user)
            status = '싫어하는상태'
        else:
            movie.movie_like_user.add(request.user)
            status = '좋아하는상태'

        data = {
            'status': status
        }
        return Response(data)
        # serializer =MovieSerializer(movie)
        # return Response(serializer.data)