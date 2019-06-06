# graph-problem-matplpotlib

## problem
<div dir='rtl' align='right'>
  
شخصی میخواهد کتابی را در مدت چند روز مطالعه کند.
او در نظر دارد که در هر روز تعداد مشخصی از فصل های این کتاب را بخواند با این شرط که اگر در یک روز شروع به خواندن فصلی از کتاب میکند در پایان همان روز آن فصلی را که شروع کرده به اتمام برساند.
  
واضح است که این شخص در یک روز میتواند چند فصل از کتاب را بخواند. و هر فصل از این کتاب دارای تعداد صفحات متفاوتی میباشد. شما باید ترتیبی از مطالعه ی فصل های این کتاب را برای این شخص در هر روز ارائه بدید به
طوری که نوعی توازن در مطالعه ی تعداد صفحات کتاب داشته باشد در یک روز نه زیاد مطالعه کند و نه اینکه در یک روز تعداد صفحات کمی را مطالعه کند).
  
#### راهنمایی
اگر به عنوان مثال کتاب 4 فصل داشته باشد و هر فصل به ترتیب دارای {12-6-5-8 صفحه باشد و بخواهد کتاب را در مدت 3 روز به اتمام برساند این شخص باید به طور میانگین روزانه 10 صفحه از کتاب را بخواند (میانگین صفحه اعشاری نمیشود). بنابراین هدف همانطور که گفته شد باید به گونه ای باشد که خروجی برنامه بگوید در هر روز چه فصولی خوانده شود تا نوعی توازن در مطالعه تعداد صفحات کتاب در هرروز به وجود آید. و مجموع صفحات خوانده شده تا جایی که امکان دارد به میانگین که در این مثال عدد 10 میباشد نزدیک شود. شما باید از یک گراف جهت دار استفاده کنید به طوری که راس های این گراف شماره فصل میباشد و بال های این گراف وزن دار بوده به طوری که مثلا اگر فصل 1 را میخواند و بخواهد فصل 2 را شروع کند باید از راس 1 با پیمایش بالی به وزن 8 به راس 2 برود. و همین طور ادامه پیدا میکند تا به راس نهایی برسد. توجه شود که منظور از راس نهایی راس فصل آخر کتاب نميباشد. بلکه برای مثال گفته شده که 4 فصل دارد .گراف ما 5 راس خواهد داشت که راس اخر همان راس حالت پایانی است. (اتمام صفحات).
  
  
#### نکته

خروجی برنامه باید به گونه ای باشد که مشخص کند در هر روز چه فصولی خوانده میشود. . به همراه پروژه گراف رسم شده نیز باید ارائه شود.

حداقل تعداد فصول كتاب 3 و حداقل تعداد روز ها 2 میباشد که بسته به انتخاب خود میتوانید
برای تعداد صفحات روز-تعداد فصل كتاب. با رعایت حداقل های ذکر شده. عددی را نسبت
دهید.

از روش جستجوی عمقی (DFS) نیز در روند حل مسئله میتوانید استفاده کنید. . هدف از حل مسئله انتخاب فصل های معینی در هر روز میباشد. (بسته به تعداد روز)

</div>
