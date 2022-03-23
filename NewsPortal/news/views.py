from datetime import datetime
from django.views.generic import ListView, DetailView

from .models import Post


class PostList(ListView):
    model = Post # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html' # имя шаблона, в кот будет лежать HTML, в кот будут все инст-ии о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'#имя списка, в кот будут лежать все объекты
    queryset = Post.objects.order_by('-dateCreation')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context[
            'value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context


# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'






