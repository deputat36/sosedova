---
"layout": "default"
"title": "Контакты ипотечного брокера | __BROKER_NAME__"
"description": "Связаться с __BROKER_NAME__: консультация по ипотеке для клиентов\
  \ из любого региона России. Телефон и удобные способы обращения."
"permalink": "/kontakty/"
---

<section class="page-hero section"><p class="eyebrow">На связи с клиентами по всей России</p><h1>Контакты ипотечного брокера</h1><p class="lead">{{ site.data.broker.name }}. {{ site.data.broker.role }}. {{ site.data.broker.experience }}.</p><div class="hero-actions"><a class="btn btn-primary" href="tel:{{ site.data.contacts.phone_e164 }}">{{ site.data.contacts.phone }}</a><a class="btn btn-light" href="{{ '/online-zayavka/' | relative_url }}">Подготовить обращение</a>{% include social-links.html %}</div></section><section class="section split"><div><h2>Как связаться</h2><p>Позвоните или отправьте SMS. В первом сообщении достаточно описать цель покупки и удобное время для связи.</p><p><a class="btn btn-light" href="sms:{{ site.data.contacts.phone_e164 }}">Написать SMS</a></p>{% if site.data.contacts.email != blank %}<p><a href="mailto:{{ site.data.contacts.email | escape }}">{{ site.data.contacts.email | escape }}</a></p>{% endif %}<h2>Место работы</h2><p>{{ site.data.contacts.city }}, {{ site.data.contacts.region }}. {{ site.data.contacts.hours }}.</p><p>Дистанционно работаю с клиентами из любого региона России. Укажите часовой пояс, если он отличается от московского.</p></div><div class="card"><h2>Что рассказать на консультации</h2><ul><li>Какое жильё и в каком регионе хотите купить.</li><li>Примерный бюджет и первоначальный взнос.</li><li>Формат занятости: найм, ИП, самозанятость.</li><li>Были ли обращения в банки и отказы.</li></ul><p>Для первого знакомства документы не нужны.</p></div></section>
