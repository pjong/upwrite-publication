from django.core.management.base import BaseCommand
from faker import Faker
from news.models import Article
import random
import os
from django.core.files.base import ContentFile
import requests

class Command(BaseCommand):
    help = 'Generate fake articles with images'

    def handle(self, *args, **kwargs):
        fake = Faker()
        sections = ['home', 'regional', 'national', 'editorial', 'provincial', 'legal']

        for _ in range(30):
            title = fake.sentence()
            content = fake.paragraph(nb_sentences=20)
            section = random.choice(sections)

            article = Article.objects.create(
                title=title,
                content=content,
                section=section,
                is_published=True
            )

            # Get random image from Unsplash or placeholder
            image_url = f'https://source.unsplash.com/random/800x600/?news,{section}'
            response = requests.get(image_url)
            if response.status_code == 200:
                image_name = f"{fake.word()}.jpg"
                article.image.save(image_name, ContentFile(response.content), save=True)

        self.stdout.write(self.style.SUCCESS('Successfully created 30 fake articles.'))
