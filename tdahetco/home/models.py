import datetime

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.blocks import StreamBlock

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel, \
    FieldRowPanel
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.snippets.models import register_snippet
from wagtailcaptcha.models import WagtailCaptchaEmailForm

# from articles.models import Article
# from articles.models import Article
from django import forms
from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', related_name='custom_form_fields')


class ContactPage(WagtailCaptchaEmailForm):
    templates = "home/contact_page.html"

    max_count = 1

    thank_you_text = RichTextField(blank=True)
    intro = RichTextField(blank=True, null=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('custom_form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email Notification Config"),
    ]

    def get_form_fields(self):
        return self.custom_form_fields.all()


class HomePage(Page):
    """Home page Model"""

    max_count = 1

    templates = "home/home_page.html"

    titre_partie_une = models.CharField(max_length=255, blank=False, null=True)
    titre_partie_deux = models.CharField(max_length=255, blank=False, null=True)
    titre_partie_trois = models.CharField(max_length=255, blank=False, null=True)
    contenu_partie_une = RichTextField(null=True)
    contenu_partie_deux = RichTextField(null=True)
    contenu_partie_trois = RichTextField(null=True)
    contenu_partie_presentation = RichTextField(null=True)
    titre_cta_formation = models.CharField(max_length=255, blank=False, null=True)
    bouton_cta_formation = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Bouton appelant la page des formation"
    )

    image_partie_une = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    image_parallax = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    image_partie_trois = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("titre_partie_une"),
            FieldPanel("contenu_partie_une"),
            ImageChooserPanel("image_partie_une"),
        ], heading="Partie une"),
        ImageChooserPanel("image_parallax"),
        MultiFieldPanel([
            FieldPanel("titre_partie_deux"),
            FieldPanel("contenu_partie_deux"),
        ], heading="Partie deux"),
        MultiFieldPanel([
            FieldPanel("titre_partie_trois"),
            FieldPanel("contenu_partie_trois"),
            ImageChooserPanel("image_partie_trois"),
        ], heading="Partie trois"),
        MultiFieldPanel([
            FieldPanel("titre_cta_formation"),
            PageChooserPanel("bouton_cta_formation"),
        ], heading="Call ot action"),
        MultiFieldPanel([
            FieldPanel("contenu_partie_presentation"),
        ], heading="Présentation"),

    ]

    def get_recent_blogs(self):
        max_count = 2  # max count for displaying post
        return Article.objects.all().order_by('-date')[:max_count]

        # add this to custom context

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request)
        context['article'] = self.get_recent_blogs()
        return context



class Formations_individuelles(Page):
    """Formations page Model"""

    max_count = 1

    templates = "home/formations_individuelles.html"

    titre_partie_une_a = models.CharField(max_length=255, blank=False, null=True)
    titre_partie_une_b = models.CharField(max_length=255, blank=True, null=True)
    contenu_partie_une = RichTextField(null=True)

    titre_partie_deux = models.CharField(max_length=255, blank=False, null=True)
    contenu_partie_deux = RichTextField(null=True)

    titre_partie_trois = models.CharField(max_length=255, blank=False, null=True)
    contenu_partie_trois = RichTextField(null=True)

    titre_partie_theme = models.CharField(max_length=255, blank=False, null=True)
    contenu_theme_a = RichTextField(null=True)
    contenu_theme_b = RichTextField(null=True)


    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("titre_partie_une_a"),
            FieldPanel("titre_partie_une_b"),
            FieldPanel("contenu_partie_une"),
        ], heading="Partie une"),
        MultiFieldPanel([
            FieldPanel("titre_partie_deux"),
            FieldPanel("contenu_partie_deux"),
        ], heading="Partie deux"),
        MultiFieldPanel([
            FieldPanel("titre_partie_trois"),
            FieldPanel("contenu_partie_trois"),
        ], heading="Partie trois"),
        MultiFieldPanel([
            FieldPanel("titre_partie_theme"),
            FieldPanel("contenu_theme_a"),
            FieldPanel("contenu_theme_b"),

        ], heading="Thèmes"),
    ]

class Formations_groupes(Page):
    """Formations page Model"""

    max_count = 1

    templates = "home/formations_groupes.html"

    titre_partie_une_a = models.CharField(max_length=255, blank=False, null=True)
    contenu_partie_une = RichTextField(null=True)

    titre_partie_deux = models.CharField(max_length=255, blank=False, null=True)
    contenu_partie_deux = RichTextField(null=True)

    titre_partie_trois = models.CharField(max_length=255, blank=False, null=True)
    contenu_partie_trois = RichTextField(null=True)

    titre_partie_theme = models.CharField(max_length=255, blank=False, null=True)
    contenu_theme_a = RichTextField(null=True)
    contenu_theme_b = RichTextField(null=True)


    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("titre_partie_une_a"),
            FieldPanel("contenu_partie_une"),
        ], heading="Partie une"),
        MultiFieldPanel([
            FieldPanel("titre_partie_deux"),
            FieldPanel("contenu_partie_deux"),
        ], heading="Partie deux"),
        MultiFieldPanel([
            FieldPanel("titre_partie_trois"),
            FieldPanel("contenu_partie_trois"),
        ], heading="Partie trois"),
        MultiFieldPanel([
            FieldPanel("titre_partie_theme"),
            FieldPanel("contenu_theme_a"),
            FieldPanel("contenu_theme_b"),

        ], heading="Thèmes"),
    ]


class Formatrice(Page):
    """Formations page Model"""

    max_count = 1

    templates = "home/formatrice.html"

    contenu_partie_une = RichTextField(null=True)

    titre_partie_deux = models.CharField(max_length=255, blank=False, null=True)

    titre_tab_a = models.CharField(max_length=255, blank=False, null=True)
    titre_tab_b = models.CharField(max_length=255, blank=False, null=True)
    titre_tab_c = models.CharField(max_length=255, blank=False, null=True)
    titre_tab_d = models.CharField(max_length=255, blank=False, null=True)

    contenu_tab_a = RichTextField(null=True)
    contenu_tab_b = RichTextField(null=True)
    contenu_tab_c = RichTextField(null=True)
    contenu_tab_d = RichTextField(null=True)


    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("contenu_partie_une"),
        ], heading="Partie une"),
        MultiFieldPanel([
            FieldPanel("titre_partie_deux"),
        ], heading="Partie deux"),
        MultiFieldPanel([
            FieldPanel("titre_tab_a"),
            FieldPanel("contenu_tab_a"),
        ], heading="Onglet 1"),
        MultiFieldPanel([
            FieldPanel("titre_tab_b"),
            FieldPanel("contenu_tab_b"),
        ], heading="Onglet 2"),
        MultiFieldPanel([
            FieldPanel("titre_tab_c"),
            FieldPanel("contenu_tab_c"),
        ], heading="Onglet 3"),
        MultiFieldPanel([
            FieldPanel("titre_tab_d"),
            FieldPanel("contenu_tab_d"),
        ], heading="Onglet 4"),
    ]



class Activites(Page):
    """activites page Model"""

    max_count = 1

    templates = "home/activites.html"

    titre_partie_une = models.CharField(max_length=255, blank=False, null=True)
    contenu_partie_une = RichTextField(null=True)

    contenu_partie_deux = RichTextField(null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("titre_partie_une"),
            FieldPanel("contenu_partie_une"),
        ], heading="Partie une"),
        MultiFieldPanel([
            FieldPanel("contenu_partie_deux"),
        ], heading="NB"),
    ]

class Formation_Redirect(Page):
    """page redirigées vers la formation individuelles"""

    max_count = 1


@register_snippet
class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text='A slug to identify posts by this category',
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class ArticlesListingPage(Page):
    """List all the articles"""

    max_count = 1
    template = "home/articles.html"

    custom_title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Ecraser le titre par défaut"
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["articles"] = Article.objects.live().public()
        context["categories"] = ArticleCategory.objects.all()
        return context


class Article(Page):

    template = "home/article.html"
    categories = ParentalManyToManyField("home.ArticleCategory", blank=True)

    auteur = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField("Post date", default=datetime.date.today)
    article_description = models.CharField(max_length=255, null=True, blank=True)


    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock(icon="image")),
        ('embedded_video', EmbedBlock(icon="media")),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('article_description'),
        MultiFieldPanel(
            [
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Categories"
        ),
        ImageChooserPanel("banner_image"),
        StreamFieldPanel('body'),
        FieldPanel('auteur'),
        FieldPanel('date')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["articles"] = Article.objects.live().public()
        context["categories"] = ArticleCategory.objects.all()

        return context
