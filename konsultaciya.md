---
layout: "default"
title: "Онлайн-консультация ипотечного брокера | __BROKER_NAME__"
description: "Бесплатная первичная онлайн-консультация ипотечного брокера из любого города: платеж, взнос, документы, риски отказа и следующий шаг."
permalink: "/konsultaciya/"
breadcrumb: "Консультация"
og_type: "article"
schema: '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Сколько стоит первичная консультация ипотечного брокера?","acceptedAnswer":{"@type":"Answer","text":"Стоимость и состав помощи согласуются до начала работы."}},{"@type":"Question","name":"Можно ли обратиться из другого города?","acceptedAnswer":{"@type":"Answer","text":"Да. Первичный разбор можно провести дистанционно из любого города. Возможность дальнейшего сопровождения зависит от банка, региона, объекта и задачи."}},{"@type":"Question","name":"Как получить консультацию?","acceptedAnswer":{"@type":"Answer","text":"Можно заполнить онлайн-заявку, позвонить по номеру 8 903 025-08-07, написать в MAX по этому номеру или обратиться на страницу ВКонтакте."}}]}'
---

<section class="page-hero section">
  <p class="eyebrow">Первичный разбор по договорённости · онлайн из любого города</p>
  <h1>Онлайн-консультация ипотечного брокера</h1>
  <p class="lead">Помогу понять, с чего начать ипотеку, какой платеж ориентировочно подходит, какие риски могут помешать одобрению и нужен ли вам полный подбор банка.</p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="{{ '/online-zayavka/' | relative_url }}?source={{ page.url | url_encode }}&amp;scenario={{ 'Первичная консультация и подбор ипотеки' | url_encode }}">Заполнить онлайн-заявку</a>
    <a class="btn btn-light" href="tel:{{ site.data.contacts.phone_e164 }}">Позвонить</a>
    
    {% include social-links.html %}
  </div>
</section>

<section class="section compact-section" id="zayavka">
  <div class="notice">
    <div>
      <p class="eyebrow">Онлайн-обращение</p>
      <h2>Передайте основные вводные через анкету</h2>
      <p>Укажите любой город или населённый пункт, тип объекта, примерную стоимость, первоначальный взнос, доход и были ли заявки или отказы. Сайт подготовит структурированный текст для отправки удобным способом.</p>
      <p>Не отправляйте персональные документы в открытые комментарии или незнакомые чаты. На первом этапе достаточно краткого описания ситуации, а порядок передачи документов лучше согласовать отдельно.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-primary" href="{{ '/online-zayavka/' | relative_url }}?source={{ page.url | url_encode }}&amp;scenario={{ 'Первичная консультация и подбор ипотеки' | url_encode }}">Перейти к анкете</a>
      <a class="btn btn-dark" href="tel:{{ site.data.contacts.phone_e164 }}">Позвонить</a>
    </div>
  </div>
</section>

<section class="section muted">
  <div class="section-head">
    <p class="eyebrow">Что разберем</p>
    <h2>На первичной консультации</h2>
    <p>Консультация помогает быстро увидеть реальную картину и выбрать следующий шаг. Окончательное решение по ипотеке всегда принимает банк.</p>
  </div>
  <div class="grid cards-4">
    <article class="card"><h3>Цель покупки</h3><p>Квартира, дом, новостройка, вторичка, строительство, материнский капитал или семейная ипотека.</p></article>
    <article class="card"><h3>Доход и нагрузку</h3><p>Как банк может смотреть на платежеспособность, действующие кредиты и формат дохода.</p></article>
    <article class="card"><h3>Риски отказа</h3><p>Что проверить до подачи заявки: кредитную историю, просрочки, частые запросы, состав заемщиков.</p></article>
    <article class="card"><h3>Следующий шаг</h3><p>Консультация, подбор, подготовка документов, проверка истории или пауза перед новой заявкой.</p></article>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <p class="eyebrow">География</p>
    <h2>Первичный разбор доступен из любого региона</h2>
    <p>Обратиться дистанционно можно из любого города. Дальнейший формат зависит от региона, банка, объекта и объёма необходимой работы.</p>
  </div>
  <div class="grid cards-4">
    <article class="card"><h3>Ваш город</h3><p>Укажите место проживания и где находится объект. Эти адреса могут не совпадать.</p></article>
    <article class="card"><h3>Онлайн-разбор</h3><p>Первичные вводные можно передать через форму, по телефону или в переписке.</p></article>
    <article class="card"><h3>Документы позже</h3><p>На первом этапе не требуется отправлять паспорт и полные банковские документы.</p></article>
    <article class="card"><h3>Формат работы</h3><p>После разбора станет понятно, возможна ли дальнейшая дистанционная помощь по вашей задаче.</p></article>
  </div>
</section>

<section class="section muted">
  <div class="section-head">
    <p class="eyebrow">Что написать</p>
    <h2>Шаблон первого сообщения</h2>
    <p>Можно отправить в MAX или ВКонтакте такой текст и заменить данные на свои.</p>
  </div>
  <div class="notice">
    <div>
      <p><strong>Здравствуйте, {{ site.data.broker.first_name }}. Хочу проконсультироваться по ипотеке.</strong></p>
      <p>Город: ___. Объект: квартира / дом / новостройка / строительство. Стоимость примерно: ___ ₽. Первоначальный взнос: ___ ₽. Доход: официально / ИП / самозанятость / другой вариант. Были ли заявки или отказы: да / нет.</p>
    </div>
    <a class="btn btn-dark" href="{{ '/online-zayavka/' | relative_url }}?source={{ page.url | url_encode }}&amp;scenario={{ 'Первичная консультация и подбор ипотеки' | url_encode }}">Заполнить готовую форму</a>
  </div>
</section>



<section class="section cta-section">
  <div>
    <p class="eyebrow">Начать онлайн</p>
    <h2>Передайте вводные удобным способом</h2>
    <p>Заполните анкету из любого города или позвоните, если нужен короткий первичный ответ.</p>
  </div>
  <div class="cta-actions">
    <a class="btn btn-primary" href="{{ '/online-zayavka/' | relative_url }}?source={{ page.url | url_encode }}&amp;scenario={{ 'Первичная консультация и подбор ипотеки' | url_encode }}">Онлайн-заявка</a>
    <a class="btn btn-secondary" href="tel:{{ site.data.contacts.phone_e164 }}">{{ site.data.contacts.phone }}</a>
    
    {% include social-links.html %}
  </div>
</section>
