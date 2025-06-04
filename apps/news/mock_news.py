from datetime import datetime

MOCK_NEWS = [
    {
        "id": 1,
        "title": "Pudge",
        "content": "Как без боя...",
        "source": "Кабал",
        "links": [
            {
                "url": "https://dallas.net/dr/dev/359114_preces_for_dry_attributes",
                "description": "Preces for dry attributes"
            }
        ],
        "thanks": ["Доступные Благодари", "Выберимые Благодари"],
        "publication_date": "04.06.2025",
        "status": "draft",
        "image_url": None
    },
    # Добавляйте другие новости по аналогии
]

def get_today_news():
    today = datetime.now().strftime("%d.%m.%Y")
    return [n for n in MOCK_NEWS if n['publication_date'] == today]

def get_all_news():
    return MOCK_NEWS