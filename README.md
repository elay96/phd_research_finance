<div dir="rtl">

<div align="center">

# 🚀 הצעה למחקר דוקטורט: השפעות פיננסיות של אירועי בטיחות בתעשיות התעופה והחלל

</div>

## 🎯 מטרת המסמך

המסמך מציג שלוש חלופות מחקר סביב אותה שאלה כלכלית: כיצד אירוע בטיחותי משפיע על החברה המעורבת, על מתחרותיה ועל חברות החשופות לאותם שווקים או לקוחות.

המטרה בשלב זה אינה לאשר מסלול מראש, אלא **לבצע בדיקת היתכנות ממוקדת לכל חלופה, להשוות ביניהן, ואז לבחור את מסלול הדוקטורט**.

## 📖 נקודת המוצא המתודולוגית

המאמר המרכזי הוא [Bosch, Eckard & Singal (1998), *The Competitive Impact of Air Crashes: Stock Market Evidence*](literature/README.md).

המאמר בוחן את תגובת מחירי המניות להתרסקויות מטוסים קטלניות. הוא מבחין בין שני מנגנונים אפשריים: מעבר לקוחות למתחרות (switching) ופגיעה כלל־ענפית (negative spillover).

המדד המרכזי, `PCTLAP`, הוא שיעור ה־RPM של חברת תעופה שאינה מעורבת בהתרסקות, שמקורו בקווים שהיא חולקת עם חברת התעופה שהתרסקה.

## 🛤️ שלוש חלופות מחקר

<div dir="ltr">

| Option | Focus | Pros | Cons | Current position |
| --- | --- | --- | --- | --- |
| **1. Original-paper replication + IV** | Replicate the original result and add IV. | Clear benchmark and direct link to the paper. | May depend on author data and exact PCTLAP implementation. | NBER archive and key paper are available. Contact [Vijay Singal](https://experts.vt.edu/3354-vijay-singal). |
| **2. Later aviation-event extension** | Test later air-crash events. | Same economic setting with a newer sample. | Needs post-2016 data and an event definition. | Historical NBER data are available through 2016Q3. |
| **3. Space-launch-failure extension** | Test launch failures, competitors and contractors. | Potentially original setting; event universe already exists. | Exposure mapping may be difficult. | ESA DISCOS has 119 failure-flagged launches since 2000. |

</div>

## 🧭 תהליך העבודה המוצע

1. **חלופה 1: שחזור המחקר המקורי והוספת נתוני IV.**
   - לפנות ל־[Vijay Singal](https://experts.vt.edu/3354-vijay-singal), אחד מכותבי המאמר, בבקשה לנתונים המקוריים, לקוד, או להסבר על בניית `PCTLAP`.
   - לשחזר את נתוני התעופה מתוך [NBER DB1A/DB1B](https://www.nber.org/research/data/department-transportation-db1adb1b) ולהוסיף תשואות מניה ו־IV. האתגר המרכזי הוא שחזור חפיפת המסלולים, `PCTLAP`.

2. **חלופה 2: מחקר תעופה חדש על אירועים מאוחרים יותר.**
   - לקחת את מבנה המחקר המקורי ולבנות מדגם של אירועי תעופה מאוחרים יותר.
   - לנתח תשואות ו־IV יחד, לאחר השלמת נתוני DB1B מאז 2016Q4 והגדרה עקבית של מדד החפיפה.

3. **חלופה 3: מחקר חדש על כשלי שיגור בחלל.**
   - להשתמש ב־ESA DISCOS כבסיס לאירועי שיגור וכשל. ב־extract הנוכחי יש 119 שיגורים המסומנים ככושלים מאז 2000.
   - במקום לשחזר את `PCTLAP`, לבנות `ContractOverlap`: עד כמה חוזים של חברה i מגיעים מאותם לקוחות ממשלתיים ומאותם סוגי פרויקטים כמו חברה j.
   - להשתמש ב־[USAspending](https://www.usaspending.gov/) כמקור ממשלתי פתוח לנתוני חוזים פדרליים בארה״ב.

## 📦 חומרי עבודה שכבר קיימים

- [מאמר המפתח וה־PDF](literature/README.md)
- [ניתוח נתוני NBER DB1A/DB1B](docs/nber_db1a_findings.md)
- [טבלת 119 כשלי השיגור מ־ESA DISCOS](data/space/processed/esa_discos_failed_launches_since_2000.csv)
- [מזכר ההחלטה](docs/00_decision_memo.md)
- [מסמך שחזור המאמר המקורי](docs/tracks/01_airline_replication.md)
- [מסמך הרחבת החלל](docs/tracks/03_space_extension.md)

</div>
