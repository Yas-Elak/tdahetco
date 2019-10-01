"""Streamfield live in here"""

from wagtail.core import blocks


class TitleAndTextTextBlock(blocks.TextBlock):
    """Title and text and nothing else"""

    title = blocks.CharBlock(
        required=True,
        help_text="Ajouter votre titre")
    text = blocks.TextBlock(required=True, help_text="Ajouter le contenu du paragraphe")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Titret et contenu"


class TextRichTextBlock(blocks.RichTextBlock):
    """Title and text and nothing else"""

    text = blocks.RichTextBlock(
        required=True,
        help_text="Ajouter le texte")

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Text"



