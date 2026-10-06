from django.shortcuts import render

# Create your views here.
import random
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product  


def products_list(request):
    products = Product.objects.all()

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Список товарів</title>
        <style>
            table { width: 80%; border-collapse: collapse; margin: 20px auto; font-family: Arial, sans-serif; }
            th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
            th { background-color: #4CAF50; color: white; }
            tr:nth-child(even) { background-color: #f2f2f2; }
            h1 { text-align: center; font-family: Arial, sans-serif; }
        </style>
    </head>
    <body>
        <h1>Список товарів / книжок</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Назва / Товар</th>
                    <th>Ціна (грн)</th>
                </tr>
            </thead>
            <tbody>
    """

    for item in products:
        # Припустимо, що у моделі є поля title/name та price
        name = getattr(item, 'title', None) or getattr(item, 'name', f'Товар #{item.pk}')
        price = getattr(item, 'price', 'N/A')
        
        html_content += f"""
            <tr>
                <td>{item.pk}</td>
                <td>{name}</td>
                <td>{price}</td>
            </tr>
        """

    html_content += """
            </tbody>
        </table>
    </body>
    </html>
    """

    return HttpResponse(html_content)


def replenish_products(request, count: int):
    sample_titles = [
        "Кобзар", "Тіні забутих предків", "Захар Беркут", "Місто", 
        "Кайдашева сім'я", "Енеїда", "Ворошиловград", "Intermarium"
    ]
    sample_genres = ["Класика", "Проза", "Історія", "Фантастика", "Драма"]

    created_count = 0
    for _ in range(count):
        random_title = f"{random.choice(sample_titles)} (Видання {random.randint(2020, 2026)})"
        random_price = round(random.uniform(150.0, 800.0), 2)
        random_genre = random.choice(sample_genres)

        Product.objects.create(
            title=random_title,
            price=random_price,
            genre=random_genre,
            year=random.randint(2015, 2026)
        )
        created_count += 1

    return HttpResponse(f"Успішно додано {created_count} нових записів у базу даних.")