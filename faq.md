---
"layout": "default"
"title": "Вопросы ипотечному брокеру | __BROKER_NAME__"
"description": "Ответы о дистанционной работе по России, подготовке заявки, документах,\
  \ стоимости услуг и помощи после отказа банка."
"permalink": "/faq/"
---

<section class="page-hero section"><p class="eyebrow">Что важно знать заранее</p><h1>Вопросы ипотечному брокеру</h1><p class="lead">Порядок работы, документы и возможности сопровождения.</p></section><section class="section"><div class="faq-list">{% for item in site.data.faq %}<details><summary>{{ item.question }}</summary><p>{{ item.answer }}</p></details>{% endfor %}</div></section>{% include faq-schema.html items=site.data.faq %}<section class="section cta-section"><div><h2>Остались вопросы?</h2><p>Обсудим вашу ситуацию индивидуально.</p></div><a class="btn btn-primary" href="{{ '/online-zayavka/' | relative_url }}">Получить консультацию</a></section>
