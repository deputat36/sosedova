---
"layout": "default"
"title": "Услуги ипотечного брокера по России | __BROKER_NAME__"
"description": "Подбор ипотеки, семейная ипотека, квартиры, дома, строительство, сложные\
  \ случаи, ИП, самозанятые, рефинансирование и страхование."
"permalink": "/uslugi/"
---

<section class="page-hero section"><p class="eyebrow">Онлайн по всей России</p><h1>Услуги ипотечного брокера</h1><p class="lead">Выберите вашу задачу. На консультации разберём ситуацию и согласуем объём помощи.</p></section><section class="section"><div class="broker-audience">{% for service in site.data.services %}<a class="card" href="{{ '/uslugi/' | append: service.slug | append: '/' | relative_url }}"><h2>{{ service.title }}</h2><p>{{ service.short }}</p><span class="text-link">Подробнее →</span></a>{% endfor %}</div></section><section class="section"><h2>Другие ситуации</h2><div class="grid cards-3">{% for item in site.pages %}{% if item.url contains '/uslugi/' and item.url != '/uslugi/' and item.layout != 'redirect' %}<a class="card" href="{{ item.url | relative_url }}">{{ item.breadcrumb | default: item.h1 | default: item.title | split: '|' | first | replace: ' по России', '' }}</a>{% endif %}{% endfor %}</div></section>
