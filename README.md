<div dir="rtl">

# 🚀 הצעה למחקר דוקטורט: השפעות פיננסיות של אירועי בטיחות בתעשיות התעופה והחלל

## 🎯 מטרת המסמך

המסמך מציג שלוש חלופות מחקר סביב אותה שאלה כלכלית: כיצד אירוע בטיחותי משפיע על החברה המעורבת, על מתחרותיה ועל חברות החשופות לאותם שווקים או לקוחות.

המטרה בשלב זה אינה לאשר מסלול מראש, אלא **לבצע בדיקת היתכנות ממוקדת לכל חלופה, להשוות ביניהן, ואז לבחור את מסלול הדוקטורט**.

## 📖 נקודת המוצא המתודולוגית

המאמר המרכזי הוא [Bosch, Eckard & Singal (1998), *The Competitive Impact of Air Crashes: Stock Market Evidence*](literature/README.md).

המאמר בוחן את תגובת מחירי המניות להתרסקויות מטוסים קטלניות. הוא מבחין בין שני מנגנונים אפשריים: מעבר לקוחות למתחרות (switching) ופגיעה כלל־ענפית (negative spillover).

המדד המרכזי, `PCTLAP`, הוא שיעור ה־RPM של חברת תעופה שאינה מעורבת בהתרסקות, שמקורו בקווים שהיא חולקת עם חברת התעופה שהתרסקה.

## 🛤️ שלוש חלופות מחקר

| Option | Research question | Advantages | Limitations | Available now | Missing / next step |
| --- | --- | --- | --- | --- | --- |
| **1. Original-paper replication + IV** | Can the Bosch, Eckard & Singal results be replicated and extended with implied volatility? | Direct link to an established paper; strongest identification benchmark; can validate the full research pipeline. | Exact replication may depend on unavailable author data, code, and undocumented implementation choices. | NBER DB1A ticket archive, key paper, and an initial quarterly analysis. | Contact [Vijay Singal](https://experts.vt.edu/3354-vijay-singal) for replication data/code and PCTLAP clarification; obtain returns and IV. |
| **2. Later aviation-event extension** | Does the aviation mechanism persist for later events when returns and IV are analysed jointly? | Retains the original economic setting while producing a more current sample. | Less differentiated; requires comparable post-2016 airline data and a defensible event definition. | Historical NBER data through 2016Q3 and the original study's framework. | Download later DB1B quarters, construct the event sample and PCTLAP, and obtain returns and IV. |
| **3. Space-launch-failure extension** | Do launch failures affect returns and IV of the failing firm, competitors, and related contractors? | Potentially original setting; a reproducible failure-event universe already exists; clear opportunity to develop a new exposure measure. | Exposure may be difficult to map because relevant firms can be private, diversified, or indirectly affected. | ESA DISCOS extract with 119 failure-flagged launches since 2000. | Build company/ticker exposure mapping, obtain returns and IV, and construct/validate `ContractOverlap`. |

## 🧭 תהליך העבודה המוצע

כדי שלא להשאיר אף חלופה ללא המשך ברור, יבוצעו שלושה צעדי היתכנות קצרים במקביל:

1. **חלופה 1 — בירור שחזור מדויק:** לפנות ל־[Vijay Singal](https://experts.vt.edu/3354-vijay-singal), אחד מכותבי המאמר, בבקשה לנתונים, קוד או הבהרה לגבי `PCTLAP`.
2. **חלופה 2 — בדיקת כיסוי עדכני:** להשלים ידנית רבעוני DB1B מ־2016Q4 ועד היום, ולהגדיר רשימת אירועי תעופה מאוחרים.
3. **חלופה 3 — פיילוט חלל:** לבנות `event_master` קטן ומאומת לכמה כשלי שיגור, כולל חומרת האירוע, חברות חשופות, tickers ומקורות.
4. **החלטת מסלול:** להשוות את שלוש החלופות לפי זמינות נתונים, היתכנות מדד החשיפה, כיסוי returns/IV, תרומה מקורית וסיכוני זיהוי.

## 📦 חומרי עבודה שכבר קיימים

- [מאמר המפתח וה־PDF](literature/README.md)
- [ניתוח נתוני NBER DB1A/DB1B](docs/nber_db1a_findings.md)
- [טבלת 119 כשלי השיגור מ־ESA DISCOS](data/space/processed/esa_discos_failed_launches_since_2000.csv)
- [מזכר ההחלטה](docs/00_decision_memo.md)
- [מסמך שחזור המאמר המקורי](docs/tracks/01_airline_replication.md)
- [מסמך הרחבת החלל](docs/tracks/03_space_extension.md)

</div>
