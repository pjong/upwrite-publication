from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from news.models import Article
from faker import Faker
import random
import requests

# your_app/management/commands/create_fake_articles.py
class Command(BaseCommand):
    help = 'Create fake articles'

    def handle(self, *args, **kwargs):
        fake = Faker()
        sections = ['regional', 'national', 'editorial', 'provincial', 'legal']
        articles = []

        for _ in range(50):
            title = fake.sentence(nb_words=6)
            content = "\n\n".join(fake.paragraphs(nb=5))
            section = random.choice(sections)
            published_at = fake.date_time_between(start_date='-30d', end_date='now')
            image_url = f"https://picsum.photos/seed/{fake.uuid4()}/800/400"

            # Download the image
            response = requests.get(image_url)
            image_name = f"{fake.uuid4()}.jpg"
            image = ContentFile(response.content, image_name)

            articles.append({
                'title': title,
                'content': content,
                'section': section,
                'published_at': published_at,
                'image': image
            })

            Article.objects.create(
                title=title,
                content=content,
                section=section,
                is_published=True,
                image=image
            )

        self.stdout.write(self.style.SUCCESS('Successfully created 50 fake articles'))
