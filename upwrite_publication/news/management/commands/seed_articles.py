from django.core.management.base import BaseCommand
from news.models import Article
from faker import Faker
import random
import os
from django.core.files import File

fake = Faker()

SECTIONS = ['regional', 'national', 'editorial', 'provincial', 'legal']

class Command(BaseCommand):
    help = 'Seed the database with dummy articles and images'

    def handle(self, *args, **kwargs):
        Article.objects.all().delete()
        for _ in range(30):
            title = fake.sentence(nb_words=6)
            content = fake.paragraph(nb_sentences=20)
            section = random.choice(SECTIONS)
            image_path = os.path.join('static', 'news', 'placeholder.jpg')

            with open(image_path, 'rb') as image_file:
                article = Article(
                    title=title,
                    content=content,
                    section=section,
                    is_published=True
                )
                article.image.save(f"{fake.slug()}.jpg", File(image_file), save=True)
        self.stdout.write(self.style.SUCCESS('Dummy articles created!'))
