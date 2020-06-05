from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from job_app.apis.serializers import CategoryListSerializer, JobsSerializer
from django.utils.text import slugify
from rest_framework_simplejwt.authentication import JWTAuthentication


class CategoryListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryListSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class JobsListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = JobsSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class JobsRetriveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = JobsSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class JobsCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = JobsSerializer
    # model = serializer_class.Meta.model
    # queryset = model.objects.all()

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data["title"]
        slug = slugify(title)
        author = self.request.user
        serializer.save(author=author, slug=slug)
        return serializer


class JobsDestroyAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = JobsSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()