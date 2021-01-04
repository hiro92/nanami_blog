import logging
from django.urls import reverse_lazy
from django.views import generic
from .forms import InquiryForm
from django.contrib import messages
from .models import Diary

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(generic.ListView):
    model = Diary
    template_name = "index.html"
    paginate_by = 3

    def get_queryset(self):
        diaries = Diary.objects.order_by('created_at')
        return diaries

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class DiaryListView(generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 8

    def get_queryset(self):
        diaries = Diary.objects.order_by('created_at')
        return diaries

class DiaryDetailView(generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'
    slug_field = "title"
    slug_url_kwarg = "title"